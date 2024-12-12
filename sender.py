import socket


head = 10

def send():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((socket.gethostname(),3031))
    s.listen(5)
    
    while True:
        clientsocket,address = s.accept()
        
        
        mess = input("enter message: ")
        msg = f'{len(mess) :<{head}}'+mess
        
        clientsocket.send(bytes(msg, "utf_8"))
        clientsocket.shutdown(socket.SHUT_RDWR)
        clientsocket.close()
        
        break
send()