import argparse

from cryptools import AES
from cryptools import RSA


if __name__ == '__main__':

    parser = argparse.ArgumentParser('main.py')

    parser.add_argument('op',metavar='operation',
                        choices=['encrypt', 'decrypt', 'gen_key', 'sign', 'verify'],
                        help= """
                        {encrypt, decrypt, gen_key, sign, verify}
                        """)

    parser.add_argument('type',metavar='type',
                        choices=['aes', 'rsa'], help="{aes, rsa}")

    parser.add_argument('-k','--key_id', help="identificador da chave", required=True)
    parser.add_argument('-m','--message_file', help='arquivo que contém a mensagem cifrada/decifrada' )

    args = parser.parse_args()


    if args.op == 'gen_key':
        if not args.key_id:
            parser.error("Deve ser especificado um identificador (KEY_ID) para gerar o(s) arquivo(s) da(s) chave(s).")

        if args.type == 'aes':
            f = open(args.key_id+".key", 'w')
            f.write(AES.gen_key())
        if args.type == 'rsa':

            p_key, s_key = RSA.gen_keys()
            n , e = p_key
            _, d = s_key

            f = open(args.key_id+'_public.key', 'w')
            f.write(hex(n) + '\n')
            f.write(hex(e))
            f.close()

            f = open(args.key_id+'_private.key', 'w')
            f.write(hex(n) + '\n')
            f.write(hex(d))
            f.close()

    if args.op == 'encrypt':
        if not args.message_file:
            parser.error("Deve ser especificado o arquivo que contem a mensagem (MESSAGE_FILE).")
        if not args.key_id:
            parser.error("Deve ser especificado o identificador da chave (KEY_ID).")

        if args.type == 'aes':
            with open(args.key_id+".key") as f:
                key = f.read()
                if not key:
                    parser.error("Arquivo de chave vazio.")
                c = AES.encrypt(open(args.message_file, 'rb').read()
                                  ,key)
                print(c.hex(), end="")

        elif args.type == 'rsa':
            content = open(args.message_file, 'rb').read()

            with open(args.key_id+"_public.key") as f:
                public_key =  (int(key, 16) for key in f.readlines()[:2])
                c = RSA.encrypt(content ,public_key)
                print(c.hex(), end="")

        else:
            parser.error("Tipo de criptografia inválido.")

    if args.op == 'decrypt':
        if not args.message_file:
            parser.error("Deve ser especificado o arquivo que contem a mensagem cifrada (MESSAGE_FILE).")
        if not args.key_id:
            parser.error("Deve ser identificador da chave (KEY_ID).")

        if args.type == 'aes':
            with open(args.key_id+".key") as f:
                key = f.read()
                if not key:
                    parser.error("Arquivo de chave vazio.")
                content = bytes.fromhex(open(args.message_file).read())
                print(AES.decrypt(content,key).decode(), end="")

        if args.type == 'rsa':
            with open(args.key_id+"_private.key") as f:
                private_key = (int(key, 16) for key in f.readlines()[:2])
                content = bytes.fromhex((open(args.message_file, 'r').read()))
                print(RSA.decrypt(content ,private_key).decode(), end="")

    if args.op == 'sign' and args.type == 'rsa': 
        content = open(args.message_file, 'rb').read()
        with open(args.key_id+"_private.key") as f:
            private_key = (int(key, 16) for key in f.readlines()[:2])
            signature = RSA.sign(content, private_key)
            open(args.message_file+'.sig', 'wb').write(signature)

    if args.op == 'verify' and args.type == 'rsa': 
        content = open(args.message_file, 'rb').read()
        signature = open(args.message_file+'.sig', 'rb').read()
        with open(args.key_id+"_public.key") as f:
            public_key = (int(key, 16) for key in f.readlines()[:2])
            RSA.verify(content, public_key, signature)




