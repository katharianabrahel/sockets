import socket
import time


def consultar_dns(server_name):
    client_dns = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_dns.sendto(server_name.encode(), ('127.0.0.1', 5000))
    message, address = client_dns.recvfrom(1024)
    client_dns.close()
    return message.decode()


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

with open("tempo_TCP.txt", "w") as arquivo_tempo:

    HOST = consultar_dns('tcp-server')
    PORT = 54321

    while True:
        #Cadastro de notas
        print("Cadastrando aluno e nota...\n")
        tempo_inicio = time.time()
        for nome, notas in alunos.items():
            nota1 = notas[0]
            nota2 = notas[1]
            solicitacao = f"Cadastrar {nome} {nota1} {nota2}"
            inicio_solicitacao = time.perf_counter()
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((HOST, PORT))
            client_socket.send(solicitacao.encode())
            response = client_socket.recv(1024).decode()
            final_solicitacao = time.perf_counter()
            print(response)
            tempo_transmissao = final_solicitacao - inicio_solicitacao
            print(f"Tempo para cadastrar: {tempo_transmissao * 10 ** 3:.3f}ms")
            arquivo_tempo.write(f"Tempo para cadastrar: {tempo_transmissao * 10 ** 3:.3f}ms\n")
            client_socket.close()

        #Listar as notas
        print("\nListando os alunos cadastrados...\n")
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, PORT))
        solicitacao = "Listar"
        client_socket.send(solicitacao.encode())
        response = client_socket.recv(1024).decode()
        print(response)
        tempo_final = time.time()

        tempo_total = tempo_final - tempo_inicio
        arquivo_tempo.write(f"Tempo total: {tempo_total * 10 ** 3:.3f}ms\n")
        print(f"O tempo total foi de: {tempo_total * 10 ** 3:.3f}ms")

        #Esperar tecla para sair
        print("Pressione ENTER para salvar os tempo no arquivo .txt")
        input()
        print("Programa encerrado.")
        client_socket.close()
        break