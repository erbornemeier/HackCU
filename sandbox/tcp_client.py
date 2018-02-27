#!/usr/bin/python3

import socket
import sys

BUF_SIZE = 1024

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: %s IP PORT" % sys.argv[0])
        sys.exit(-1)

    ip = sys.argv[1]
    port = int(sys.argv[2]) 

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Made a socket!")
    sock.connect((ip, port))

    print("connected...")

    sock.send(b"Why hello!")
    print("Sent test message...")
    data = 1
    while data:
        sock.send(b"hello?")
        data = sock.recv(BUF_SIZE)
        print("Got something!: %s" % data)

    sock.close()
