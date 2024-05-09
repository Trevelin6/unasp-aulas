from random import randint
#importando o método randint da classe random

esComp = randint(0,100)
#utilizando o método randint para gerar um inteiro aleatório entre 0 e 100

tentativas = list()
#criando a lista que irá guardar todas as tentativas do jogador


def leiaInt(msg):
    #método para validar o valor digitado, recebe um texto como parâmetro
    while True:
        #loop infinito
        try:
            #inicia o tratamento de exceptions
            n = int(input(msg))
            #utiliza o texto para pedir um input
        except ValueError:
            #se o jogador digitar um valor que não seja um inteiro, cai aqui
            print('Valor inválido')
        else:
            #se estiver tudo certo, ele retorna o número, encerrando o laço
            return n


while True:
    esJog = leiaInt('Digite um número inteiro: ')
    #chamando o método que valida o valor digitado
    tentativas.append(esJog)
    #adiciona a tentiva na lista de tentativas
    if esComp == esJog:
        #se o jogador acertar o número
        print(f"Parabéns, você acertou!O número era {esComp}")
        break
    elif esJog > esComp:
        #se o jogador escolher um número mais alto
        print("Tente um número mais baixo")
    else:
        #sobrou apenas se o jogador escolher um número menor
        print("Tente um número mais alto")


print(f"Você fez {len(tentativas)} tentativas, e elas foram: \n {tentativas}")
#essa linha será executada quando o laço acabar, mostrando o número total de tentivas
#e quais foram as tentivas, que foram previamente salvas na lista