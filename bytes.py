import math

n = int(input())

total = n
temporest = 0
tempototal = 0

print(f'Transmitindo {n} bytes...')

temp = 0
media = 0
res = 0
count = 0

while total > 0:
    num = int(input())
    temp += num
    count += 1 
    tempototal += 1
    total -= num
    
    if count == 5:
        if temp == 0:
            print('Tempo restante: pendente...')
            count = 0
        else: 
            media = (temp/5)
            res = math.ceil((n-temp)/media)
            if res >= 15 and res <= 16:
                res = 15
            n -= temp
            if res != 0:
                print(f'Tempo restante: {res} segundos.')
            temp = 0
            count = 0

print(f'Tempo total: {tempototal} segundos.')
    