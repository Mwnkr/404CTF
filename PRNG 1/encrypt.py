from my_random import Generator
from Crypto.Util.number import long_to_bytes


BLOCK_SIZE = 4
flag = None

with open("flag.png.part",'rb') as f:
	flag = f.read()
print(type(flag))



def xor(b1, b2):
    return bytes(a ^ b for a, b in zip(b1, b2))

def get_blocks(data,block_size):
	return [data[i:i+block_size] for i in range(0,len(data),block_size)]

def pad(data,block_size):
	return data+b'\x00'*(block_size-len(data)%block_size)

def decrypt(data,block_size):
	padded_data = pad(data,block_size)
	padded_f = pad(flag,block_size)
	data_blocks = get_blocks(padded_data,block_size)
	f_blocks = get_blocks(padded_f,block_size)
	encrypted = b''

	for block in range (len(f_blocks)):
		xored = xor(data_blocks[block],f_blocks[block])
		encrypted+= xored
	return encrypted

def encrypt(data,block_size):
	padded_data = pad(data,block_size)
	data_blocks = get_blocks(padded_data,block_size)
	generator = Generator()
	encrypted = b''

	for block in data_blocks:

		rd = generator.get_random_bytes(block_size)
		xored = xor(block,rd)
		encrypted+= xored
	return encrypted




#with open("flag.png",'rb') as f:
#	flag = f.read()

with open('flag.png.enc', 'rb') as f:
	encr = f.read()
	print(len(encr))
	test1 = decrypt(encr,BLOCK_SIZE)
	test = [int(byte) for byte in test1]
	test = test[:2000]
	print(len(test),type(test),type(test[0]))

	def decrypt_1(data,block_size):
		padded_data = pad(data,block_size)
		data_blocks = get_blocks(padded_data,block_size)
		generator = Generator()
		generator.feed = test
		print(len(generator.feed))
		encrypted = b''

		for index, block in enumerate(data_blocks):
			if (index < 500):
				rd = generator.feed[index*block_size:(index+1)*block_size]
				xored = xor(block,rd)
				encrypted+= xored
			else :
				rd = generator.get_random_bytes(block_size)
				xored = xor(block,rd)
				encrypted+= xored
		return encrypted
	

with open('flag_oue.png', 'wb') as flog:
    flog.write(decrypt_1(encr, BLOCK_SIZE))

with open('flag_oue.png', 'rb') as flog:
    decrypted_data = flog.read()
    print(len(decrypted_data))

# Assuming you have defined the `flag` variable somewhere in your code
# and it contains the original flag data
print(decrypted_data[:len(flag)] == flag)
