import socket

def calcular_status(media):
    if media >= 7.0:
        return "Aprovado"
    return "Reprovado"

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

server_socket.close()