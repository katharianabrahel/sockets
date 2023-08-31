import socket

def registrar_server():
    server_name, addr = server_dns.recvfrom(1024)
    server_name = server_name.decode()
    registro_dns[server_name] = addr[0]
    print(f"DNS registrou o servidor {server_name}, IP: {addr[0]}")

registro_dns = {}

host = '127.0.0.1'
port = 5000

server_dns = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_dns.bind((host,port))

#RECEBER O REGISTRO DOS SERVIDORES:
print("Esperando registro dos servidores...")
registrar_server()
registrar_server()

#RESPONDER SOLICITAÇÕES DNS
print("DNS disponível para solicitações...")
while True:
    message, addr = server_dns.recvfrom(1024)
    message = message.decode()
    server_dns.sendto(registro_dns[message].encode(), addr)







