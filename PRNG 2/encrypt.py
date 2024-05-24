from LFSR import LFSR
import numpy as np
from generator import CombinerGenerator
import random as rd
from tqdm import tqdm


with open("flag.png.part","rb") as f:
	flag = f.read()

def int_to_bit_list(n, num_bits=19):
    # Convertir n en chaîne binaire remplie de zéros à gauche
    bin_str = bin(n)[2:].zfill(num_bits)
    # Convertir la chaîne binaire en liste de bits
    bit_list = [int(bit) for bit in bin_str]
    return bit_list

def xor(b1, b2):
	return bytes(a ^ b for a, b in zip(b1, b2))

#Polynomial representation
poly1 = [19,5,2,1] # x^19+x^5+x^2+x
poly2 = [19,6,2,1] # x^19+x^6+x^2+x
poly3 = [19,9,8,5] # x^19+x^9+x^8+x^5

# initialize states
state1 = [rd.randint(0,1) for _ in range(max(poly1))] 
state2 = [rd.randint(0,1) for _ in range(max(poly2))]
state3 = [rd.randint(0,1) for _ in range(max(poly3))]

#combine function
combine = lambda x1,x2,x3 : (x1 and x2)^(x1 and x3)^(x2 and x3)

state_1 = int_to_bit_list(359839)
state_2 = int_to_bit_list(277622)
state_3 = int_to_bit_list(430367)

#Create LFSRs
L1 = LFSR(fpoly=poly1,state=state_1)
L2 = LFSR(fpoly=poly2,state=state_2)
L3 = LFSR(fpoly=poly3,state=state_3)

#Create (secure) generator
generator = CombinerGenerator(combine,L1,L2,L3)

#read the flag
clear_flag = None
with open("flag.png.enc","rb") as f:
	clear_flag = f.read()

#encrypt the flag
def encrypt():
	encrypted_flag = b''
	key = b""
	for i in range(len(clear_flag)):
		random = generator.generateByte()
		byte = clear_flag[i:i+1]
		key+=random
		encrypted_flag += xor(byte,random)
	return encrypted_flag
  
def decrypt():
	encrypted_flag = b''
	key = b""
	for i in range(len(flag)):
		random = flag[i:i+1]
		byte = clear_flag[i:i+1]
		key+=random
		encrypted_flag += xor(byte,random)
	return encrypted_flag

state = decrypt()
#print(len(state))
#print(state)
#clip = [int_to_bit_list(bop) for bop in state]
#clap = []
#for bloup in clip:
#    clap += [zoup for zoup in bloup]
#print(clap)
#print(len(clap))
#print([int(bop) for bop in state])
#write encrypted flag

with open("flag.png","w+b") as f:
	f.write(encrypt())


with open("flag.png","rb") as f:
	flog = f.read()
	print(flog[:35]==flag[:35])

def find_period(seq):
    n = len(seq)
    for i in range(1, n//2 + 1):
        if seq[:i] * (n//i) == seq[:n//i*i] and seq[:i] * (n//i + 1)[:n] == seq:
            return i
    return n

sequence = [1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0]


def unzip(oue):
	clip = [int_to_bit_list(bop,8) for bop in oue]
	clap = []
	for bloup in clip:
		clap += [zoup for zoup in bloup]
	return clap


def correl():
	max1 = 0
	indice = 0
	for ke in tqdm(range(2**19)):
		k = 2**19 - ke
		l = []
		encrypted_flag = []
		egal = []
		# initialize states
		#state1 = [rd.randint(0,1) for _ in range(max(poly1))]
		#state2 = [rd.randint(0,1) for _ in range(max(poly2))]
		#state3 = [rd.randint(0,1) for _ in range(max(poly3))]
		L3 = LFSR(fpoly=poly3,state=int_to_bit_list(k))
		#L1 = LFSR(fpoly=poly1,state=state1)
		#L2 = LFSR(fpoly=poly2,state=state2)
		#L3 = LFSR(fpoly=poly3,state=state3)	
		#generator1 = CombinerGenerator(combine,L1,L2,L3)
		for i in range(280):
			random = L3.generateBit()
			#byte = clear_flag[i:i+1]
			#key+=random
			#encrypted_flag += xor(byte,random)
			encrypted_flag.append(random)
		#encrypted_flag = unzip(encrypted_flag)
		egal = [1 for k in range(len(encrypted_flag)) if sequence[k]==encrypted_flag[k]]
		count = len(egal)/len(sequence)
		l.append(count)
		if count > max1:
			max1 = count
			indice = k
			print(indice,max1)
	moyenne = np.mean(np.array(l))
	return indice,max1,moyenne
  
  
print(correl())
