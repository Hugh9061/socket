import socket
import threading

SERVER_ADDRESS = ('192.168.2.100',9999)

Server = None
Server_Pool = []


class Server():
    
    # 初始化
    def __init__(self,host = '192.168.2.100',port = 9999,listen_count = 5):
        self.client_pool = []  #客户端线程池
        self.host = host,
        self.port = port,
        self.listen_count = listen_count
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket.bind((host,port))
        self.socket.listen(listen_count)
        print('Wating for connection......')
    
    
    # 用来处理每一个线程接收的会话
    def handle_message(self,client,address):   
        client_name = client.recv(1024).decode('utf-8')  #用户名
        print('Accect new connection from {}'.format(client_name))
        client.send('welcome to Server: {}'.format(client_name).encode('utf-8'))
        while True:
            recv_message =  client.recv(1024).decode('utf-8') #获取客户端传递的消息
            print('{} ： '.format(client_name),recv_message)
            send_message = input('回复{} :   '.format(client_name)).encode('utf-8') #待发送的消息
            client.send(send_message)
            
        
    # 开启一个线程用于接收客户端链接
    def acception(self):    
        client,address = self.socket.accept()
        self.client_pool.append((client,address))
        t = threading.Thread(target=self.handle_message,args=(client,address))
        t.start()
        
        
        
if __name__ == "__main__":
    server = Server()
    while True:
        server.acception()
    
    
    
