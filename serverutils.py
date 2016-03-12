#!/usr/bin/env python

__author__ = 'igulyaev'

import sys, socket
from socket import gethostbyname, gethostname, gethostbyaddr

THREAD =  "thread-base"
SEQUENCE = "sequence"
GREEN = "greenlet-based"

def open_listener_socket(host, port, type):
    for res in socket.getaddrinfo(host, port, socket.AF_INET,
        socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
        family, socktype, proto, canonname, sockaddr = res
        try:
            s = socket.socket(family, socktype, proto)
        except socket.error as msg:
            s = None
            continue
        try:
            s.bind(sockaddr)
            s.listen(5)
        except socket.error as msg:
            s.close()
            s = None
            continue
        if s is None:
            print 'could not open socket: %s' % msg
            sys.exit(1)
        print '''
            Starting %s server on %s:%s and socket %s
            ''' % (type, gethostbyname(gethostname()), port, s.getsockname())
        break
    return s

def handle_request(conn, sleep):
    try:
        data = conn.recv(1024)
        print '< Client requested', repr(data)
        sleep(0.1)
        peer = conn.getpeername()
        host = gethostbyaddr(peer[0])
        conn.send("HTTP/1.0 200 Ok \n\n Hello, {0}".format(host[0]))
        conn.shutdown(socket.SHUT_WR)
        print '> Closing connection\n>'
    except Exception, ex:
        print 'Exception: ', ex
    finally:
        sys.stdout.flush()
        conn.close()