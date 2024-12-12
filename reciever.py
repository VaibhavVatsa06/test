import socket

head = 10

def recieve():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((socket.gethostname(),3031))
    
    try:
        while True:
            full_msg = ''
            new_msg = True
            while True:
                msg = s.recv(16)
                if new_msg:
                    msglen = int(msg[: head])
                    new_msg = False
                full_msg += msg.decode("utf-8")
                
                print(full_msg)
                
                if len(full_msg)-head == msglen:
                    transfer = full_msg[head :]
                    new_msg = True
                    full_msg = ''
    except:
        pass

recieve()