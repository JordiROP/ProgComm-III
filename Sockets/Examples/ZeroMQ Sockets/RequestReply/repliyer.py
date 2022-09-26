import zmq


context = zmq.Context()

sock = context.socket(zmq.REP)
sock.bind("tcp://127.0.0.1:5678")

while True:
    message = sock.recv()
    sock.send_string("Echo: General Kenobi")
    print("Echo: {}".format(message))
    if message:
        break
