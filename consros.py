filein = open('rosalind_cons.txt', encoding = 'UTF-8')

DNA_list =[]
i = -1
for line in filein:
    if '>' in line:
        i = i + 1
        DNA_list.append('')
        continue
    else:
        DNA_list[i] = DNA_list[i] + line.replace('\n', '')
        
A = []
C = []
G = []
T = []

for i in range(0, len(DNA_list[0])):
    A.append(0)
    C.append(0)
    G.append(0)
    T.append(0)
    for elem in DNA_list:
        if elem[i] == 'A':
            A[i] = A[i] + 1
        elif elem[i] == 'C':
            C[i] = C[i] + 1
        elif elem[i] == 'G':
            G[i] = G[i] + 1
        elif elem[i] == 'T':
            T[i] = T[i] + 1

out = ''

for i in range(0,len(A)):
    maximum = A[i]
    char = 'A'
    if C[i] > maximum:
        maximum = C[i]
        char = 'C'
    if G[i] > maximum:
        maximum = G[i]
        char = 'G'
    if T[i] > maximum:
        maximum = T[i]
        char = 'T'
    out = out + char

outA = 'A: '
for elem in A:
    outA = outA + str(elem) + ' '
outA = outA[0:len(outA)-1]

outC = 'C: '
for elem in C:
    outC = outC + str(elem) + ' '
outC = outC[0:len(outC)-1]

outG = 'G: '
for elem in G:
    outG = outG + str(elem) + ' '
outG = outG[0:len(outG)-1]

outT = 'T: '
for elem in T:
    outT = outT + str(elem) + ' '
outT = outT[0:len(outT)-1]

out = out + '\n' + outA + '\n' + outC + '\n' + outG + '\n' + outT
fileout = open('rosalind_cons_sol.txt', 'w', encoding = 'UTF-8')
fileout.write(out)
filein.close()
fileout.close()

        
