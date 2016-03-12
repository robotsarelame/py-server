#!/usr/bin/env python

"""
greenlet aka microthreads server prototype
"""

__author__ = 'igulyaev'

import sys, serverutils, time
from serverutils import open_listener_socket, handle_request
from greenlet import greenlet

def init_connection(conn):
    gr = greenlet.getcurrent()
    gr.
    print "> new greenlet started"
    handle_request(conn, time.sleep)

def start_thread_server(host='127.0.0.1', port=8083):
    s = open_listener_socket(host, port, serverutils.GREEN)
    while True:
        conn, addr = s.accept()
        print "> Connection accepted %s" % str(addr)
        greenlet(init_connection(conn))

if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) == 0:
        start_thread_server()
    elif len(args) == 2:
        start_thread_server(args[0], args[1])