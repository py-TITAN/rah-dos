import os
import time
from colorama import init,Back,Fore
init()
print(Fore.GREEN)
print()
print("Example www.site.ru")
print("Select ip")
ip = input("$ ")
print("Choose")
mamber = input()
ddos = ('ping ' + ip + '-t -l ' + mamber)
os.system(ddos)
