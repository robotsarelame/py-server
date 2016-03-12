#!/usr/bin/env python

"""
Thread server skeleton
"""

__author__ = 'IGulyaev'

import sys, threading, serverutils, time
from serverutils import open_listener_socket, handle_request

def start_thread_server(host='127.0.0.1', port=8082):
    s = open_listener_socket(host, port, serverutils.THREAD)

    while True:
        cli, addr = s.accept()
        print "> Connection accepted %s" % str(addr)
        t = threading.Thread(target=handle_request, args=(cli, time.sleep))
        t.daemon = True
        t.start()

if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) == 0:
        start_thread_server()
    elif len(args) == 2:
        start_thread_server(args[0], args[1])