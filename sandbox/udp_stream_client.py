#!/usr/bin/python3

import socket
import sys
import cv2
import numpy as np
import pickle

UDP_FRAME_SIZE = 65507
NUM_PACKETS = 15

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: %s IP PORT" % sys.argv[0])
        sys.exit(-1)

    ip = sys.argv[1]
    port = int(sys.argv[2]) 
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    cap = cv2.VideoCapture(1)

    while True:
        _, frame = cap.read()

        for packet in np.split(frame, NUM_PACKETS):
            print(packet.shape)
            sock.sendto(pickle.dumps(packet), (ip, port))
        print(sys.getsizeof(frame))
        print("That's %d packets" % (sys.getsizeof(frame)//UDP_FRAME_SIZE))
        print(frame.shape)
        #sock.sendto(frame, (ip, port))
        #sock.sendto("Hello world".encode(), (ip, port))

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
