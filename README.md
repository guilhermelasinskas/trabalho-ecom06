### Autores:
Guilherme Henriques Lasinskas

Gustavo Luiz de A Guerra

João Otávio da Silva Barros

## Trabalho de ECOM06

Este programa é um compilador para a linguagem desenvolvida na disciplina ECOM06.

Foi proposto pelos alunos o desenvolvimento de uma linguagem natural para a manipulação de um sistema de arquivos.
Este programa compila a linguagem criada, reconhecendo as instruções e os tipos da linguagem.
Para fins de demonstração, só foram utilizados arquivos com extensão `.txt`.

## Tipos

Os tipos reconhecido pela linguagem são:
- Arquivo
- Caminho
- Pasta

Pastas são caminhos do sistema. Os seus nomes devem satisfazer o RegEx `[a-zA-Z][_]/([a-zA-Z][_]/)*`.
O motivo pelo qual as pastas devem terminar com `/` é para difereciá-las dos Caminhos.

Arquivos são o tipo mais simples da liguagem. São reprensentados pelo RegEx `[a-zA-Z][_]`.
Durante a implementação deste compilador foi necessário considerar as extensões dos arquivos.
Portanto, podem ser utilizadas extensões adicionando um ponto (`.`) ao final de um arquivo.
Contudo, a extensão deve satisfazer o RegEx `[a-zA-Z][_]`.

Caminhos são caminhos do sistema, mas não terminam com o caractere `/`.
São diferentes das Pastas pois terminam em um arquivo.
O RegEx que representa Caminhos é `[a-zA-Z][_]/([a-zA-Z][_]/)*`.
Contudo, como Caminhos podem terminar em arquivo, a validação de extensão também deve ser considerada.

## Compilação

Existem três arquivos com programas de exemplo na pasta **Example Programs**. O nome do arquivo que será compilado e executado deve ser alterado no arquivo `Util/constants.py`.
A compilação da linguagem é feita utilizando os analisadores aprendidos na disciplina.

- O analisador léxico lê a entrada e faz o tratamento necessário.
    - As regras conhecidas pelo analisador léxico correspondem ao formato de entrada esperado pelo analisador sintático.

- O analisador sintático faz uma série de verificações, a depender do comando recebido.
    - Comandos diferentes podem requisitar argumentos de tipos diferentes.

- As entidades utilizadas têm suas formas validadas separadamente.
    - O analisador sintático faz uso extensivo dessas validações, visto que é necessário verificar a compatibilidade entre o comando e o tipo do argumento passado.

Uma vez que o comando tenha sido validado pelo compilador, a ação necessária ligada ao comando é armazenada numa fila.
Depois que o programa foi completamente compilado, as ações são realizadas por ordem de entrada na fila (FIFO).

## Execução

As instruções interpretadas são executadas por ordem de entrada na fila (FIFO).
A implementação de cada uma das instruções foi realizada utilizando os *modules* `os` e `shutil`.
`os` possibilita maneiras simples de realizar operações do sistema operacional.
`shutil` oferece diversas operações em arquivos e coleções de arquivo - em particular, cópia e remoção.

[`shutil`](https://docs.python.org/3/library/shutil.html)

[`os`](https://docs.python.org/3/library/os.html#module-os)
