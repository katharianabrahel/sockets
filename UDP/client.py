import socket

def consultar_dns(server_name):
    client_dns = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_dns.sendto(server_name.encode(), ('127.0.0.1', 5000))
    message, address = client_dns.recvfrom(1024)
    client_dns.close()
    return message.decode()

def enviar_solicitacao(mensagem):
    client_socket.sendto(mensagem.encode(), (host, port))
    resposta, addr = client_socket.recvfrom(1024)
    return resposta

alunos = {
    "João": [7.5, 9.2],
    "Maria": [8.0, 6.5],
    "Pedro": [6.8, 7.7],
    "Ana": [9.5, 8.9],
    "Lucas": [5.2, 6.0],
    "Carla": [7.0, 7.8],
    "Mariana": [8.5, 9.0],
    "Gustavo": [4.5, 7.2],
    "Luiza": [9.8, 9.7],
    "Fernando": [6.2, 8.4],
    "Alice": [7.3, 9.1],
    "Rafael": [8.7, 8.3],
    "Eduardo": [6.5, 7.1],
    "Larissa": [9.0, 8.5],
    "Marcos": [5.8, 6.4],
    "Isabela": [7.9, 8.2],
    "Tiago": [4.2, 7.9],
    "Juliana": [8.4, 9.3],
    "Roberto": [6.9, 7.6],
    "Tatiana": [9.2, 9.8],
    "André": [5.6, 6.7]
}

host = consultar_dns('udp-server')
port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    #Cadastro de notas
    print("Cadastrando aluno e nota...\n")
    for nome, notas in alunos.items():
        nota1 = notas[0]
        nota2 = notas[1]
        solicitacao = f"Cadastrar {nome} {nota1} {nota2}"
        print(enviar_solicitacao(solicitacao).decode())
    
    #Listar as notas
    print("\nListando os alunos cadastrados...\n")
    solicitacao = "Listar"
    print(enviar_solicitacao(solicitacao).decode())

    #Esperar tecla para sair
    print("Pressione qualquer tecla para fechar o programa...")
    input()
    print("Programa encerrado.")
    client_socket.close()
    break