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
    z = 1
    w = 0
    count = 0
    random_bytes = os.urandom(32)
    # hex64 = binascii.hexlify(random_bytes).decode()
    while True:
        count += 1
        # if count % 1000 == 0:
        #     random_bytes = os.urandom(32)
        #     hex64 = binascii.hexlify(random_bytes).decode()
        #     count = 0

        hex64 = 'da0e5cfff6538ab8640ee77ce95f6fa78432ac54611a5bab9afac26e537ca062'

        hex64_int = int(hex64, 16)
        hex64_int += count
        hex64 = hex(hex64_int)[2:].zfill(64)

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
            print('Winning: ', str(w), ' --- ', str(z), ' --- Total Scan Checking ----- ETH Address =', str(addr), end='\r')
            w += 1
            z += 1
            f = open("reth_1k_test_success.txt", "a")
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
