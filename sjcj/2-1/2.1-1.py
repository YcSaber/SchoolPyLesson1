# 导入socket及依赖库
import socket
import threading
import time


# 建立TCP链接

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 绑定地址以及监听端口

s.bind(('127.0.0.1',6666))

# 监听端口

s.listen(5)
print('等待连接...')

# 创建服务器端应答函数

def tcp(sock, addr):
    print('接受新的连接，地址 %s:%s...' % addr)
    sock.send(b'Success!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Welcome! %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('连接已关闭 %s:%s' %addr)
    
    
    
# 循环处理客户端连接

while True:
    sock, addr = s.accept()
    # 创建新线程处理TCP连接
    t = threading.Thread(target=tcp, args=(sock,addr))
    t.start()