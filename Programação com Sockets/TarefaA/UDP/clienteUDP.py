# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# PROF. CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
# ALUNO: SÉRGIO PIRES BARRA
# SCRIPT: Cliente de sockets UDP modificado para enviar o comando 'data' ao servidor e aguardar resposta (python 3)
#

# importacao das bibliotecas
from socket import * # sockets

# definicao das variaveis
serverName = 'localhost' # ip do servidor a se conectar
serverPort = 61000 # porta a se conectar
clientSocket = socket(AF_INET, SOCK_DGRAM) # criacao do socket UDP

message = input('Digite o comando para o servidor: ')
clientSocket.sendto(message.encode('utf-8'),(serverName, serverPort)) # envia mensagem para o servidor
modifiedMessage, serverAddress = clientSocket.recvfrom(2048) # recebe do servidor a resposta
print ('O servidor (\'%s\', %d) respondeu com: %s' % (serverName, serverPort, modifiedMessage.decode('utf-8')))
clientSocket.close() # encerra o socket do cliente