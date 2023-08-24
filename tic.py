import requests 
import time 
import threading 
import os
import string
import random
from colorama import Fore, Back, Style











u = '   ,    '


os.system('clear')
    

print(Fore.RED +'\t\t\t\t░█████╗░██████╗░░█████╗░')
time.sleep(0.3)
print(Fore.RED +'\t\t\t\t██╔══██╗██╔══██╗██╔══██╗')
time.sleep(0.3)
print(Fore.RED +'\t\t\t\t╚█████╔╝██████╔╝╚██████║')
time.sleep(0.3)
print(Fore.RED +'\t\t\t\t██╔══██╗██╔══██╗░╚═══██║')
time.sleep(0.3)
print(Fore.RED +'\t\t\t\t╚█████╔╝██║░░██║░█████╔╝')
time.sleep(0.3)
print(Fore.RED +'\t\t\t\t░╚════╝░╚═╝░░╚═╝░╚════╝░\n')
time.sleep(0.3)


print (Fore.RED + '\t\t\t programmed by >>> insta : @8r9.8\n\n')
time.sleep(1)


us = int(input('Enter the username Count like a : 4 , 6 ,3 >> : '))

u = '   ,    '



class info :
        
    url = ""
    headers = {}
    threa = ''
    username = ''



def req5 ():
    
        
        y = info()
        y.username = 'qwertyuiofsdhjy655877345346_______.........ererttplkj63......553hgfdsa_____zxcvbnm1234567890_.'
        r = random.sample(y.username,us)

        user = ''.join(r)
        

        y.url = f'https://www.tiktok.com/@{user}'
        y.headers = {'user-agent':'Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/20.0 Chrome/106.0.5249.126 Mobile Safari/537.3'}
        if user.endswith ('.'):
            print (Fore.RED + f"This user is Already exists > : {user}")
        else :
            req = requests.get(url=y.url,headers=y.headers).status_code
        
        try : 

            if req == 404 :
                print (Fore.GREEN + f'This user is Available >> : {user}')
                print ('\n')
            elif req == 403 :
                print (Fore.LIGHTRED_EX + 'You are BANNED')
            else :
                print (Fore.RED + f"This user is Already exists > : {user}")
                print ('\n')
        except :
            print (Fore.CYAN + '\n\n\n instagram : @8r9.8\n\n\n')
            





ppp = input ('do yo wanna use the threading ? ')
print ('\n')

if ppp == 'n':
     while True :
          time.sleep(1)
          req5()
else :
    def thread ():
        thr = int(input ('threading >> : '))
        print ('\n')
        for i in range (thr):

            th = threading.Thread(target=req5)
            th.start()






    th1 = threading.Thread(target=thread)
    th2 = threading.Thread(target=thread)
    th1.start()
    th2.start()