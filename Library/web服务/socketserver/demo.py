import socketserver


class MyServer(socketserver.BaseRequestHandler):
    def handle(self) -> None:
        """
        这里是客户端交互的内容
        :return:
        """
        while True:
            data = self.request.recv(1024)
            if len(data) > 0:
                print('->client:', data.decode('utf-8'))
            else:
                pass
            # self.request.send(data.upper())


socketserver.TCPServer.allow_reuse_address = True
server = socketserver.ThreadingTCPServer(('192.168.101.103', 10010), MyServer)
server.serve_forever()
