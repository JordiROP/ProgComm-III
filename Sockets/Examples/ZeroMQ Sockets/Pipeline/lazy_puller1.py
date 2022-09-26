import zmq
import time
import numpy as np
import math

def get_work_time():
    mu = 2
    sigma = 1
    return math.fabs(np.random.normal(mu, sigma, 1))
    
context = zmq.Context()

sock = context.socket(zmq.PULL)
sock.connect("tcp://127.0.0.1:5690")

while True:
    work_time = get_work_time()
    print("Working during: {}".format(work_time))
    time.sleep(work_time)
    message = sock.recv()
    print("Received: {}".format(message))
