import argparse
import os
from utils import encrypt, decrypt, break_

if __name__ == '__main__':

    parser = argparse.ArgumentParser('vigenere.py')

    parser.add_argument('op',metavar='operation',
                        choices=['encrypt', 'decrypt', 'break'])
    parser.add_argument('-k','--key')
    parser.add_argument('msg', metavar='message') 

    args = parser.parse_args()

    if os.path.exists(args.msg): 
        args.msg = open(args.msg,'r').read().strip()


    if args.op =='encrypt':
        print(encrypt(args.msg, args.key))
    elif args.op == 'decrypt':
        print(decrypt(args.msg, args.key))
    else:
        break_(args.msg)

    

    

