# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# AUTOR: PROF. CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
#
# SCRIPT: Base de um servidor HTTP (python 3)
#

# importacao das bibliotecas
import socket

# definicao do host e da porta do servidor
HOST = '' # ip do servidor (em branco)
PORT = 8080 # porta do servidor

# cria o socket com IPv4 (AF_INET) usando TCP (SOCK_STREAM)
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# permite que seja possivel reusar o endereco e porta do servidor caso seja encerrado incorretamente
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# vincula o socket com a porta (faz o "bind" do IP do servidor com a porta)
listen_socket.bind((HOST, PORT))

# "escuta" pedidos na porta do socket do servidor
listen_socket.listen(1)

# imprime que o servidor esta pronto para receber conexoes
print ('Serving HTTP on port %s ...' % PORT)

while True:
    # aguarda por novas conexoes
    client_connection, client_address = listen_socket.accept()
    # o metodo .recv recebe os dados enviados por um cliente atraves do socket
    request = client_connection.recv(1024)
    # imprime na tela o que o cliente enviou ao servidor
    request = request.decode('utf-8')
    print('Cliente Enviou:[>{}<]'.format(request))
    #print(request)
    vetor = request.split(" ")
    texto = ""
    corpo = """
<html>
<head></head>
<body>
<h1>404 Not Found</h1>
</body>
</html>
\r\n
"""
    corpo2 = """
<html>
<head></head>
<body>
<h1>400 Bad Resquest</h1>
</body>
</html>
\r\n
"""
    # declaracao da resposta do servidor
    if vetor[0] == "GET":
            if vetor[1] != "" and vetor[1] != "/":
                #print(vetor)
                caminho = vetor[1]
                try:
                    a = open(caminho[1:])
                except Exception:
                    print('erro de caminho!!')
                    confirmacao = 'HTTP/1.1 404 Not Found\r\n\r\n'
                    client_connection.send(confirmacao.encode('utf-8'))
                    client_connection.send(corpo.encode('utf-8'))
                
                texto = a.read()
                print(texto)
                confirmacao = 'HTTP/1.1 200 OK\r\n\r\n'
                client_connection.send(confirmacao.encode('utf-8'))
                client_connection.send(texto.encode('utf-8'))
            elif vetor[1] == '/':
                a = open("index.html")
                texto = a.read()
                confirmacao = 'HTTP/1.1 200 OK\r\n\r\n'
                client_connection.send(confirmacao.encode('utf-8'))
                client_connection.send(texto.encode('utf-8'))
                print(texto)
            else:
                print('erro de caminho!!')
                confirmacao = 'HTTP/1.1 404 Not Found\r\n\r\n'
                client_connection.send(confirmacao.encode('utf-8'))
                client_connection.send(corpo.encode('utf-8'))
    elif request == '':
        print('pedido do logo')

    else:
        print('erro de comando!!')
        confirmacao = 'HTTP/1.1 400 Bad Request\r\n\r\n'
        client_connection.send(confirmacao.encode('utf-8'))
        client_connection.send(corpo2.encode('utf-8'))


    # servidor retorna o que foi solicitado pelo cliente (neste caso a resposta e generica)
    #client_connection.send(texto.encode('utf-8'))
    # encerra a conexao
    client_connection.close()

# encerra o socket do servidor
listen_socket.close()