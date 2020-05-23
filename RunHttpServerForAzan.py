#!/usr/bin/env python
# Start lightweight httpd.server to serve mp3 files for Azan playing on Google Home Mini Speakers
#

import http.server
import socketserver
import os

PORT = 8000

path = "/home/pi/AZAN/mp3"
os.chdir(path)

# print("New path: " + os.getcwd())

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()