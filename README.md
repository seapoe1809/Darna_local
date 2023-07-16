##########################DO NOT USE. UNDER CONSTRUCTION#####################

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


<img src="https://github.com/seapoe1809/assets/blob/main/darna_local_assets/IMG_5771.jpeg" width =200, height=400>
<img src="https://github.com/seapoe1809/Darna/assets/82007659/96ff06aa-3739-4596-9ead-240359e40a48" width =200, height=400>
<img src="https://github.com/seapoe1809/Darna/assets/82007659/c9a21783-9c57-464a-9f8e-d71f658c7793" width =200, height=400>
<img src="https://github.com/seapoe1809/Darna/assets/82007659/0b126f2a-d66f-4bc2-a90f-1a49efb2281d" width =200, height=400>
<img src="https://github.com/seapoe1809/Darna/assets/82007659/478d54cd-5e25-4134-ba6c-21a67220b5f7" width =200, height=400>
<img src="https://github.com/seapoe1809/Darna/assets/82007659/c1756960-15b9-495e-97f2-7e0927c7cb31" width =200, height=400>
<img src="https://github.com/seapoe1809/Darna/assets/82007659/2b88836b-5375-46f8-89a8-a14d766c0813" width =200, height=400>
<img src="https://github.com/seapoe1809/Darna/assets/82007659/0d4136b1-7b2b-4435-ad05-e74712779f58" width =200, height=400>
<img src="https://github.com/seapoe1809/Darna/assets/82007659/ffc57183-8ef7-4d9e-bd39-02e580aa115a" width =200, height=400>
<img src="https://github.com/seapoe1809/Darna/assets/82007659/8ff0cb26-c491-4186-9302-8960f8ebcb54" width =200, height=400>
<img src="https://github.com/seapoe1809/Darna/assets/82007659/869afa6e-ec9d-4203-a6c9-636d55ca6e57" width =200, height=400>
<img src="https://github.com/seapoe1809/Darna/assets/82007659/b17eb880-cd9d-4657-8099-1a508f7167a8" width =200, height=400>


<img src="https://github.com/seapoe1809/Darna/assets/82007659/f1c26f0c-fb38-48e1-8551-5b36de750c91" width =200, height=400>
<img src="https://github.com/seapoe1809/Darna/assets/82007659/f718336b-e545-43e5-aa50-aa004c274954" width =200, height=400>
<img src="https://github.com/seapoe1809/Darna/assets/82007659/86ab0bce-a0da-4330-9849-2d1600262f27" width =200, height=400>
<img src="https://github.com/seapoe1809/Darna/assets/82007659/c8272ff2-69db-4984-8ebe-469cb02ee7ab" width =200, height=400>




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
 Goto your home folder Health_server and enter the following python3 commands:
        
   
               
                 $in process
       
 
 This step should lead to unzipping, syncing and setting you up with files in your health server. it should also set up Grafana to view your file. I am using https://github.com/k0rventen/apple-health-grafana code as this person seems to have done a fair job in visualizing the data. This followed by creating an encrypted backup in Darna folder done automatically by the syncmyfiles.py
 
 Step 4: Start the flask server to view your files
 ==================================================
 Go to the Health_server dir and start the flask server.
          
               $cd /home/<user>/Health_server
               $python3 darna.py
 
 
 It should tell you which ip address to go to to start interacting with your data. Hope you like it! Please share feedback and let me know if you woudl like to contribute to this project.
 
 The default password for Darna is 'health' and for Grafana is user:'admin', password:'health'.
 

 
Sources and references:
1. https://github.com/k0rventen/apple-health-grafana
2. chat.openai.com
