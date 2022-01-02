from datetime import datetime , timedelta
from time import sleep


class Cache:
    cache_ip_list ={}

    @classmethod
    def get_ip_from_cache(self,domain,id):
        if domain in self.cache_ip_list:
            self.cache_ip_list[domain]['last_update'] = datetime.now()
            return id+self.cache_ip_list[domain]['respons']
        else:
            return False


    @classmethod
    def add_to_cache(self,domain,respons):
        self.cache_ip_list[domain] ={}
        self.cache_ip_list[domain]['respons'] = respons[4:]
        self.cache_ip_list[domain]['last_update'] = datetime.now()
        self.cache_ip_list[domain]['create_time'] = datetime.now()

    @classmethod
    def cache_cleaner (self):
        while True:
            sleep(600)
            temp_list = {}
            create_time = datetime.now() - timedelta(minutes=59)
            last_update = datetime.now() - timedelta(minutes=9)
            for domain in self.cache_ip_list:
                if self.cache_ip_list[domain]['last_update'] > last_update and self.cache_ip_list[domain]['create_time'] > create_time:
                    temp_list[domain] = self.cache_ip_list[domain]

            self.cache_ip_list = temp_list
                #if self.cache_ip_list[domain]['last_time'] < last_time:
                 #   self.cache_ip_list.pop(domain)





#cash = Cache()
#cash.add_to_cache('google.com','aasfsadgasdga')
#cash.add_to_cache('google.ru','aasfsadgasdga')
#cash.add_to_cache('google.rr','aasfsadgasdga')
#cash.cache_ip_list['google.rr']['last_update'] = datetime.now()-timedelta(minutes = 15)
#cash.cache_ip_list['google.com']['create_time'] = datetime.now()-timedelta(minutes = 70)
#print(cash.cache_ip_list)
#cash.cache_cleaner()
#print(cash.cache_ip_list)
#print(cash.cache_ip_list)
#print(cash.cache_ip_list['google.com']['last_time']+timedelta(minutes = 10))
#print(cash.cache_ip_list['google.com']['last_time'])
#print(datetime.now()-timedelta(minutes = 10))
#print(cash.cache_ip_list)