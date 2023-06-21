# Darna_local which creates a local instance/ server without need for nextcloud
##DARNA Healthy Intent v1.0- An open source intiative - self custody of your health data
##feel free to contribute
##Early stage. Beta and under development and isnt secure. Please take all steps to safeguard your data. 

What is this project?
======================
Darn the siloed health system!! 
This project is an open-source software that helps you store your health data that is currently saved in different places like electronic health records, fitness apps, and wearable devices. 

With this software, you can bring all your health data together in one place on your computer at home. When you visit a new doctor, you can choose to share your health data with them on demand through email, link etc. This way, you have full custody of your health data and can decide who to share it with.

I created this project because I had trouble moving my own health data when I switched healthcare providers. As someone who works in the healthcare space, I see that current EHR solutions make it difficult to port your data, even though there are regulatory requirements to do so. It's frustrating to see that some institutions still rely on fax and scan to move data around, which shows how outdated and hidden these data porting techniques are.

This is just the first iteration of the project, and I anticipate that there will be many more iterations before it takes a good form. But my goal is to make it easier for people to take ownership of their health data and store it in one place on their own computer. This way, they can decide who to share it with and have more control over their own health.

License?
========
This program is free software; you can redistribute it and/or modify it under the terms of the Darna modified GNU General Public License as published by the Free Software Foundation.
The Darna modification does require citing this repo when using the code. ; 

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

Snapshots:
=============
<img src="https://github.com/seapoe1809/Darna/assets/129666906/f3a34322-8402-485c-b8d0-cc70bf9cd2bc" width="200" height="400" alt="Image1"/>
<img src="https://github.com/seapoe1809/Darna/assets/129666906/7feb1a14-7e6a-4273-b571-1f1a282350b3" width="200" height="400" alt="Image1"/>
<img src="https://github.com/seapoe1809/Darna/assets/129666906/a4a53580-2943-4942-bf03-06d913ac8a4e" width="200" height="400" alt="Image1"/>
<img src="https://github.com/seapoe1809/Darna/assets/129666906/3e5e2600-eab8-40a8-9e15-c17fa8a46e6c" width="200" height="400" alt="Image1"/>
<img src="https://github.com/seapoe1809/Darna/assets/129666906/0d6b7ae8-b95b-4306-ad80-99a193f99dad" width="200" height="400" alt="Image1"/>
<img src="https://github.com/seapoe1809/Darna/assets/129666906/ae934f4a-cde2-426c-846b-6d03fd1c673d" width="200" height="400" alt="Image1"/>
<img src="https://github.com/seapoe1809/Darna/assets/129666906/bc569065-d8d8-4238-bd94-26943e20d74e" width="200" height="400" alt="Image1"/>
<img src="https://github.com/seapoe1809/Darna/assets/129666906/3b8481ac-ccd5-4fcd-95ea-c614c4ece37d" width="200" height="400" alt="Image1"/>
<img src="https://github.com/seapoe1809/Darna/assets/129666906/cbf00dd4-b45d-4137-8306-e90bdae8159b" width="200" height="400" alt="Image1"/>
<img src="https://github.com/seapoe1809/Darna/assets/129666906/a59bdd51-caa0-409d-994f-27c716b82b93" width="200" height="400" alt="Image1"/>)
<img src="https://github.com/seapoe1809/Darna/assets/129666906/a94d831b-df02-4389-94fa-39aae382e380" width="200" height="400" alt="Image1"/>



basic requirements
=======================================
#linux os (any distro as long as docker runs)
#git
#docker
#python3

For my project, I decided to make the software only for Linux users. I have gotten rid of step using nexcloud given the finickiness of its installation that requires domain registration and port forwarding of router. If you are willing to
play with Nextcloud because it has built-in security features, and it already has apps available for iOS, Android please use the Darna installation steps.

To make things even easier, I used Python for some automation to move files on your computer, create encrypted backups, and create some basic visualizations of your health data. This way, you can easily manage your health data, keep it secure, and view it in a way that makes sense to you.

Please note that this is only the first version of the project, and I plan on adding more features and making improvements in the future.

step 1: Git clone and install Darna_local
=======================================

a) Make sure you have docker and python3. If not go to docker.com and python3; get a free acct and then install. Once done do the following:
 Install Git and git clone Darna_local repo:
 
 
              $sudo apt-get install git
              $git clone https://github.com/seapoe1809/Darna
              $cd Darna
              $pip install -r requirements.txt
              $python3 setup_darna.py
        


Step 2: Download your health data in the health_server folder
=========================================================
a) Download ios health files: On apple health app, click the profile icon, then choose "Export All Health Data" and save the zip file in nextcloud to 'Darnahi' folder.
 
b) If you have data on EPIC MyChart or your doctors gateway, login and go to Menu, search 'sharing' or 'export', click 'yourself' and download a zip file to 'Darnahi' folder.
 
c) Scan PDF's: On nextcloud, choose the '+' menu in the lower center and make scanned pdf's of your health documents and save to the 'Darnahi' folder.

 
 
 Step 3: sync files to your health server, unzip, create encrypted backups:
 ==========================================================================
 Goto your home folder Darna and enter the following python3 commands:
        
   
               
                 $python3 syncmyfiles.py
       
 
 This step should lead to unzipping, syncing and setting you up with files in your health server. it should also set up Grafana to view your file. I am using https://github.com/k0rventen/apple-health-grafana code as this person seems to have done a fair job in visualizing the data. This followed by creating an encrypted backup in Darna folder done automatically by the syncmyfiles.py
 
 Step 4: Start the flask server to view your files
 ==================================================
 Go to the Health_server dir and start the flask server.
          
               $cd /home/<user>/Health_server
               $python3 darna.py
 
 
 It should tell you which ip address to go to to start interacting with your data. Hope you like it! Please share feedback and let me know if you woudl like to contribute to this project.
 
 The default password for Darna is 'health' and for Grafana is user:'admin', password:'health'.
 

 Other issues:
 
## Help needed for android nextcloud app setup, downloads and PDF scans OCR recognition
 
Sources and references:
1. https://github.com/k0rventen/apple-health-grafana
2. chat.openai.com
