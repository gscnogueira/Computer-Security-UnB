
# Cifra de Vigenère

-   Aluno : Gabriel da Silva Corvino Nogueira
-   Matricula: 180113330
-   Linguagem utilizada : Python 3.10.10


## Cifrador

Para cifrar uma mensagem execute o seguinte comando:

    $ python src/vigenere.py encrypt -k <chave> <mensagem>

As mensagens podem estar tanto em formato textual como em um arquivo:

    $ python src/vigenere.py encrypt -k 'secret' 'hello world'
    zincs pgvnu

    $ echo 'hello world' > file.txt
    $ python src/vigenere.py encrypt -k 'secret' file.txt
    zincs pgvnu


## Decifrador

Para decifrar uma mensagem execute o seguinte comando:

    $ python src/vigenere.py decrypt -k <chave> <mensagem>

As mensagens podem estar tanto em formato textual como em um arquivo:

    $ python src/vigenere.py decrypt -k 'secret' 'zincs pgvnu' 
    hello world

    $ echo 'zincs pgvnu' > file.txt
    $ python src/vigenere.py encrypt -k 'secret' file.txt
    hello world



## Ataque de Recuperação de Senha

Para iniciar o ataque de recuperação de senha execute:

    $ python src/vigenere.py break <mensagem>

Para quebrar o desafio 1, por exemplo, execute:

    $ python src/vigenere.py break desafios/desafio1.txt

