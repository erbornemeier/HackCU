#!/usr/bin/python2
import os, sys, inspect, thread, time, socket, ctypes
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
# Windows and Linux
arch_dir = '../lib/x64' if sys.maxsize > 2**32 else '../lib/x86'
# Mac
#arch_dir = os.path.abspath(os.path.join(src_dir, '../lib'))

sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))

import Leap

class SampleListener(Leap.Listener):
    def set_socket(self, sock):
        self.sock = sock

    def on_connect(self, controller):
        print "ohai"

    def on_frame(self, controller):
        #print "I have a frame!"
        frame = controller.frame()

        #print "Frame id: %d, timestamp: %d, hands: %d, fingers: %d" % (frame.id, frame.timestamp, len(frame.hands), len(frame.fingers))

        #payload = frame.serialize
        #payload_addr = payload[0].cast().__long__()
        buf = (ctypes.c_ubyte * payload[1]).from_address(payload_addr)
        #sock.send(str(payload[1]))
        print(payload[0])
        sock.send(buf)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: %s IP PORT" % sys.argv[0])
        sys.exit(-1)

    ip = sys.argv[1]
    port = int(sys.argv[2]) 

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))

    listener = SampleListener()
    listener.set_socket(sock)
    controller = Leap.Controller()

    controller.add_listener(listener)

    print "Press enter to quit"
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        controller.remove_listener(listener)
        sock.close()

