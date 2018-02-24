#!/usr/bin/python3

import socket
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: %s IP PORT" % sys.argv[0])
        sys.exit(-1)

    ip = sys.argv[1]
    port = int(sys.argv[2]) 

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("i'm sending now")
    sock.sendto("Hello world".encode(), (ip, port))
    print("kbye")
