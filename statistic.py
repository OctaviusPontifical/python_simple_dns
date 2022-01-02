from datetime import datetime

from config import setting

STATISTIC_PATH = setting.get_param("STATISTIC_PATH")

# sours ip : domain : time
def record_statistic (ip , domain ):
     #   print(file.readlines()[-1])
    with open (STATISTIC_PATH, 'a') as file:
        time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        file.write('%s:%s:%s\n'%(ip,domain,time))
