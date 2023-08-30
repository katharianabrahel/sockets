import socket

def calcular_status(media):
    if media >= 7.0:
        return "Aprovado"
    return "Reprovado"

host = '127.0.0.1'
port = 12345

alunos = {}

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((host,port))

print("O servidor UDP está pronto")

while True:
    message, addr = server_socket.recvfrom(1024)
    message = message.decode()

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

    server_socket.sendto(resposta.encode(), addr)