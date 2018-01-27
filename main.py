#-*-coding:utf-8-*-

import cv2
import numpy
import socket
import time

def main():
    port = 12345
    bufsize = 1024*64

    cv2.namedWindow("viewer", 1)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('', port))
    while True:
        data = sock.recv(bufsize)
        narray = numpy.fromstring(data, dtype = "uint8")
        decimg = cv2.imdecode(narray,1)
        cv2.imshow("viewer", decimg)
        if cv2.waitKey(1) == 27:
            break

    sock.close()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
