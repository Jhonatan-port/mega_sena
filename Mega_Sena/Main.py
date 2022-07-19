#import das bibliotecas necessarias
import random
from tokenize import Ignore
#cria a matriz para ser usada na função
matriz_s = []


def mostra_cartela(numeros):
#for que gera os numeros da cartela
    for maior in range(0, 60):
        
        matriz_s.append(maior + 1)
    #variavel para verificar o tamanho da cartela
    cartela = 0
    #variavel para verificar a quantidade de numeros marcados
    cartela_marcado = 0
    
    while cartela < 60:
        #if para verificar se a quantidade de numeros marcados foi excedida
        if len(numeros) > cartela_marcado:
            Ignore
            #if que verificar qual numero foi sorteado para colocar na cartela
            if(matriz_s[cartela] == numeros[cartela_marcado]):
                print("-", end= "")
                cartela_marcado += 1
                
        # print("cartela ", cartela, end=" ")
        if cartela < 10:
            print(matriz_s[cartela], end='  ')
        else:
            print(matriz_s[cartela], end=' ')
        cartela += 1
        #if para pular linhas de 10 em 10
        if(cartela == 10 or cartela == 20 or cartela == 30 or cartela == 40 or cartela == 50 or cartela == 60):
            print("\n")
    print('tamanho ', len(matriz_s))

#programa inicia
inicio = False

while inicio == False:
    print("Quantos numeros você deseja jogar: 6, 7 ou 8 numeros: ", end="")
    jogo = int(input())
    if(jogo >= 6) and (jogo <= 8):
        numeros = []
        for i in range(0, jogo):
            gera = random.randint(1, 60)
            numeros.append(gera)
        
        numeros.sort()
        print("numeros: ", numeros)
        mostra_cartela(numeros)
        inicio = True
    else:
        print("Favor digitar um numero valido.")
        inicio = False