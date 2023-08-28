import socket

def enviar_operacao(client_socket, operacao):
    client_socket.send(operacao.encode())
    


HOST = '127.0.0.1'
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

while True:
    print("Escolha uma operação:")
    print("1. Cadastrar aluno")
    print("2. Procurar aluno")
    print("3. Listar alunos")
    print("4. Sair")

    escolha = input("Digite o número da operação desejada: ")

    if escolha == "1":
        nome = input("Digite o nome do aluno: ")
        notas = input("Digite as notas separadas por espaço (ex: 7.5 8.0): ")
        enviar_operacao(client_socket, "cadastrar")
        client_socket.send(nome.encode())
        client_socket.send(notas.encode())
    elif escolha == "2":
        nome = input("Digite o nome do aluno que deseja procurar: ")
        enviar_operacao(client_socket, "procurar")
        client_socket.send(nome.encode())
    elif escolha == "3":
        enviar_operacao(client_socket, "listar")
    elif escolha == "4":
        enviar_operacao(client_socket, "sair")
        break
    else:
        print("Operação inválida. Tente novamente.")

    #ESSA É A PARTE QUE TAVA NA FUNÇÃO "ENVIAR OPERAÇÃO"
    response = client_socket.recv(1024).decode()
    print(response) 


# Fecha a conexão com o servidor
client_socket.close()
