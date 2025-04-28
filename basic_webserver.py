import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8080))
server_socket.listen(5)

while True:
    client_socket, address = server_socket.accept()
    data = client_socket.recv(1024).decode('utf-8')
    method, path, _ = data.split(' ', 2)
    
    if path == '/hello':
        response = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nHello, World!"
    else:
        response = "HTTP/1.1 404 Not Found\r\nContent-Type: text/plain\r\n\r\nNot Found"
    
    client_socket.send(response.encode('utf-8'))
    client_socket.close()