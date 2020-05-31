#!/user/bin/python3

import os 
import time
#set up debian server on proxmox

#update server
print('\n=====Getting updates=====\n\n')
os.system('apt-get update')
os.system('apt-get upgrade')
print('Updates complete...')

#install preferred packages
print('\n=====Getting preferred packages=====\n\n')
os.system('apt-get install sudo vim nano wget net-tools')
print('Preferred packages installation complete...')

#configure and start SSH
print('\n=====Configuring SSH=====\n\n')
os.system('cd')
os.system('cd /etc/ssh')
os.system('rm sshd_config')
os.system('curl -o sshd_config https://raw.githubusercontent.com/harrisonglotz/debian-setup/master/sshd_config')

print('\n=====Starting SSH=====\n\n')
os.system('systemctl start sshd')
os.system('systemctl restart sshd')

#change timezone to Standard Est. Time
print('\n=====Setting Timezone=====\n\n')
os.system('timedatectl set-timezone America/New_York')
os.system('timedatectl status')

#create new sudo user
print('\n=====Creating sudo user=====\n\n')
username = input('Enter username for sudo user: ')
os.system(f'adduser {username}')
os.system(f'usermod -aG sudo {username}')

print('*****Set up script complete!*****')







