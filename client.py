
import socket

from config import setting

DNS_SERVER_IP = setting.get_param("DNS_SERVER_IP")

def send_request(message):
    clien_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        clien_sock.sendto(message,(DNS_SERVER_IP,53))
        respons,_ = clien_sock.recvfrom(4096)
    finally:
        clien_sock.close()
    return respons



