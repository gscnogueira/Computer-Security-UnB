import string
import re
from collections import Counter
from itertools import cycle


CHARACTERS = string.ascii_lowercase

CHARACTER_CODES = {c:n for n,c in enumerate(CHARACTERS)}

FREQS_PT = {'a':	14.63, 
            'b':	1.04, 
            'c':	3.88, 
            'd':	4.99, 
            'e':	12.57, 
            'f':	1.02, 
            'g':	1.30, 
            'h':	1.28, 
            'i':	6.18, 
            'j':	0.40, 
            'k':	0.02, 
            'l':	2.78, 
            'm':	4.74, 
            'n':	5.05, 
            'o':	10.73, 
            'p':	2.52, 
            'q':	1.20, 
            'r':	6.53, 
            's':	7.81, 
            't':	4.34, 
            'u':	4.63, 
            'v':	1.67, 
            'w':	0.01, 
            'x':	0.21, 
            'y':	0.01, 
            'z':	0.47
            }


FREQS_EN = {'a' :	8.167,
            'b' :	1.492,
            'c' :	2.782,
            'd' :	4.253,
            'e' :	12.702,
            'f' :	2.228,
            'g' :	2.015,
            'h' :	6.094,
            'i' :	6.966,
            'j' :	0.153,
            'k' :	0.772,
            'l' :	4.025,
            'm' :	2.406,
            'n' :	6.749,
            'o' :	7.507,
            'p' :	1.929,
            'q' :	0.095,
            'r' :	5.987,
            's' :	6.327,
            't' :	9.056,
            'u' :	2.758,
            'v' :	0.978,
            'w' :	2.360,
            'x' :	0.150,
            'y' :	1.974,
            'z' :	0.074
            }

def encode(c): return CHARACTER_CODES[c]

def decode(n): return CHARACTERS[n]

def expand_key(msg, key):
    times, rest = divmod(len(msg), len(key))
    return key*times + key[:rest]

def encrypt_char(m, k):
    return (decode((encode(m) + encode(k))%len(CHARACTERS))
            if m in CHARACTER_CODES else m)

def encrypt(msg, key):
    print(CHARACTER_CODES)
    key_it = cycle(key)
    return ''.join([encrypt_char(m,next(key_it)) if m in CHARACTER_CODES else m for m in msg])

def decrypt_char(m, k):
    return (decode((encode(m) - encode(k))%len(CHARACTERS))
            if m in CHARACTER_CODES else m)

def decrypt(msg, key):
    key_it = cycle(key)
    return ''.join([decrypt_char(m,next(key_it)) if m in CHARACTER_CODES else m for m in msg])

def preproc(msg) : return re.sub('[^a-z]',"", msg)

def get_divs(n) :
    divs = set()
    for i in range(1,n):
        if i*i>n: break 
        if n%i == 0 : divs |={i, n//i}

    return divs

def find_key_length(msg, n_options=10 ):
    pos = {}
    lens = Counter()
    for i in range(len(msg)):
        s = msg[i:i+3]
        if s in pos:
            lens.update(get_divs(i-pos[s]))
        pos[msg[i:i+3]]= i

    del lens[1]

    key_lens = lens.most_common(n_options)

    return key_lens

def get_groups(msg, key_len):
    return [msg[i::key_len] for i in range(key_len)]

def get_freqs(group):
    counter = Counter({c:0 for c in CHARACTERS})
    counter.update(group)
    return [v*100/counter.total() for v in counter.values()]

def break_char(group, language):
    real_freqs = list(FREQS_PT.values() if language=='PT' else FREQS_EN.values())
    txt_freqs = get_freqs(group)
    rank = []
    for c in CHARACTERS:
        rank.append(((sum(abs(a-b) for a, b in zip(real_freqs, txt_freqs))), c))
        txt_freqs.append(txt_freqs.pop(0))
    return [c for _,c in sorted(rank)]


def query_key_len(msg):
    print(f'Possible key lengths found:\n')
    print('RANK\tLEN\tMARKS')
    for i, (k, v) in enumerate(find_key_length(msg), 1):
        print(f'{i}\t{k}\t{v}')

    return int(input('\nInsert a key length (from LEN column): '))

def find_key(msg,key_len):
    print('\nENGLISH:')
    for group in get_groups(msg, key_len): print( break_char(group, 'EN'))
    print('PORTUGUESE:')
    for group in get_groups(msg, key_len): print( break_char(group, 'PT'))

def try_again():
    return input('\nWould you like to try another length?[y/n]') != 'n'
def break_(msg):
    while True:
        msg = preproc(msg)
        key_len = query_key_len(msg)
        find_key(msg,key_len)
        if not try_again() : break

    


if __name__ == '__main__':
    with open('desafio1.txt', 'r') as f:
        break_(f.read())


