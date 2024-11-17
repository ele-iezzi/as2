filein = open('rosalind_revp.txt', encoding = 'UTF-8')

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
            if len(sub) > 12:
                continue
            if len(sub) < 4:
                break
            temp = sub[::-1]
            temp = temp.replace('A','t')
            temp = temp.replace('C','g')
            temp = temp.replace('G','C')
            temp = temp.replace('T','A')
            temp = temp.replace('t','T')
            temp = temp.replace('g','G')
            if sub == temp:
                out = str(i + 1) + ' ' + str(len(sub))
                print(out)
                        
filein.close()


