
import random
matriz_s = []


def mostra_cartela(numeros[]):
#for menor in range(0, 6):
    for maior in range(0, 60):
                
        matriz_s.append(maior + 1)
    cartela = 0
    while cartela < 60:
        print(matriz_s[cartela], end=' ')
        cartela += 1
        
        if(cartela == 10 or cartela == 20 or cartela == 30 or cartela == 40 or cartela == 50 or cartela == 60):
            print("\n")
            
print("Quantos numeros você deseja jogar: 4, 5 ou 6 numeros ", end="")
jogo = int(input())
if(jogo >= 4) and (jogo <= 6):
    numeros = []
    for i in range(0, jogo):
        gera = random.randint(1, 60)
        numeros.append(gera)
    
    
    