#!/usr/bin/env python
# coding: utf-8

import pychromecast
import socket
import sys
import time

# Function to be called from crontab job
# Arg1: devices string e.g. "Living Room Speaker, Kitchen Speaker"
# Arg2: path of mp3 file

def playOnCC(speakerslist, mediafile, requested_volume):
    # Find out IP of this machine
    MyIP = [myip for myip in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] 
    if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for     s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if myip][0][0]
    
    
    # print(MyIP)
    
    chromecasts = pychromecast.get_chromecasts()
 
    for cc in chromecasts:
        print(cc.device.friendly_name)
        if cc.device.friendly_name in speakerslist:
            # print(cc.device.friendly_name)
            cast = cc
            cast.wait()
            mc = cast.media_controller
            # Save prevVolume and set to requested volume 
            # RESET TO PREV VOLUME DOES NOT WORK AS WE DO NOT BLOCK EXECUTION/NOR MULTI-THREAD
            # print("Requested Volume: {}", requested_volume)

#             if requested_volume != None:
#                 prevVolume = cast.status.volume_level
#                 cast.set_volume(requested_volume)
            
            cast.set_volume(requested_volume)
            # print("Previous Volume: {}", prevVolume)
            
            mc.play_media('http://' + MyIP + ':8000/' + mediafile, 'audio/mpeg')
            mc.block_until_active()
            
#             if requested_volume != None:
#                 cast.set_volume(prevVolume)

    print([cc.device.friendly_name for cc in chromecasts])

print(sys.argv)

# Convert volume to float
requestedVolume = float(sys.argv[3]) if len(sys.argv) > 1 else None

# Call the function playOnCC with command line arguments
# playOnCC(sys.argv[1], sys.argv[2])
playOnCC(sys.argv[1], sys.argv[2], requestedVolume)