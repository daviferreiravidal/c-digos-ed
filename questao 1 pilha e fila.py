from collections import deque

string = input()
saida = deque()

for letra in string:
    if letra == "*":
        #mover da lista
        print(saida.popleft())
    else:
        #adicionar na lista
        saida.append(letra)

#usando lista, pode-se fazer com:
#saida = []
#else:
    #saida.insert(0, letra)
