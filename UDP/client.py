import socket

def enviar_solicitação(mensagem):
    client_socket.sendto(mensagem.encode(), (host, port))
    resposta, addr = client_socket.recvfrom(1024)
    return resposta


host = '127.0.0.1'
port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

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
        print(enviar_solicitação(solicitacao).decode())
    
    elif escolha == "2":
        nome = input("Nome do aluno: ")
        solicitacao = f"Procurar {nome}"
        print(enviar_solicitação(solicitacao).decode())
    
    elif escolha == "3":
        solicitacao = "Listar"
        print(enviar_solicitação(solicitacao).decode())

    elif escolha == "4":
        print("Saindo")
        client_socket.close()
        break
    
    else:
        print("Opção inválida")