import time
import os
import socket
msg =  '''
 _____ _   _   ___   _   _   ___ _____ _____ _____ 
|_   _| | | | / _ \ | \ | | / _ \_   _|  _  /  ___|
  | | | |_| |/ /_\ \|  \| |/ /_\ \| | | | | \ `--. 
  | | |  _  ||  _  || . ` ||  _  || | | | | |`--. \
  | | | | | || | | || |\  || | | || | \ \_/ /\__/ /
  \_/ \_| |_/\_| |_/\_| \_/\_| |_/\_/  \___/\____/ 
  WEB and NETWORKING bot for hacking
'''
os.system("clear")
print(msg)
target = input("(target)-->")
try: 
 wifi = socket.socket("192.168.1.1")
 socket.connect(wifi)
 print("[+]connction stable")
 hosting = socket.socket(target)
 socket.connect(hosting)
 print("[+]host online")
 nmap = "nmap -Pn -T4 -A "+target 
 ssl = "testssl -U "+target
 cyper = "testssl "+target
 nikto = "nikto --host "+target
 host = "host "+target
 os.system(nmap)
 os.system(ssl)
 os.system(cyper)
 os.system(nikto)
 os.system(host)
except:
 print("[-]connction error")