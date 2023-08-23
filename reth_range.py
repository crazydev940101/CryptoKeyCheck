import multiprocessing
from multiprocessing import Pool
import random
from ecdsa import SigningKey, SECP256k1
import sha3

r = 1
cores = 8

def seek(r):
    filename = "list.txt"
    with open(filename) as f:
        add = f.read().split()
    add = set(add)
    print('\n', "---start---", '\n')
    z = 1
    w = 0
    count = 0
    hex64 = '0000000000000000000000000000000000000000000000000000000000000001'
    random_number = random.randint(1, 100000000000000000000000000000000000000000000000000000000000000000000000)
    while True:        
        count += 1
        if count % 100 == 0:
            random_number = random.randint(1, 100000000000000000000000000000000000000000000000000000000000000000000000)
            hex64_int = int(hex64, 16)
            hex64_int += random_number
            count = 0
        else:
            hex64_int = int(hex64, 16)
            hex64_int += 1
        hex64 = hex(hex64_int)[2:].zfill(64)
        if hex64_int > int('ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff', 16):
            hex64 = '0000000000000000000000000000000000000000000000000000000000000001'

        hex_priv_key = str(hex64)
        keccak = sha3.keccak_256()
        priv = SigningKey.from_string(string=bytes.fromhex(hex_priv_key), curve=SECP256k1)
        pub = priv.get_verifying_key().to_string()
        keccak.update(pub)
        kec = keccak.hexdigest()[24:]
        ethadd = '0x' + kec
        privatekey = priv.to_string().hex()
        addr = ethadd.lower()
        print('Total:', str(z), ' ----- Winner:', str(w), '----- Checking ----- ', str(addr), ' ----- ', str(privatekey), end='\n', flush=True)
        z += 1
        if addr in add:
            print('Winning:', str(w), ' --- ', str(z), ' --- Total Scan Checking ----- ETH Address =', str(addr), end='\r')
            w += 1
            z += 1
            f = open("range.txt", "a")
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
