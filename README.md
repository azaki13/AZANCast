# AZANCast
# Play Azan (aka Adhan) MPEG files at correct times daily to one or more Chromecast Speaker devices (e.g. Google Home mini).
# Currently on Raspberry Pi (hence the user pi) but can be run on any Python 3 capable box
# 
# This program updates the crontab for user pi to to include 2 programs to be run at reboot and
# multiple Azan/other media as needed. You will need to edit this file to add lines to setup the string
# strPlayFajrAzaanMP3Command and add the call to function addAzaanTime().
# 
# It is important that a reboot is needed to start the webserver serving the media files.
# 
# To install/initialize:
#      1. From the ~pi/AZAN folder run: python3 /home/pi/AZAN/updateAzaanTimers.py
#      2. Reboot either from the Raspberry Menu at top left corner of screen or Run from command line: 
#         pi@raspberrypi:~ $ sudo reboot <CR>
# That is it!
# You can view the crontab by running the following command at command line:  crontab -l
# Some Credits and history: As a starting point I got the main code from a friend who had downloaded "possibly" from https://github.com/achaudhry/adhan. The code was downloaded 3+ years ago, in Python 2 and had been updated by my friend over the years to work to wired speakers. 
# My additional needs were: 
# 1. Play to Google Home (Chromecast capable) devices
# 2. Be self contained i.e. not needing external media server so it has one less dependency. 
# 
# I will add more description later. Feel free to comment.
