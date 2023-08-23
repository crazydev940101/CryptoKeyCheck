import multiprocessing
from multiprocessing import Pool
from ecdsa import SigningKey, SECP256k1
import sha3
import os
import binascii

r = 1
cores = 8

def seek(r):
    filename = "test.txt"
    with open(filename) as f:
        add = f.read().split()
    add = set(add)
    print('\n', "---start---", '\n')
    count = 0
    z = 0
    w = 0
    addr = ''
    while True:
        if 1 <= z <= 10000000:
            random_bytes = os.urandom(32)
            mhash = binascii.hexlify(random_bytes).decode()
        elif 10000001 <= z <= 10010000:
            random_bytes = os.urandom(32)
            mhash = binascii.hexlify(random_bytes).decode()
            hex_priv_key = str(mhash)
            keccak = sha3.keccak_256()
            priv = SigningKey.from_string(string=bytes.fromhex(hex_priv_key), curve=SECP256k1)
            pub = priv.get_verifying_key().to_string()
            keccak.update(pub)
            kec = keccak.hexdigest()[24:]
            ethadd = '0x' + kec
            privatekey = priv.to_string().hex()
            addr = ethadd.lower()
            print('Total:', str(count), ' ----- Winner:', str(w), '----- Checking ----- ', str(addr), ' ----- ', str(privatekey), end='\n', flush=True)
        elif z > 10010001:
            addr = '0x2a8c2857b1b1b58a6a89dc1dc1e95f90a9018fe2'
            z = 0
        count += 1
        z += 1
        if addr in add:
            print('Winning: ', str(w), '---' , str(count), ' --- Total Scan Checking ----- ETH Address =' , str(addr), end='\r')
            w += 1
            z += 1
            count += 1
            f = open("special_test.txt", "a")
            f.write('\nAddress = ' + str(addr))
            f.write('\nPrivate Key = ' + str(privatekey))
            f.write('\n=========================================================\n')
            f.close()
            print('Winner information Saved On text file = ADDRESS ', str(addr))
            continue
        
seek(r)

if __name__ == '__main__':
    jobs = []
    for r in range(cores):
        p = multiprocessing.Process(target=seek, args=(r,))
        jobs.append(p)
        p.start()
