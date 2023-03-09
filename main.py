import os
msg = '''
 _____ _   _   ___   _   _   ___ _____ _____ _____ 
|_   _| | | | / _ \ | \ | | / _ \_   _|  _  /  ___|
  | | | |_| |/ /_\ \|  \| |/ /_\ \| | | | | \ `--. 
  | | |  _  ||  _  || . ` ||  _  || | | | | |`--. \
  | | | | | || | | || |\  || | | || | \ \_/ /\__/ /
  \_/ \_| |_/\_| |_/\_| \_/\_| |_/\_/  \___/\____/ 
  bots for hacking tasks
 1}web and network
 2}SCADA
 3}ddos exploit method
 '''
choose = input("-->")
if(choose==1):
 os.system("python3 bot/thanatosbot.py")
if(choose==2):
 os.system("python3 bot/scadathanathos.py")
if(choose==3):
 os.system("python3 bot/ddosthanatos.py")
else:
 os.system("exit")