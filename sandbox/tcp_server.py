#!/usr/bin/python3

import socket
import sys

BUFFER_SIZE = 1024

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: %s IP PORT" % sys.argv[0])
        sys.exit(-1)

    ip = sys.argv[1]
    port = int(sys.argv[2]) 

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.bind((ip, port))
    sock.listen(1)

    conn, addr = sock.accept()
    while True:
        data = conn.recv(BUFFER_SIZE)
        if not data:
            break
        print("Got data: %s" % data)
    conn.close()

