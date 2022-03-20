from datetime import datetime

from config import setting

STATISTIC_PATH = setting.get_param("STATISTIC_PATH")
STATISTIC = int(setting.get_param("STATISTIC"))


class Statistic:
    address_list = []


    @classmethod
    def init(self):
        try:
            file = open(STATISTIC_PATH)
            for line in file:
                domain = line.rstrip('\n')
                self.address_list.append(domain)
            file.close()
        except FileNotFoundError:
            None
        except Exception as e:
            print('Не предвиденная ошибка :', e)

    @classmethod
    def record_statistic (self,ip , domain ):
        if STATISTIC :
            if domain not in self.address_list:
                self.address_list.append(domain)
                add_domain_to_file(domain)


def add_domain_to_file(domain):
    with open(STATISTIC_PATH, 'a') as file:
        file.write(domain+'\n')


    #with open (STATISTIC_PATH, 'a') as file:
     #   time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
      #  file.write('%s:%s:%s\n'%(ip,domain,time))

