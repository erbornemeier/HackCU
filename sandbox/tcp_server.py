#!/usr/bin/python3

import socket
import sys
import struct

import os, inspect, thread, time, ctypes
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))

arch_dir = '../lib/x64' if sys.maxsize > 2**32 else '../lib/x86'

sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))

import Leap

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
        frame = Leap.Frame()
        frame.deserialize(data, len(data))
        print(int(data.decode("utf-8")))
        if not data:
            break
        print("Got data: %s" % data)
    conn.close()

