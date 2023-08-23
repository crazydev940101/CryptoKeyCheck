from colorama import Fore, Style
import multiprocessing
from multiprocessing import Pool
import random
from ecdsa import SigningKey, SECP256k1
import sha3
from web3 import Web3

# Connect to an Ethereum node
web3 = Web3(Web3.HTTPProvider('https://ethereum.publicnode.com'))

# Ethereum wallet address to check the balance for
wallet_address = '0x2a8c2857b1b1b58a6a89dc1dc1e95f90a9018fe2'

# Get the balance of the wallet address
checksum_address  = web3.to_checksum_address(wallet_address)

balance_wei = web3.eth.get_balance(checksum_address)

# Convert the balance to Ether
balance_ether = web3.from_wei(balance_wei, 'ether')

# print('Wallet balance:', balance_ether, 'ETH')
# Convert the balance to Ether
# balance_ether = web3.fromWei(checksum_address , 'ether')

r = 1
cores = 8

def seek(r):
    # filename = "test.txt"
    # with open(filename) as f:
    #     add = f.read().split()
    # add = set(add)
    # print('\n', Fore.WHITE, "---start---", Style.RESET_ALL, '\n')
    z = 1
    w = 0
    count = 0
    # hex64 = 'da0e5cfff6538ab8640ee77ce95f6fa78432ac54611a5bab9afac26e537cb062'
    # hex64 = "e4baeadc3fdaf557b2cfedc7f72b*****5c8b4ca52e859da4466baa608c3db7e"


    prefix = "f58f5fe858f04d7cadde51d3ceffe"
    suffix = "56d9a8ba5efabdcda3860ed22f8ccbc"

    for i in range(0, 100000):
        current_string = prefix + format(i, '04x') + suffix

        hex_priv_key = str(current_string)
        keccak = sha3.keccak_256()
        priv = SigningKey.from_string(string=bytes.fromhex(hex_priv_key), curve=SECP256k1)
        pub = priv.get_verifying_key().to_string()
        keccak.update(pub)
        kec = keccak.hexdigest()[24:]
        ethadd = '0x' + kec
        privatekey = priv.to_string().hex()


        # Get the balance of the wallet address
        checksum_address  = web3.to_checksum_address(ethadd)

        balance_wei = web3.eth.get_balance(checksum_address)

        # Convert the balance to Ether
        balance_ether = web3.from_wei(balance_wei, 'ether')

        print(privatekey + " --- " + ethadd) 

        if balance_wei > 0:
            print('Winning', Fore.GREEN, str(w), Fore.WHITE, str(z), Fore.YELLOW, 'Total Scan Checking ----- ETH Address =', Fore.GREEN, str(ethadd), end='\r')
            w += 1
            z += 1
            f = open("result.txt", "a")
            f.write('\nAddress = ' + str(ethadd))
            f.write('\nPrivate Key = ' + str(privatekey))
            f.write('\n=========================================================\n')
            f.close()
            print('Winner information Saved On text file = ADDRESS ', str(ethadd))
            continue
        

    # while True:        
        # random_number = random.randint(1, 1000000000000000000000000000000000000000000000000000000000000000000000)
        # hex64_int = int(hex64, 16)
        # hex64_int += random_number
        # hex64 = hex(hex64_int)[2:].zfill(64)

        # if hex64_int > int('ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff', 16):
            # hex64 = '0000000000000000000000000000000000000000000000000000000000000001'

        # hex_priv_key = str(hex64)
        # keccak = sha3.keccak_256()
        # print('keccak: ', keccak.hexdigest(), end='\n')
        # priv = SigningKey.from_string(string=bytes.fromhex(hex_priv_key), curve=SECP256k1)
        # print('priv: ', priv.to_string().hex(), end='\n')
        # pub = priv.get_verifying_key().to_string()
        # print('pub: ', pub, end='\n')
        # keccak.update(pub)
        # print('Update keccak: ', keccak.hexdigest(), end='\n')
        # kec = keccak.hexdigest()[24:]
        # print('kec: ', kec, end='\n')
        # ethadd = '0x' + kec
        # privatekey = priv.to_string().hex()
        # print('privatekey: ', privatekey, end='\n')
        # addr = ethadd.lower()
        # print(Fore.WHITE,'Total:', str(z), ' ----- Winner:', str(w), '----- Checking ----- ', str(addr), ' ----- ', str(privatekey), end='\n', flush=True)
        # z += 1
        # if addr in add:
        #     print('Winning', Fore.GREEN, str(w), Fore.WHITE, str(z), Fore.YELLOW, 'Total Scan Checking ----- ETH Address =', Fore.GREEN, str(addr), end='\r')
        #     w += 1
        #     z += 1
        #     f = open("range.txt", "a")
        #     f.write('\nAddress = ' + str(addr))
        #     f.write('\nPrivate Key = ' + str(privatekey))
        #     f.write('\n=========================================================\n')
        #     f.close()
        #     print('Winner information Saved On text file = ADDRESS ', str(addr))
        #     continue
        
seek(r)

if __name__ == '__main__':
    jobs = []
    for r in range(cores):
        p = multiprocessing.Process(target=seek, args=(r,))
        jobs.append(p)
        p.start()
