import socket  # 导入 socket 模块
 
ADDRESS = ('192.168.2.100',9999) #绑定的地址

s = socket.socket()  # 创建 socket 对象
s.connect(ADDRESS)  #连接地址

s.send('张三'.encode('utf-8'))

print(s.recv(1024).decode(encoding='utf8'))  #显示服务器发过来的消息


while True:
    send_message = input('向Server发送：  ').encode('utf-8')
    s.send(send_message)
    print('Server：  ',s.recv(1024).decode(encoding='utf-8')) #接收服务器那边传递过来的消息
    if send_message == 'exit':
        break

