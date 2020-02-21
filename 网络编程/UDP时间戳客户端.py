from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)
udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input('请输入你想发送的数据:')
    if not data:
        break
    udpCliSock.sendto(bytes(data, encoding='UTF-8'), ADDR)
    data, ADDR = udpCliSock.recvfrom(BUFSIZ)
    if not data:
        break
    data = data.decode('utf-8')
    print(data)

udpCliSock