#  Gerador/Verificador de Assinaturas

## Uso 

```
usage: main.py [-h] -k KEY_ID [-m MESSAGE_FILE] operation type

positional arguments:
  operation             {encrypt, decrypt, gen_key}
  type                  {aes, rsa}

options:
  -h, --help            show this help message and exit
  -k KEY_ID, --key_id KEY_ID
                        identificador da chave
  -m MESSAGE_FILE, --message_file MESSAGE_FILE
                        arquivo que contém a mensagem cifrada/decifrada
```

## Casos de Uso

### Cifração AES

#### Geração da chave

Primeiramente, deve ser gerada uma chave aleatória. Para isso, deve ser fornecido um identificador para a chave.

```
python main.py gen_key aes -k chave_aes
```

No exemplo acima, o identificador da chave é `chave_aes`. Dessa forma, a chave ficara armazenada no arquivo `chave_aes.key`


#### Cifração

Para que o arquivo `msg.txt` seja cifrado com a chave gerada, deve ser fornecido o seguinte comando

```
 python main.py encrypt aes -k chave_aes -m msg.txt 
```

Para armazenar o resultado em um arquivo, basta redirecionar a saída com o operador `>`

```
 python main.py encrypt aes -k chave_aes -m msg.txt > c_msg.txt
```

#### Decifração

Para decifrar um arquivo `c_msg.txt` basta executar o seguinte comando

```
python main.py decrypt aes -k chave_aes -m c_msg.txt
```




