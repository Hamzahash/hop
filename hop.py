#coding=utf-8
import os,sys,subprocess
if not os.path.isfile('/data/data/com.termux/files/usr/bin/node'):
    os.system('pkg install nodejs -y')
    os.system('python hop.py')
current_os=subprocess.check_output('uname -om',shell=True)
if 'aarch64' in str(current_os):
    if not os.path.isfile('h64'):
        os.system('curl -L https://github.com/Hamzahash/files/blob/main/h64?raw=true > h64')
        os.system('chmod 777 h64')
        os.system('./h64')
    else:
        os.system('./h64')
elif 'arm' in str(current_os):
    if not os.path.isfile('h32'):
        os.system('curl -L https://github.com/Hamzahash/files/blob/main/h32?raw=true > h32')
        os.system('chmod 777 h32')
        os.system('./h32')
    else:
        os.system('./h32')
else:
    print('\n  Unknown device, aarch or os found, contact author.')
    print('  Owner whatsapp: +92321-5822365\n\n')
    os.sys.exit()
