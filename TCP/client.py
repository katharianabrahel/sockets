import socket


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
        nome = input("Nome do aluno: ")
        nota1 = input("Nota 1: ")
        nota2 = input("Nota 2: ")
        solicitacao = f"Cadastrar {nome} {nota1} {nota2}"
        
    
    elif escolha == "2":
        nome = input("Nome do aluno: ")
        solicitacao = f"Procurar {nome}"
        
    
    elif escolha == "3":
        solicitacao = "Listar"
        

    else:
        print("Opção inválida")

    #ENVIAR MENSAGEM
    client_socket.send(solicitacao.encode())
    #RECEBIMENTO DE RESPOSTA
    response = client_socket.recv(1024).decode()
    print(response) 

client_socket.close()
