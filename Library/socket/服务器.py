import socket


def service_client(new_socket):
    """
    服务器发送数据
    1. 浏览器链接到网站服务的时候，首先向服务器发送数据
    2. 通过HTTP/HTTPS去发送数据
    3. 使用tcp套接字先去接收字节数据[http协议]
    :return:
    """
    # 接受数据
    request = new_socket.recv(1024)
    print(request)
    # 向浏览器发送http数据 如果浏览器在接受完http协议之和遇到了换行，将下面的数据转成网站内容 body中去
    response = 'HTTP/1.1 200 OK \r\n'
    response += '\r\n'
    # 构建你想显示的数据内容
    response += 'hello world'
    # 浏览器接受到的数据是有编码集的，所以我们需要对字符串进行编码
    new_socket.send(response.encode('utf-8'))
    # 服务完成后，浏览器需要释放系统资源
    new_socket.close()
    # 美化网站：将一个html文件返回到浏览器中


def main():
    # 创建套接字：socket模块2个参数 网络协议 和 连接协议
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    """
    操作系统由于65535个服务端口
    HTTP 80
    SSH 22
    网站指定端口 443
    
    程序完成任务之后释放端口，刷新资源
    """
    # 服务器服务中的的时候，释放窗口
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 绑定本机信息
    """
    通过浏览器去访问网站资源【数据 html css JavaScript 静态文件（图片 音频）】
    需要浏览器首先找到这台电脑的ip
    绑定电脑的ip地址
    window 内核api cpu 寄存器 
    """
    tcp_server_socket.bind(('', 80))
    # 设置监听模式，等待浏览器连接,最大连接数
    tcp_server_socket.listen(128)
    # 网站服务
    while 1:
        # new_socket 负责浏览器发送数据的
        # client_addr 记录当前链接电脑的ip:port
        new_socket, client_addr = tcp_server_socket.accept()
        # 向客户端发送数据
        service_client(new_socket)


if __name__ == '__main__':
    main()
