filein = open('rosalind_mrna.txt', encoding = 'UTF-8')
rna_table = open('rna_codon_table.txt', encoding = 'UTF-8')
prot = filein.read().replace('\n','')
tab = rna_table.read()

out = 1
for char in prot:
    out = out * tab.count(' ' + char + ' ')
    
out = out * tab.count('Stop')
out = out % 1000000

filein.close()
rna_table.close()
print(out)
