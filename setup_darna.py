import os
import subprocess
import webbrowser
import shutil
import time
from pathlib import Path
import socket

##setup with git: sudo apt-get install git
##git clone"https://github.com/seapoe1809/Darna"
##cd into the dir

##cmd to start process python3 setup_darna.py
print('*************WELCOME TO DARNA Health Intent*************')
print('*******self custody your health data************')
print(' Step 1: Will try to install rsync (to help sync the Health_server files), caffeine (to prevent the device from falling asleep while running Health_server.')

#get rsync to import zip files from Health_server
#get caffeine to help the computer stay awake and not fall asleep so it is available to nexcloud app
subprocess.run(['sudo', 'apt-get', 'install', 'rsync'])
subprocess.run(['sudo', 'apt-get', 'install', 'caffeine'])

#Darna.hi will use third party https://github.com/k0rventen/apple-health-grafana to visualize the apple health data. Cloning repository in the current directory and modifying the volume: of yml file...
grafana_repository='https://github.com/k0rventen/apple-health-grafana'
result = subprocess.run(['git', 'clone', grafana_repository])
if result.returncode ==0:
 	print("repository cloned...")
else: 	
	print("failed to clone the repository :(")
	

	
#Making the necessary directories:
#make a new dir to expand healthdata into
new_dir_name = 'Health_server'
home_dir = Path.home()
HS_path = os.path.join(str(home_dir), new_dir_name)
subprocess.run(['mkdir', HS_path])
#making necessary subdirectories, #Health_files #upload, #ocr_files
Health_files = 'Health_files'
upload_dir = 'upload'
ocr_files = 'ocr_files'

Health_files = os.path.join(str(HS_path), Health_files)
subprocess.run(['mkdir', Health_files])
upload_dir = os.path.join(str(Health_files), upload_dir)
ocr_files = os.path.join(str(Health_files), ocr_files)
subprocess.run(['mkdir', upload_dir])
subprocess.run(['mkdir', ocr_files]) 

#Copying static and template folder for flask_server to the Health_server dir and write HS_path and ip_addr to variables.py subsequently
shutil.copytree('templates', f'{HS_path}/templates')
shutil.copytree('static', f'{HS_path}/static')
shutil.copytree('apple-health-grafana', f'{HS_path}/apple-health-grafana')

#opens browser at <ip address: 8080>
#ip address generate
#get IP address
def get_ip_address():
    # Create a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # Connect to a remote server (Google DNS)
        sock.connect(("8.8.8.8", 80))

        # Get the local IP address
        ip_address = sock.getsockname()[0]
    finally:
        # Close the socket
        sock.close()

    return ip_address
ip_address = get_ip_address()

#prepare content and write to variables.py
url =f'{ip_address}:3001'
content = f"HS_path = '{HS_path}'\nip_address= '{ip_address}'\nupload_dir ='{upload_dir}'\nHealth_files = '{Health_files}'\nocr_files = '{ocr_files}'\n"	
file_path = os.path.join(HS_path, 'variables.py')
# Open the file in write mode and write the content
with open(file_path, 'w') as file:
    file.write(content) 

#write volume in docker-compose file for apple-health-grafana
#modify the volume in docker-compose.yml
volume = f'    - {upload_dir}/export.zip:/export.zip'
grafanadocker= f'{HS_path}/apple-health-grafana/docker-compose.yml'
with open(grafanadocker, 'r') as file:
	lines = file.readlines()
	
if len(lines)>=1:
	lines[-4]= volume

with open(grafanadocker, 'w') as file:
	file.writelines(lines)	

#check for docker and install if unavailable
try:
    subprocess.run(['docker', 'version'], check=True)
except subprocess.CalledProcessError:
    print('Installing docker')
    try:
        subprocess.run(['sudo', 'apt-get', 'update'], check=True)
        subprocess.run(['sudo', 'apt-get', 'install', 'docker.io'], check=True)
    except subprocess.CalledProcessError:
        print('Installation failed; please see docker.com instructions')
print('Good news, Docker already installed')


#lets all the above startup and subsequently opens browser
print("Waiting for installation to complete!")
time.sleep(5)



#run caffeine as subprocess in background, copy darna.py to Health_server and start flask server and open browser with address.
caffeine_command= "caffeine &"
subprocess.run(caffeine_command, shell=True)
subprocess.run(['cp', 'darna.py', f'{HS_path}/'])
webbrowser.open(url)
subprocess.run(['python3', f'{HS_path}/darna.py'])


