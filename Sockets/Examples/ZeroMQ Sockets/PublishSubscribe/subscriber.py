import zmq

context = zmq.Context()

sock = context.socket(zmq.SUB)

sock.setsockopt_string(zmq.SUBSCRIBE, "3")
sock.connect("tcp://127.0.0.1:5680")

while True:
    message = sock.recv()
    print(message)
