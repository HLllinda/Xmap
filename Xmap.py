import socket
import time
import subprocess
import sys
import datetime
from threading import Thread, Lock
from queue import Queue
from  colorama import *
time.sleep(5)
#Below is a usage banner
def usage1():
	print(Fore.BLUE + "             Disclaimer:  The results that appear below are not to be used illegally,  and you are advised to use a VPN for better/accurate results                       ")
usage1()
time.sleep(4)
subprocess.call('clear',  shell=True)
# number of threads, feel free to tune this parameter as you wish
N_THREADS = 10
# thread queue
q = Queue()
print_lock = Lock()
def usage2():
	print(Fore.RED + "     usage: www.example.com                \nIf you get an error that means that you have done something wrong.                     \nYou must use a VPN or a good working proxy before attempting this type of attack                            ")
print(Fore.GREEN + " [÷]Please wait while tho tool loads up for ya.......")
time.sleep(4)
usage2()
time.sleep(5)
i = 0
while i < 10:
	i = i + 1
	print(".") 
time.sleep(3)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(Fore.RED + " CREATED BY XYLOFONN")
host = input(Fore.GREEN + "[|+|]Enter your target website url: ")
subprocess.call('clear', shell=True)
print  ("=" * 60)
time.sleep(5)

res = socket.gethostbyname(host)
print ( Fore.RED + '[+]Scanning for online hosts on ' + res)
print (Fore.BLUE + "=" * 60)
time.sleep(5)

h_name = socket.gethostname()
print(f'[+]Venemy knows the host is running on a {h_name} machine ')
print ("=" * 60)
time.sleep(5)

print ("                  YOUR RESULTS ARE BELOW                          ")

for port in range(20, 1024):
    conn = s.connect((host, port))
    while conn is True and conn != 1000:
        print(f"[+] {host}:{port} is open      ")
    else:
        print(f"[!] {host}:{port} is closed ")        
						
