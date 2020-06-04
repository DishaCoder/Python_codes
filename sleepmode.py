import os
import datetime
import time


def main():
    while(1):
        timesnow = str(datetime.datetime.now().time())
        tn = timesnow.split(':',2)
        #split hours nd minuts from system time
        sys_time = str((timesnow[0]+timesnow[1]+timesnow[2]+timesnow[3]+timesnow[4])) 
    
        #give time to shut down in datetime(----)
        target = str(datetime.datetime(2017,12,29,22,15,00000).time())
        tg = (target.split(':',1))
        #split hours and minuts from target time
        target_time = str(target[0]+target[1]+target[2]+target[3]+target[4])
        


        if(sys_time == target_time):
            print("Your PC is going ro shutdown...")
            os.system("shutdown /s /t 20")
            break

if __name__ == '__main__':
    main()




















'''def main():
    while(1):
        time_now = datetime.datetime.now().time()
        print(time_now.hour)
        target = datetime.datetime(2018,9,21,10,6,00,000000).time()
        print(target.hour)

        if(time_now. == target):
            os.system("shutdown /s /t 5")
            break
    
if __name__ == '__main__':
    main()'''
