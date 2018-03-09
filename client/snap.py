#!/usr/bin/env python3

import configparser
import grpc
import io
import snapshot_pb2
import snapshot_pb2_grpc
import time

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

# open a channel
server +=  ":" + str(port)
channel = grpc.insecure_channel(server)

# create a client
client = snapshot_pb2_grpc.snap_shotStub(channel)

# capture an image
myImage = io.BytesIO()
with PiCamera() as camera:
    camera.resolution = (xres, yres)
    camera.hflip = hflip
    camera.vflip = vflip
    camera.start_preview()
    # Warm up camera
    time.sleep(2)
    camera.capture(myImage, 'jpeg')

# create a message with image data
image = snapshot_pb2.image_data(
    image = bytes(myImage),
    sequence = 1,
    date_time = int(time.time()),
    location = location)

# send the message
result = client.add_snap(image)

print(result.reply)
