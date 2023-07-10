#  Gerador/Verificador de Assinaturas

```
usage: main.py [-h] -k KEY_ID [-m MESSAGE_FILE] operation type

positional arguments:
  operation             {encrypt, decrypt, gen_key, sign, verify}
  type                  {aes, rsa}

options:
  -h, --help            show this help message and exit
  -k KEY_ID, --key_id KEY_ID
                        identificador da chave
  -m MESSAGE_FILE, --message_file MESSAGE_FILE
                        arquivo que contém a mensagem cifrada/decifrada
```


## Cifração/Decifração AES

### Geração da chave

Primeiramente, deve ser gerada uma chave aleatória. Para isso, deve ser fornecido um identificador para a chave.

```
python main.py gen_key aes -k chave_aes
```

No exemplo acima, o identificador da chave é `chave_aes`. Dessa forma, a chave ficara armazenada no arquivo `chave_aes.key`


### Cifração

Para que o arquivo `msg.txt` seja cifrado com a chave gerada, deve ser fornecido o seguinte comando

```
 python main.py encrypt aes -k chave_aes -m msg.txt 
```

Para armazenar o resultado em um arquivo, basta redirecionar a saída com o operador `>`

```
 python main.py encrypt aes -k chave_aes -m msg.txt > c_msg.txt
```

### Decifração

Para decifrar um arquivo `c_msg.txt`, basta executar o seguinte comando

```
python main.py decrypt aes -k chave_aes -m c_msg.txt
```


## Cifração/Decifração RSA

### Geração de chaves

Nesta etapa, deve ser fornecido um identificador único. Tal identificador estará associado com suas chaves pública e privada

```
python main.py gen_key rsa -k chave_rsa
```

No exemplo acima, o identificador da chave é `chave_rsa`. Dessa forma, as chaves publica e privada serão armazenada nos arquivos `chave_rsa_public.key` e `chave_rsa_private.key`, respectivamente.

### Cifração

Supondo que queremos cifrar o arquivo que `chave_aes.key`, que contém a chave gerada anteriormente pelo algoritmo AES. Podemos executar o seguinte comando.

```
python main.py encrypt rsa -k chave_rsa -m chave_aes.key
```

Para armazenar o resultado em um arquivo, basta redirecionar a saída com o operador `>`

```
 python main.py encrypt rsa -k chave_rsa -m chave_aes.key > chave_cifrada.txt
 ```


*IMPORTANTE*: No parâmetro `-k`,deve ser fornecido o identificador da chave RSA (no caso `chave_rsa`) e não o arquivo que contém a chave pública.

### Decifração

Para decifrar o arquivo `chave_cifrada.txt`, que contém a chave AES, basta executar o seguinte comando

```
 python main.py decrypt rsa -k chave_rsa -m chave_cifrada.txt
```


### Geração de Assinatura RSA

Para gerar uma assinatura do arquivo `msg.txt` fornecido o identificador de suas chaves por meio do seguinte comando

```
 python main.py sign rsa -k chave_rsa -m msg.txt
```

Esse comando gerará um arquivo que contém a assinatura. O nome desse arquivo será igual o nome da mensagem concatenado com `.sig`. Por exemplo, a assinatura do arquivo `msg.txt` será `msg.txt.sig`

### Verificação de Assinatura RSA

Para que seja verificada a assinatura do arquivo `msg.txt`, basta executar o seguinte comando:

```
python main.py verify rsa -k chave_rsa -m msg.txt
```


