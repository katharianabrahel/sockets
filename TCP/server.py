import socket
import threading  

def registrar_DNS(server_name):
    message = f'registrar {server_name}'
    client_dns = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_dns.sendto(message.encode(), ('127.0.0.1', 5000))
    client_dns.close()

def parar_server():
    input("\nPara encerrar o servidor, pressione ENTER\n")
    message = f'apagar tcp-server'
    client_dns = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_dns.sendto(message.encode(), ('127.0.0.1', 5000))
    client_dns.close()
    server_socket.close()
    exit()

def calcular_status(media):
    if media >= 7.0:
        return "Aprovado"
    return "Reprovado"

alunos = {}

HOST = '127.0.0.1'
PORT = 54321  

registrar_DNS('tcp-server')
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print(f"O servidor TCP está pronto")

parar_servidor = threading.Thread(target=parar_server)
parar_servidor.daemon = True  
parar_servidor.start()

while True:
    client_socket, addr = server_socket.accept()
    
    message = client_socket.recv(1024).decode()

    if message.startswith("Cadastrar"):
        _, nome, nota1, nota2 = message.split()
        nota1, nota2 = float(nota1), float(nota2)
        media = (nota1 + nota2)/2
        status = calcular_status(media)
        alunos[nome] = {"Nota1": nota1, "Nota2": nota2, "Média": media, "Status": status}
        resposta = f"Aluno {nome} cadastrado com média {media:.2f} - {status}"

    elif message == "Listar":
        resposta = ""
        for nome, info in alunos.items():
            resposta += f"Nome: {nome}, Média: {info['Média']:.2f}, Status: {info['Status']}\n"
        if not alunos:
            resposta = "Não há alunos cadastrados"
        
    else:
        resposta = "Comando inválido"

    client_socket.send(resposta.encode())
    client_socket.close()
