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


# Casos de uso:

Dada a mensagem M contida no arquivo msg.txt, são apresentados os seguintes casos de uso

1. Cifração de uma mensagem com AES: M, k -> AES_k(M)

Geração de chave
    ```
    python main.py gen_key aes -k chave_aes
    ```

Cifração
```
 python main.py encrypt aes -k chave_aes -m msg.txt > cmsg.txt

```



2. Cifra híbrida:
Enviando mensagem M para usuário A, (KA_p, KA_s) = chaves assimétricas de A
C = (AES_k(M) , RSA_KA_p(k))
3. Cifra híbrida (autenticação mútua):
Usuário B enviando mensagem M para usuário A, (KA_p, KA_s) = chaves assimétricas
de A; (KB_p, KB_s) = chves assimétricas de B
C = (AES_k(M) , RSA_KB_s (RSA_KA_p(k)), KB_p)
4. Geração de Assinatura de A
Usuário B enviando mensagem M para usuário A, (KA_p, KA_s) = chaves assimétricas
de A; H(.)=função de hash
Sign = (AES_k(M) , RSA_KA_s(H(AES_k(M))), KA_p)
5. Verificação da assinatura
RSA_KA_s (RSA_KA_s(H(AES_k(M)))) = H(AES_k(M)) ? 
