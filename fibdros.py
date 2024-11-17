filein = open('rosalind_fibd.txt', encoding='UTF-8')

numeri = filein.readline().split(' ')
n = int(numeri[0])
m = int(numeri[1])
k = 1 
lista = []
lista.append(1)
lista.append(1)

for i in range(2, n):
    lista.append(lista[i - 2] * k + lista[i - 1])
    if(i >= m):
        lista[i] = lista[i] - lista[i - m]
        death = lista[i - m]
        for j in range(i - m, i):
            lista[j] = lista[j] - death

filein.close()
print(lista[n - 1])
