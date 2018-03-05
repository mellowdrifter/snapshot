#!/usr/bin/env python3

import grpc
import snapshot_pb2
import snapshot_pb2_grpc
import time

# open a channel
channel = grpc.insecure_channel('localhost:50051')

# create a client
stub = snapshot_pb2_grpc.snap_shotStub(channel)

# create a message with image data
image = snapshot_pb2.image_data(
    sequence = 1,
    date_time = int(time.time()))

# send the image
result = stub.send_snap(image)

print(result.value)