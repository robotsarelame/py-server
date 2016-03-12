#!/usr/bin/env python

"""
Sequence server skeleton
"""

__author__ = 'IGulyaev'

import sys, time, serverutils
from serverutils import open_listener_socket, handle_request

def start_seq_server(host='127.0.0.1', port=8081):
    #s = socket.socket()
    #s.bind((host, port))
    #s.listen(5)
    #print '''
    #Starting sequence server on %s:%s and socket %s
    #''' % (gethostbyname(gethostname()), port, s.getsockname())

    s = open_listener_socket(host, port, serverutils.SEQUENCE)

    while True:
        conn, addr = s.accept()
        print "> Connection accepted %s" % str(addr)
        handle_request(conn, time.sleep)

if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) == 0:
        start_seq_server()
    elif len(args) == 2:
        start_seq_server(args[0], args[1])
