#!/usr/bin/python3

import socket
import sys
import cv2
import numpy as np
import pickle

BUF_SIZE = 660000
NUM_PACKETS = 15

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: %s IP PORT" % sys.argv[0])
        sys.exit(-1)

    ip = sys.argv[1]
    port = int(sys.argv[2]) 

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ip, port))

    cur_frames = 0
    frame = None

    while True:
        data, addr = sock.recvfrom(BUF_SIZE)
        #print("recieved msg: ", data)

        data = pickle.loads(data)
        #print(data.shape)
        if cur_frames == 0:
            frame = data
        else:
            frame = np.concatenate((frame, data), axis=0)
        cur_frames += 1

        if cur_frames == NUM_PACKETS:
            print(frame.shape)
            cv2.imshow("panini", frame)
            cur_frames = 0
            print("bonanza!")

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
