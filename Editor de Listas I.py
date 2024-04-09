from collections import deque

termo = 0
listamaster = deque([])
while termo == 0:
    linha = input()
    a = linha.split()
    if a[0] == 'X':
        termo += 1
        a = []
    elif a[0] == 'I':
        listamaster.appendleft(int(a[1]))
        a = []
    elif a[0] == 'F':
        listamaster.append(int(a[1]))
        a = []
    elif a[0] == 'P':
        tam = (len(listamaster))-1
        print(listamaster[tam])
        listamaster.remove(listamaster[tam])
        a = []
    elif a[0] == 'D':
        print(listamaster[0])
        listamaster.remove(listamaster[0])
        a = []

tamfinal = len(listamaster)
j = 0
for i in range(tamfinal):
    print(listamaster[j])
    j += 1
