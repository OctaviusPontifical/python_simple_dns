import binascii

from cache import Cache
from statistic import *
import client

DOMAIN_PATH_LIST = setting.get_param("DOMAIN_PATH_LIST")

def request_parser (data):
    message = binascii.hexlify(data)
    id = message[0:4]
    keys = message[4:8]
    position = 24
    resource =b''
    while True:
        leng = int(message[position:position + 2],16)
        position += 2
        for x in range(0, leng):
            resource +=message[position:position + 2]
            position += 2
        if message[position:position + 2] == b'00':
            break
        else:resource+=b'2e'
    return bytes.fromhex(resource.decode("UTF-8")).decode("UTF-8"),\
           id.decode("UTF-8"),\
           message[24:position].decode("UTF-8")

def respons_creater(ip, id, bytes_domain):
    keys = '8580'
    if id =='':
        keys = '8182'
    if ip == '':
        keys = '8185'
    header = '0001000100000000'
    ip_hex = ''
    for i in ip.split('.'):
        temp = hex(int(i))[2:]
        if len(temp) < 2:
            temp = '0' + temp
        ip_hex+=temp
    respons = id+keys+header+bytes_domain+'0000010001c00c0001000100000c900004'+ip_hex
    return respons





class Domain:
    domain_list= {}

    @classmethod
    def init (self):
        with open(DOMAIN_PATH_LIST) as file:
            for line in file:
                domain,ip = line.rstrip('\n').split(":")
                self.domain_list[domain]= ip

    @classmethod
    def get_ip(self,message, sours):
        domain,id,byte=request_parser(message)
        record_statistic(sours[0],domain)
        cache = Cache.get_ip_from_cache(domain,id)
        if cache:
            return binascii.unhexlify(cache)
        elif domain in self.domain_list:
            respons = respons_creater(self.domain_list[domain],id,byte)
            Cache.add_to_cache(domain,respons)
            return binascii.unhexlify(respons)
        else :
            respons = client.send_request(message)
            Cache.add_to_cache(domain,binascii.hexlify(respons).decode("utf-8"))
            return respons


#DOMAIN.init()
#print(DOMAIN.domain_list)
#print(DOMAIN.get_ip('google.ru'))
#message =b'b7e601000001000000000000056461697379067562756e747503636f6d0000010001'
#print(request_parser(message))
#print(request_parser(message))
#print(respons_creater('192.168.1.1','b7e6','056461697379067562756e747503636f6d'))