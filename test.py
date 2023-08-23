from colorama import Fore, Style
import multiprocessing
from multiprocessing import Pool
import secrets
import sha3
import time
import fastecdsa.curve as curve
from fastecdsa import keys, curve, ecdsa

r = 1
cores = 8

def seek(r):
    filename = "list.txt"
    with open(filename) as f:
        add = f.read().split()
    add = set(add)
    print('\n', Fore.WHITE, "---start---", Style.RESET_ALL, '\n')
    z = 1
    w = 0
    start_time = time.time()
    count = 0
    hex64 = secrets.token_hex(32)
    while True:
        count += 1
        if count % 10000 == 0:
            hex64 = secrets.token_hex(32)
            count = 0

        hex64_int = int(hex64, 16)
        hex64_int += 1
        hex64 = hex(hex64_int)[2:].zfill(64)



        hex_priv_key = str(hex64)
        priv_key = int(hex_priv_key, 16)

        # Generate the public key
        pub_key = keys.get_public_key(priv_key, curve.P256)

        # # Compute the address
        # keccak = sha3.keccak_256()
        # keccak.update(pub_key.x.to_bytes(32, 'big'))
        # keccak.update(pub_key.y.to_bytes(32, 'big'))
        # kec = keccak.hexdigest()[24:]
        # ethadd = '0x' + kec

        # # Convert private key to bytes
        # private_key_bytes = priv_key.to_bytes(32, 'big')

        # # Convert private key to hex
        # private_key_hex = private_key_bytes.hex()

        # Convert address to lowercase
        # addr = ethadd.lower()

        addr = hex64

        # print(Fore.WHITE,'Total:', str(z), ' ----- Winner:', str(w), '----- Checking ----- ', str(addr), ' ----- ', str(privatekey), end='\n', flush=True)
        z += 1

        elapsed_time = time.time() - start_time
        if elapsed_time >= 1.0:
            # Calculate the count per second
            count_per_second = count / elapsed_time
            
            # Display the result
            print("Count per second:", count_per_second)
            
            # Reset the count and start time for the next second
            count = 0
            start_time = time.time()

        if addr in add:
            print('Winning', Fore.GREEN, str(w), Fore.WHITE, str(z), Fore.YELLOW, 'Total Scan Checking ----- ETH Address =', Fore.GREEN, str(addr), end='\r')
            w += 1
            z += 1
            f = open("Success.txt", "a")
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
