filein = open('rosalind_prtm.txt', encoding = 'UTF-8')
table = open('monoisotopic_mass_table.txt', encoding = 'UTF-8')
prot = filein.read().replace('\n','')
tab = table.read()

out = 0
for char in prot:
    index = tab.find(char)
    weight = float(tab[index + 2 : index + 11])
    out = out + weight
    
filein.close()
table.close()
print(out)

