import socket

registro_dns = {}

host = '127.0.0.1'
port = 5000

server_dns = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_dns.bind((host,port))

#REGISTRAR SERVIDORES, RESPONDER SOLICITAÇÕES E APAGAR REGISTROS
print("O servidor de nomes está funcionando...")
while True:
    message, addr = server_dns.recvfrom(1024)
    message = message.decode()
    message = message.split()
    
    if message[0] == 'registrar':
        registro_dns[message[1]] = addr[0]
        print(f"DNS registrou o servidor {message[1]}, IP: {addr[0]}")
    elif message[0] == 'solicitar':
        server_dns.sendto(registro_dns[message[1]].encode(), addr)
    elif message[0] == 'apagar':
        registro_dns.pop(message[1])
        print(f"O servidor {message[1]} foi retirado do servidor de nomes.")







