import socket

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

HOST = '127.0.0.1'
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

while True:
    #Cadastro de notas
    print("Cadastrando aluno e nota...\n")
    for nome, notas in alunos.items():
        nota1 = notas[0]
        nota2 = notas[1]
        solicitacao = f"Cadastrar {nome} {nota1} {nota2}"
        client_socket.send(solicitacao.encode())
        response = client_socket.recv(1024).decode()
        print(response)
    
    #Listar as notas
    print("\nListando os alunos cadastrados...\n")
    solicitacao = "Listar"
    client_socket.send(solicitacao.encode())
    response = client_socket.recv(1024).decode()
    print(response)

    #Esperar tecla para sair
    print("Pressione qualquer tecla para fechar o programa...")
    input()
    print("Programa encerrado.")
    client_socket.close()
    break




