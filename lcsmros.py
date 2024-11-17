filein = open('rosalind_lcsm.txt', encoding = 'UTF-8')

DNA_list =[]
i = -1
for line in filein:
    if '>' in line:
        i = i + 1
        DNA_list.append('')
        continue
    else:
        DNA_list[i] = DNA_list[i] + line.replace('\n', '')

DNA = DNA_list.pop(0)
out = ''
found = False

for i in range(0, len(DNA)):
        for j in range(len(DNA), i, -1):
            sub = DNA[i:j]
            if len(sub) < len(out):
                break
            for elem in DNA_list:
                if sub in elem:
                    found = True
                else:
                    found = False
                    break
            if found:
                out = sub
                found = False
                break
                        
filein.close()
print(out)

