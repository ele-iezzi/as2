filein = open('rosalind_splc.txt', encoding = 'UTF-8')
convert = open('rna_codon_table.txt', encoding = 'UTF-8')
tab = convert.read()

out = ''
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
for elem in DNA_list:
    DNA = DNA.replace(elem, '')

DNA = DNA.replace('T', 'U')

for i in range(0, len(DNA)-2, 3):
    stringa = DNA[i:i + 3]
    index = tab.find(stringa)
    if tab[index + 4:index + 8] == 'Stop':
        break
    out = out + str(tab[index + 4])

filein.close()
convert.close()
print(out)
