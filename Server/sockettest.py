import socket
import time

INTENDTIME = "1715"
status_lost_socket = 0
def OpenSocket():
    global status_lost_socket
    HOST = "192.52.164.80"
    PORT = 22222
    BUFSIZE = 1024
    ADDR = (HOST, PORT)

    tcpSrvSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpSrvSock.bind(ADDR)
    tcpSrvSock.listen(5)

    while True:
        print('waiting for connection ...')
        tcpCliSock, addr = tcpSrvSock.accept()
        print('... connected from:', addr)

        while True:
            data = tcpCliSock.recv(BUFSIZE)
            print("data", data)
            if not data:
                continue
            if len(data) == 1:
                status_lost_socket = 1
            else:
                setTime(data)
            #tcpCliSock.send(b'got')
    tcpCliSock.close()
    tcpSrvSock.close()


def setTime(data):
    global INTENDTIME
    INTENDTIME = ""
    newData = data.encode("utf-8")
    print("newData", newData)
    INTENDTIME = newData
    print("INTENDTIME", INTENDTIME)

