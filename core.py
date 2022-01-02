
import socket
from _thread import start_new_thread
from names import *


def server() :
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('',53))
    while True:
        request,addr = sock.recvfrom(1024)
        start_new_thread(server_thread, (sock,request, addr))



def server_thread(sock,request,addres):
    respons = Domain.get_ip(request,addres)
    sock.sendto(respons, addres)




if __name__ == '__main__':
    Domain.init()
    start_new_thread(Cache.cache_cleaner,())
    server()


#print(binascii.hexlify(b'\xa0\xfc\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\tWORKGROUP\x00\x00\x01\x00\x01'))
#print(bytes.fromhex('574f524b47524f5550').decode('utf-8'))
#print(b'WORKGROUP'.hex())


