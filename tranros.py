filein = open('rosalind_tran.txt', encoding = 'UTF-8')

DNA_list =[]
i = -1
for line in filein:
    if '>' in line:
        i = i + 1
        DNA_list.append('')
        continue
    else:
        DNA_list[i] = DNA_list[i] + line.replace('\n', '')
        
purine =  ['A', 'G']
pyrimidine =  ['C', 'T']
transition = 0
transversion = 0

for i in range(0, len(DNA_list[0])):
    char = DNA_list[0][i]
    if DNA_list[1][i] == char:
        continue
    if char in purine:
        if DNA_list[1][i] in purine:
            transition = transition + 1
        else:
            transversion = transversion + 1
    else:
        if DNA_list[1][i] in purine:
            transversion = transversion + 1
        else:
            transition = transition + 1

out = transition / transversion

filein.close()
print(out)
        
