import itertools

list_1   = [1,0,0,0,0,1,1,1,1,0,1,0,0,0,1,1,1,1,1]
list_2   = [0,1,0,1,0,1,0,0,1,1,1,0,0,0,1,0,0,1,1]
list_0 = list_2 + list_2
coeff = [bip for bip in range (1,19)]

def calc(combinaison,liist):
    output = liist[combinaison[0]-1]^liist[combinaison[1]-1]
    for i in range(2,len(combinaison)):
        output^=liist[combinaison[i]-1]
    return output

def eval0():
    res = []
    list_aux = list_1.copy()
    for combi in range(3,20):
        combinations = itertools.combinations(coeff, combi)
        for style in combinations:
            count = 0
            for i in range(1,20):
                if (calc(style,list_aux) == list_2[0-i]):
                    list_aux = [list_2[(0-i)]] + list_aux[:-1]
                    count += 1
                else:
                    list_aux = list_1.copy()
                    break
                if count == 17:
                    res.append(style)
    return res

#Polynomial representation
poly1 = [19,5,2,1] # x^19+x^5+x^2+x
poly2 = [19,6,2,1] # x^19+x^6+x^2+x
poly3 = [19,9,8,5] # x^19+x^9+x^8+x^5

polys = [poly1,poly2,poly3]

def eval1(style):
    res = []
    list_aux = list_1.copy()
    for i in range(1,20):
        count = 0
        if (calc(style,list_aux) == list_2[0-i]):
            list_aux = [list_2[(0-i)]] + list_aux[:-1]
            count += 1
        else:
            list_aux = list_1.copy()
            break
        if count == 19:
            return True
    return False  

             

def int_to_bit_list(n, num_bits=19):
    # Convertir n en chaîne binaire remplie de zéros à gauche
    bin_str = bin(n)[2:].zfill(num_bits)
    # Convertir la chaîne binaire en liste de bits
    bit_list = [int(bit) for bit in bin_str]
    return bit_list

def eval2(style):
    res = []
    list_aux = list_1.copy()
    for i in range(1,20):
        inp = calc(style,list_aux)
        list_aux = [inp] + list_aux[:-1]
    return list_aux  

def eval3():
    res = []
    list_aux = list_1.copy()
    for i in range (2**19):
        binn = int_to_bit_list(i)
        for style in polys:
            for _ in range(1,20):
                inp = calc(style,list_aux)
                list_aux = [inp] + list_aux[:-1]
    return list_aux

# Exemple d'utilisation
print(eval2(poly1))

