#!/usr/bin/env python

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
# That's it
# You can view the crontab by running the following command at command line:  crontab -l
#

import datetime
import pytz

from PrayTimes import PrayTimes

#
# Personalization 
#--------------------

# Select Speakers to Play Azaan on and set volume
# Current result of pychromecast.get_chromecasts() is
# Family Room Speaker,Bedroom speaker,El Orador,Study speaker,Bedroom TV

azaanSpeakers = "Family Room Speaker,Bedroom speaker"
# Volume for speakers NOT WORKING AS WE ARE NOT BLOCKING TILL END OF MEDIA PLAY
Volume = "0.5"

# DST variable to be used as the 3rd parameter to getTimes method in PrayTimes

import time
t = time.localtime()
DST = t.tm_isdst
# print(DST)


lat = 40.418789
long = -74.556110

mylocation = pytz.timezone("America/New_York")
now = datetime.datetime.now(mylocation)

PT = PrayTimes('ISNA') 
PT.setMethod(method='ISNA')

# Updated for DST
times = PT.getTimes((now.year,now.month,now.day), (lat, long), -5, DST)

print("Fajr="+times['fajr'])
print("SunRise="+times['sunrise'])
print("Duhuhr="+times['dhuhr'])
print("Asr="+times['asr'])
print("Maghrib="+times['maghrib'])
print("Isha="+times['isha'])

#Update Crontab with Prayer Times
#---------------------------------

from crontab import CronTab
#
### Some Functions
#
#Function to add azaan time to cron
def addAzaanTime (strPrayerName, strPrayerTime, objCronTab, strCommand):

    job = objCronTab.new(command=strCommand,comment=strPrayerName)
    
    timeArr = strPrayerTime.split(':')

    hour = timeArr[0]
    min = timeArr[1]

    job.minute.on(int(min))
    job.hour.on(int(hour))

    #print job

    return

def addInitialAzaanEntry (objCronTab):

    job = objCronTab.new(command="python3 /home/pi/AZAN/updateAzaanTimers.py > /tmp/updateAzaanTimers.out 2>&1",comment="Call updateAzaanTimers.py at 3:15 AM daily")
    
    job.minute.on(15)
    job.hour.on(3)
    
    return

def addAdditionalRebootEntry (objCronTab):

    job = objCronTab.new(command="python3 /home/pi/AZAN/updateAzaanTimers.py > /tmp/updateAzaanTimers.out 2>&1",comment="Call updateAzaanTimers.py at reboot")
    
    job.every_reboot()
    
    return

def addHTTPServerEntry (objCronTab):

    job = objCronTab.new(command="python3 /home/pi/AZAN/RunHttpServerForAzan.py > /tmp/azanhttp.log 2>&1",comment="Start HTTP Server started at reboot")
    
    job.every_reboot()
    
    return

system_cron = CronTab(user='pi')

#
# Build String with python3 command + selection of speakers and Azan mp3 file to play
# Note: /home/pi/AZAN/playMediaOnCcasts.py needs 3 arguments -- azaanSpeakers list, mp3 file, speaker volume
#
strPlayFajrAzaanMP3Command = 'python3 /home/pi/AZAN/playMediaOnCcasts.py \"' + azaanSpeakers + '\" \"Azan_Al_Fajr.mp3\" \"' + Volume + '\"'

strPlayAzaanMP3Command = 'python3 /home/pi/AZAN/playMediaOnCcasts.py \"' + azaanSpeakers + '\" \"mustafa ismaeel.mp3\" \"' + Volume + '\"'



#jobs = system_cron.find_command(strPlayAzaanMP3Command)

#print(jobs)

#for j in jobs:
#   system_cron.remove(j) 

#
# Build crontab using string with selection of speakers and mp3 file
#
system_cron.remove_all()

addHTTPServerEntry(system_cron)         # Start HTTP Server started at reboot

addAdditionalRebootEntry(system_cron)   # Call updateAzaanTimers.py at reboot
addInitialAzaanEntry(system_cron)       # Call updateAzaanTimers.py at 3:15 AM daily

addAzaanTime('fajr',times['fajr'],system_cron,strPlayFajrAzaanMP3Command)
#addAzaanTime('sunrise',times['sunrise'],system_cron,strPlayAzkar_SabahCommand)
addAzaanTime('dhuhr',times['dhuhr'],system_cron,strPlayAzaanMP3Command)
addAzaanTime('asr',times['asr'],system_cron,strPlayAzaanMP3Command)
addAzaanTime('maghrib',times['maghrib'],system_cron,strPlayAzaanMP3Command)
addAzaanTime('isha',times['isha'],system_cron,strPlayAzaanMP3Command)
#addAzaanTime('midNight',times['midnight'],system_cron,strPlayKorsiCommand)


system_cron.write(user='pi')