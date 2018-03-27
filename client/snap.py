#!/usr/bin/env python3

import configparser
import grpc
import io
import os
import snapshot_pb2
import snapshot_pb2_grpc
import time

from datetime import datetime
from picamera import PiCamera

#load config
config = configparser.ConfigParser()
config.read("config.ini")
location = config.get('camera', 'location')
server = config.get('camera', 'server')
port = config.get('camera', 'port')
rate = int(config.get('camera', 'rate'))
xres = int(config.get('camera', 'xres'))
yres = int(config.get('camera', 'yres'))
hflip = config.get('camera', 'hflip')
vflip = config.get('camera', 'vflip')
folder = config.get('camera', 'folder')
start_hour = int(config.get('camera', 'start_hour'))
end_hour = int(config.get('camera', 'end_hour'))


# open a channel
'''
server +=  ":" + str(port)
channel = grpc.insecure_channel(server)

# create a client
client = snapshot_pb2_grpc.snap_shotStub(channel)
'''

sequence = 1

while True:
    # only capture when we want
    while (time.localtime().tm_hour >= start_hour and
           time.localtime().tm_hour <= end_hour):

        # Create folder to store today's images
        if sequence == 1:
            today = os.path.join(folder + datetime.now().strftime('%d-%B-%Y'))
            os.makedirs(today, exist_ok=True)

        # capture an image
        with PiCamera() as camera:
            camera.resolution = (xres, yres)
            camera.hflip = hflip
            camera.vflip = vflip
            camera.start_preview()
            # Warm up camera
            time.sleep(2)
            filename = os.path.join(today + "/" + datetime.now().strftime('%H:%M:%S') + ".jpg")
            camera.capture(filename)


        sequence += 1
        time.sleep(rate)

    # Reset sequence to 1 for the next day
    sequence = 1
