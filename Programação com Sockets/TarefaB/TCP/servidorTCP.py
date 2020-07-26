# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# PROF. CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
# ALUNO: SÉRGIO PIRES BARRA
# SCRIPT: Servidor de sockets TCP modificado para receber o comando 'obter arquivo.txt' do cliente e enviar o conteúdo de um arquivo de texto (python 3)
#

# importacao das bibliotecas
from socket import * # sockets

# definicao das variaveis
serverName = '' # ip do servidor (em branco)
serverPort = 61000 # porta a se conectar
serverSocket = socket(AF_INET,SOCK_STREAM) # criacao do socket TCP
serverSocket.bind((serverName,serverPort)) # bind do ip do servidor com a porta
serverSocket.listen(1) # socket pronto para 'ouvir' conexoes
print ('Servidor TCP esperando conexoes na porta %d ...' % (serverPort))
while 1:
  connectionSocket, addr = serverSocket.accept() # aceita as conexoes dos clientes
  sentence = connectionSocket.recv(1024) # recebe dados do cliente
  sentence = sentence.decode('utf-8')
  if sentence == 'obter arquivo.txt':
    a = open('arquivo.txt')
    texto = a.read()
    print ('Cliente %s enviou: %s, enviando: %s' % (addr, sentence, texto))
    connectionSocket.send(texto.encode('utf-8')) # envia para o cliente o texto transformado
    connectionSocket.close() # encerra o socket com o cliente
  else:
    erro = 'Erro! Envie apenas o comando obter arquivo.txt'
    print ('Cliente %s enviou: %s, enviando: %s' % (addr, sentence, erro))
    connectionSocket.send(erro.encode('utf-8')) # envia para o cliente o texto transformado
    connectionSocket.close() # encerra o socket com o cliente


serverSocket.close() # encerra o socket do servidor