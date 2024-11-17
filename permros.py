filein = open('rosalind_perm.txt', encoding = 'UTF-8')

n = int(filein.readline())
l = []
fact = 1
for i in range(1, n + 1):
    l.append(i)
    fact = fact * i
print(fact)

def generate_perm(items):
    if len(items) == 0:
        return []
    if len(items) == 1:
        return [items]

    perm = []
    
    for i in range(len(items)):
        it = items[i]
        left = items[:i] + items[i + 1:]
        for sub_perm in generate_perm(left):
            perm.append([it] + sub_perm)
    
    return perm

for elem in generate_perm(l):
    out = str(elem)
    out = out.replace(',' , '')
    out = out[1:len(out)-1]
    print (out)

filein.close()
