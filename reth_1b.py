from hdwallet import HDWallet
from hdwallet.symbols import ETH as SYMBOL
from hexer import mHash
from colorama import Fore, Style
import multiprocessing
from multiprocessing import Pool
import secrets
from ecdsa import SigningKey, SECP256k1
import sha3

# =========================================================================================
mmdrza = '''




-----------------------------------------------------------------------------------------------------------------




'''
# ============================================================================================

r = 1
cores = 8



def seek(r):
    filename = "list.txt"
    with open(filename) as f:
        add = f.read().split()
    add = set(add)
    print('\n', Fore.WHITE, str(mmdrza), Style.RESET_ALL, '\n')
    z = 1
    w = 0
    count = 0
    hex64 = secrets.token_hex(32)
    while True:

        count += 1
        if count % 100000000 == 0:
            hex64 = secrets.token_hex(32)
            count = 0

        hex64_int = int(hex64, 16)
        hex64_int += 1
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

        # PRIVATE_KEY: str = hex64
        # hdwallet: HDWallet = HDWallet(symbol=SYMBOL)
        # hdwallet.from_private_key(private_key=PRIVATE_KEY)
        # priv = hdwallet.private_key()
        # addr = (hdwallet.p2pkh_address()).lower()
        print(Fore.WHITE,'Total:',Fore.WHITE, str(z),Fore.WHITE,'Winner:',Fore.WHITE, str(w), Fore.WHITE, '-Checking-', Fore.WHITE, str(addr), Fore.WHITE, str(privatekey), end='\n', flush=True)
        z += 1
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
