###############################################DEPRECATED ###############################
LATEST IS AT https://github.com/seapoe1809/Health_server

# Darna_local which creates a local instance/ server without need for nextcloud
##DARNA Healthy Intent v1.2- An open source intiative - self custody of your health data
##feel free to contribute
##Early stage. Beta and under development and isnt secure. Please take all steps to safeguard your data. 

What is this project?
======================
Darn the siloed health system!! 
This project is an open-source software that helps you store your health data that is currently saved in different places like electronic health records, fitness apps, and wearable devices. 

With this software, you can bring all your health data together in one place on your computer at home. When you visit a new doctor, you can choose to share your health data with them on demand through email, link etc. This way, you have full custody of your health data and can decide who to share it with.

I created this project because I had trouble moving my own health data when I switched healthcare providers. As someone who works in the healthcare space, I see that current EHR solutions make it difficult to port your data, even though there are regulatory requirements to do so. It's frustrating to see that some institutions still rely on fax and scan to move data around, which shows how outdated and hidden these data porting techniques are.

This is just the second iteration of the project, and I anticipate that there will be many more iterations before it takes a good form. But my goal is to make it easier for people to take ownership of their health data and store it in one place on their own computer. This way, they can decide who to share it with and have more control over their own health.

License?
========
This program is free software; you can redistribute it and/or modify it under the terms of the Darna modified GNU General Public License as published by the Free Software Foundation.
The Darna modification does require citing this repo when using the code. ; 

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.


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

**step 1: Git clone and install Darna_local**
=======================================

a) Make sure you have docker and python3. If not go to docker.com and python3; get a free acct and then install. Once done do the following:
 Install Git and git clone Darna_local repo:
 
    sudo apt-get install git

 Git clone the Darna_local repo
              
    git clone https://github.com/seapoe1809/Darna_local

 Make sure pip is installed to help install python modules

    sudo apt-get install python3-pip

Change directory into the Git repo directory
              
    cd Darna_local

Now install the python modules needed to launch Darna_local
              
    pip install -r requirements.txt

Start the setup of the Darna_local
              
    python3 setup_darna.py
              
        


**Step 2: After the Health_server is set up it is ready to Launch:**
=================================================================
Now that your server is ready to launch, cd to your health_server and Launch. Navigate back to your /home/user and do the following:

    cd Health_server

The final step will now start up your **development Server**. It will show logs to debug. Make sure you do this to start server everytime you reboot your computer

    python3 darna.py

To start the **production server**. Make sure you do this to start server everytime you reboot your computer:

    gunicorn -w 1 -b 0.0.0.0:3001 darna:app

The server should be active at port :3000. The flask server when launched will give you the IP address at which it launched. You could now navigate to that http:// adddress with any mobile device and access the server.

**Troubleshooting**
===================
If you have trouble launching with $python3 darna.py, you might have to speciy the version of python. eg. 

    python3.6 darna.py 

To run server in background

    nohup python3 darna.py &

The default password it 'health'. You could change it in darna.py if you wish.



**Step3: Download your health data in the health_server folder:**
=================================================================

a) Download ios health files: On apple health app, click the profile icon, then choose "Export All Health Data" and save the zip file in files. Then click on 'UPLOAD' card on your flask server and download to your server.
 
b) If you have data on EPIC MyChart or your doctors gateway, login and go to Menu, search 'sharing' or 'export', click 'yourself' and download a zip file to 'files'.  Then click on 'UPLOAD' card on your flask server and download to your server.
 
c) PDF's and JPGS on mobile: 'UPLOAD' card of server and follow instructions to download to your server.

d) Once files are downloaded, to UPLOAD directory, click tha 'RUN SYNC' card to move files and start Grafana.

e) Tips are in 'CONNECT' card of server. 

f)  The default password for Darna is 'health' and for Grafana is user:'admin', password:'health'.

Snapshots:
=============


<img src="https://github.com/seapoe1809/assets/blob/main/darna_local_assets/IMG_5771.jpeg" width =300, height=550>
<img src="https://github.com/seapoe1809/assets/blob/main/darna_local_assets/IMG_5772.jpeg" width =300, height=550>
<img src="https://github.com/seapoe1809/assets/blob/main/darna_local_assets/IMG_5781.jpeg" width =300, height=550>
<img src="https://github.com/seapoe1809/assets/blob/main/darna_local_assets/IMG_5773.jpeg" width =300, height=550>
<img src="https://github.com/seapoe1809/assets/blob/main/darna_local_assets/IMG_5782.jpeg" width =300, height=550>
<img src="https://github.com/seapoe1809/assets/blob/main/darna_local_assets/IMG_5774.jpeg" width =300, height=550>
<img src="https://user-images.githubusercontent.com/82007659/243430051-478d54cd-5e25-4134-ba6c-21a67220b5f7.jpg" width =300, height=550>
<img src="https://github.com/seapoe1809/assets/blob/main/darna_local_assets/IMG_5775.jpeg" width =300, height=550>
<img src="https://github.com/seapoe1809/assets/blob/main/darna_local_assets/IMG_5783.jpeg" width =300, height=550>
<img src="https://github.com/seapoe1809/assets/blob/main/darna_local_assets/IMG_5778.jpeg" width =300, height=550>
<img src="https://github.com/seapoe1809/assets/blob/main/darna_local_assets/IMG_5785.jpeg" width =300, height=550>
<img src="https://github.com/seapoe1809/assets/blob/main/darna_local_assets/IMG_5786.jpeg" width =300, height=550>
<img src="https://github.com/seapoe1809/assets/blob/main/darna_local_assets/IMG_5779.jpeg" width =300, height=550>
<img src="https://github.com/seapoe1809/assets/blob/main/darna_local_assets/IMG_5777.jpeg" width =300, height=550>


<img src="https://github.com/seapoe1809/Darna/assets/82007659/f1c26f0c-fb38-48e1-8551-5b36de750c91" width =300, height=550>
<img src="https://github.com/seapoe1809/Darna/assets/82007659/f718336b-e545-43e5-aa50-aa004c274954" width =300, height=550>
<img src="https://github.com/seapoe1809/Darna/assets/82007659/86ab0bce-a0da-4330-9849-2d1600262f27" width =300, height=550>
<img src="https://github.com/seapoe1809/Darna/assets/82007659/c8272ff2-69db-4984-8ebe-469cb02ee7ab" width =300, height=550>

<img src="https://github.com/seapoe1809/assets/blob/main/darna_local_assets/IMG_5787.jpeg" width =300, height=550>
<img src="https://github.com/seapoe1809/assets/blob/main/darna_local_assets/IMG_5789.jpeg" width =300, height=550>
<img src="https://github.com/seapoe1809/assets/blob/main/darna_local_assets/IMG_5790.jpeg" width =300, height=550>
<img src="https://github.com/seapoe1809/assets/blob/main/darna_local_assets/IMG_5791.jpeg" width =300, height=550>

 
**PIE IN SKY:** Is still under construction. I imagine it a way download external apps to run on your server. It adds more functionalities and dimensions to our server. Cheers! 
 
 Hope you like it! Please share feedback and let me know if you woudl like to contribute to this project. You could send feedbac by commenting on this repo or clicking on 'CONNECT' card and clicking on link saying 'email' the writer of repo.
 

 

 
Sources and references:
1. https://github.com/k0rventen/apple-health-grafana
2. chat.openai.com
