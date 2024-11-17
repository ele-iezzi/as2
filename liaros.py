filein = open('rosalind_lia.txt', encoding='UTF-8')
data = filein.readline().strip().split(' ')

gen_level = int(data[0])
min_count = int(data[1])

def compute_fact(num):
    fact = 1
    for j in range(1, num + 1):
        fact = fact * j
    return fact

def combination(tot, chosen):
    return compute_fact(tot) // (compute_fact(chosen) * compute_fact(tot - chosen))

#Min_count Aa Bb organisms
def p_min(lvl, min_AaBb):
    size = 2 ** lvl
    
    pg_AaBb = 0.25
    pg_other = 1 - pg_AaBb
   
    pless_min = 0
    for x in range(min_AaBb):
        comb_value = combination(size, x)
        prob_x = comb_value * (pg_AaBb ** x) * (pg_other ** (size - x))
        pless_min = pless_min + prob_x

    finalp = 1 - pless_min
    return finalp

print(p_min(gen_level, min_count))

filein.close()
