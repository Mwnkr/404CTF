import time
import socket
from Crypto.Util.number import bytes_to_long,long_to_bytes
from tqdm import tqdm
import os

server = "challenges.404ctf.fr"
port = 31953

invSBox = [
    0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb,
    0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb,
    0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e,
    0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25,
    0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92,
    0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84,
    0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06,
    0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b,
    0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73,
    0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e,
    0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b,
    0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4,
    0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f,
    0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef,
    0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d,
]


def f_inv( block):
        b1 = block & 0xff
        b2 = (block>>8) & 0xff
        b3 = (block>>16) & 0xff
        b4 = (block>>24) & 0xff
        b4^=b3
        b4 = invSBox[b4]
        b3 = invSBox[b3]
        b3^=b1
        b1^=b2
        b2 = invSBox[b2]
        b2^=b1
        b1 = invSBox[b1]
        return (b1<<24) + (b2<<16) + (b3<<8) + b4

# Connect to the server
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect((server, port))

# Wait for the server to send the help message
conn.recv(1024)

def encrypt_text(text_hex):
    # Send the encrypt command with the hexadecimal text to encrypt
    conn.send(f"encrypt {text_hex}\n".encode())
    # Receive the encrypted text from the server
    encrypted_text = bytes.fromhex(conn.recv(1024).decode().strip())

    # Convert the encrypted text to hexadecimal and return it
    return encrypted_text
    

def decrypt_text(text_hex):
    # Send the encrypt command with the hexadecimal text to encrypt
    conn.send(f"decrypt {text_hex}\n".encode())
    # Receive the encrypted text from the server
    decrypted_text = bytes.fromhex(conn.recv(1024).decode().strip())

    # Convert the encrypted text to hexadecimal and return it
    return decrypted_text

def slide():
    bip = os.urandom(4)
    p_0s = []
    p_1s = []
    
    # Generate p_0s and p_1s lists
    for _ in tqdm(range(2**16)):
        p_0 = os.urandom(4) + bip
        p_1 = os.urandom(4) + bip
        while p_0 == p_1:
            p_1 = os.urandom(4) + bip
        c_0 = encrypt_text(p_0.hex().zfill(16))
        c_1 = decrypt_text(p_1.hex().zfill(16))
        p_0s.append((p_0, c_0))
        p_1s.append((p_1, c_1))
    
    # Loop through p_0s and p_1s lists to check for the condition
    for p in tqdm(p_0s):
      for p_p in p_1s:
          if p[1][4:] == p_p[1][4:] and p[0] != p_p[0]:
              print('p0,c0',p)
              print('p1,c1',p_p)
              k_0 = f_inv(bytes_to_long(p_p[0][:4]) ^ bytes_to_long(p[0][:4])) ^ bytes_to_long(p[0][4:]) #100% juste
              k_0 = long_to_bytes(k_0)
              k_1 = f_inv(bytes_to_long(p_p[1][:4]) ^ bytes_to_long(p[1][:4])) ^ bytes_to_long(p[1][4:])
              k_1 = long_to_bytes(k_1)
              if k_0 == k_1:
                  return k_0

def slidek1():    
    bip = os.urandom(4)
    pp_0s = []
    pp_1s = []
    
    # Generate pp_0s and pp_1s lists
    for _ in tqdm(range(2**16)):
        pp_0 = bip + os.urandom(4)
        cc_0 = decrypt_text(pp_0.hex().zfill(16))
        pp_1 = bip + os.urandom(4)
        while pp_0 == pp_1 :
            pp_1 = bip + os.urandom(4)
        cc_1 = encrypt_text(pp_1.hex().zfill(16))
        pp_0s.append((pp_0, cc_0))
        pp_1s.append((pp_1, cc_1))
    
    # Loop through pp_0s and pp_1s lists to check for the condition
    for pp in tqdm(pp_0s):
      for pp_p in pp_1s:
          if pp[1][:4] == pp_p[1][:4] and pp[0] != pp_p[0]:
              print('p0,c0',pp)
              print('p1,c1',pp_p)
              k_1 = f_inv(bytes_to_long(pp_p[0][4:]) ^ bytes_to_long(pp[0][4:])) ^ bytes_to_long(pp[0][:4])
              k_1 = long_to_bytes(k_1)
              k_0 = f_inv(bytes_to_long(pp_p[1][4:]) ^ bytes_to_long(pp[1][4:])) ^ bytes_to_long(pp[1][:4])
              k_0 = long_to_bytes(k_0)
              if k_1 == k_0:
                  return k_1
        
k_0 = slide().hex()
k_1 = slidek1().hex()
conn.send(f"check {k_0} {k_1}\n".encode())
print(conn.recv(1024).decode().strip())
time.sleep(0)
# Example usage


# TODO: Implement key recovery and flag retrieval

# Close the connection
conn.close()
