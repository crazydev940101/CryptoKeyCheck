from hdwallet import HDWallet
from hdwallet.symbols import ETH as SYMBOL
from hexer import mHash
from colorama import Fore, Style
import multiprocessing
from multiprocessing import Pool

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
    while True:
        hex64 = mHash()
        PRIVATE_KEY: str = hex64
        hdwallet: HDWallet = HDWallet(symbol=SYMBOL)
        hdwallet.from_private_key(private_key=PRIVATE_KEY)
        priv = hdwallet.private_key()
        addr = (hdwallet.p2pkh_address()).lower()
        print(Fore.WHITE,'Total Scan:',Fore.WHITE, str(z),Fore.WHITE,'Winner Wallet:',Fore.WHITE, str(w), Fore.WHITE, 'Checking Now ----- ETH Address', Fore.WHITE, str(addr), end='\r', flush=True)
        z += 1
        if addr in add:
            print('Winning', Fore.GREEN, str(w), Fore.WHITE, str(z), Fore.YELLOW, 'Total Scan Checking ----- ETH Address =', Fore.GREEN, str(addr), end='\r')
            w += 1
            z += 1
            f = open("Success.txt", "a")
            f.write('\nAddress = ' + str(addr))
            f.write('\nPrivate Key = ' + str(priv))
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
