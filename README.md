# AZANCast
# Play Azan (aka Adhan) MPEG files at correct times daily to one or more Chromecast Speaker devices (e.g. Google Home mini).
# Currently on Raspberry Pi (hence the user pi) but can be run on any Python 3 capable box
# 
# This program updates the crontab for user pi to to include 2 programs to be run at reboot and
# multiple Azan/other media as needed. You will need to edit this file to add lines to setup the string
# strPlayFajrAzaanMP3Command and add the call to function addAzaanTime().
# 
# Requirements:
# 1. Raspberry Pi (3 or better) with NOOBS installed, select Full Install of Raspbian OS (this gives you full GUI, etc).
#    I have used default user pi but any other user can be used. You will need to update the program as paths are hardcoded so far.
# 2. Make sure you have Python 3 installed and updated.
# 3. You will need to add Python modules that are used for "import" command in the .py files. Use command: pip3 install <module name>
# 
# To install/initialize:
#      1. Download as zip file. and unzip in /home/pi as user pi.
#      2. From the /home/pi/AZAN folder run: python3 /home/pi/AZAN/updateAzaanTimers.py
#      3. Reboot either from the Raspberry Menu at top left corner of screen or Run from command line: 
#         pi@raspberrypi:~ $ sudo reboot <CR>
# That is it!
# It is important that a reboot is needed to start the webserver serving the media files.
# 
# You can view the crontab by running the following command at command line:  crontab -l
# Some Credits and history: As a starting point I got the main code from a friend who had downloaded "possibly" from https://github.com/achaudhry/adhan. The code was downloaded 3+ years ago, in Python 2 and had been updated by my friend over the years to work to wired speakers. 
# My additional needs were: 
# 1. Play to Google Home (Chromecast capable) devices
# 2. Be self contained i.e. not needing external media server so it has one less dependency. 
# 
# I will add more description later. Feel free to comment.
# Apology: I realize this is YAAP (Yet Another Azan Player) but I felt I needed to put this together. There is another player https://github.com/OJ7/AdhanCast which also seems like a good and clean implementation.
