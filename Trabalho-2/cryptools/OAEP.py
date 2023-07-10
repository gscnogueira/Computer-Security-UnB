import secrets
import hashlib

def mgf1(seed, length, hash_func=hashlib.sha3_256):
    h_len = hash_func().digest_size

    if length > (h_len << 32):
        raise ValueError("Tamanho fornecido para a máscara é muito grande")

    T = b''
    cont = 0
    while len(T) < length:
        b_cont = int.to_bytes(cont, 4, 'big')
        T += hash_func(seed + b_cont).digest()
        cont+=1

    return T[:length]

def encrypt(message, label=b""):
    K = 256 # bytes (p*q = n, com 2048 bits)
    H_LEN = 32 # bytes = 256 bits

    l_hash = hashlib.sha3_256(label).digest()

    ps = bytes.fromhex('00' * (K - len(message) - 2*H_LEN -2))

    db = l_hash + ps + b'\x01' + message

    seed = secrets.token_bytes(H_LEN)

    db_mask = mgf1(seed, K-H_LEN-1)

    masked_db = bytes([m^b for m, b in zip(db_mask, db)])

    seed_mask = mgf1(masked_db, H_LEN)

    masked_seed = bytes([m^b for m, b in zip(seed_mask, seed)])

    return b'\x00' + masked_seed + masked_db

def decrypt(message, label=b""):
    K = 256 # bytes (p*q = n, com 2048 bits)
    H_LEN = 32 # bytes = 256 bits

    l_hash = hashlib.sha3_256(label).digest()

    masked_seed, masked_db = message[1:H_LEN+1], message[H_LEN+1:]

    seed_mask = mgf1(masked_db, H_LEN)

    seed = bytes(m^b for m, b in zip(seed_mask, masked_seed))

    db_mask = mgf1(seed, K - H_LEN - 1)

    db = bytes(m^b for m, b in zip(db_mask, masked_db))

    message_start = db[H_LEN+1:].index(b'\x01') + H_LEN +  1

    return db[message_start+1:]
