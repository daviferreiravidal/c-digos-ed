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

#criação de classe

class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self, item):
        return self.items.pop()
