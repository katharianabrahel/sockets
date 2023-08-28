import socket

def calcular_status(notas):
    media = sum(notas) / len(notas)
    if media >= 7.0:
        return "Aprovado"
    else:
        return "Reprovado"


def cadastrar_aluno(client_socket):
    nome = client_socket.recv(1024).decode()
    notas = [float(nota) for nota in client_socket.recv(1024).decode().split()]
    status = calcular_status(notas)
    alunos[nome] = {'notas': notas, 'status': status}
    return f"Aluno {nome} cadastrado com sucesso."


def procurar_aluno(client_socket):
    nome = client_socket.recv(1024).decode()
    if nome in alunos:
        aluno = alunos[nome]
        return f"Nome: {nome}, Notas: {aluno['notas']}, Média: {sum(aluno['notas']) / len(aluno['notas'])}, Status: {aluno['status']}"
    else:
        return f"Aluno {nome} não encontrado."


def listar_alunos():
    lista = []
    for nome, aluno in alunos.items():
        lista.append(f"Nome: {nome}, Notas: {aluno['notas']}, Média: {sum(aluno['notas']) / len(aluno['notas'])}, Status: {aluno['status']}")
    return "\n".join(lista)

alunos = {}

HOST = '127.0.0.1'
PORT = 12345  

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)
print(f"O servidor está pronto")

client_socket, addr = server_socket.accept()
print(f"Conexão recebida de {addr}")

while True:
    operacao = client_socket.recv(1024).decode()
    
    if operacao == "cadastrar":
        response = cadastrar_aluno(client_socket)
    elif operacao == "procurar":
        response = procurar_aluno(client_socket)
    elif operacao == "listar":
        response = listar_alunos()
    elif operacao == "sair":
        response = "Encerrando a conexão."
        client_socket.send(response.encode())
        break
    else:
        response = "Operação inválida."

    client_socket.send(response.encode())
client_socket.close()

server_socket.close()