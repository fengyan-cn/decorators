from socket import *
import time

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('waiting for connection')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connected from:', addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        data = data.decode('utf-8')
        if not data:
            break
        timenow = time.ctime()
        output = '[%s]:%s' %(timenow, data)
        tcpCliSock.send(output.encode('utf-8'))

    tcpCliSock.close()
print('我这个服务器要关闭了，但是我按道理应该是永远不关闭的')
tcpSerSock.close()
