from socket import *
import time

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print('waiting for message...')
    data, addr = udpSerSock.recvfrom(BUFSIZ)
    data = data.decode('utf-8')
    timenow = time.ctime()
    output = '[%s] %s' % (timenow, data)
    udpSerSock.sendto(output.encode('utf-8'), addr)
    print('...received from and returned to:', addr)

udpSerSock.close()
