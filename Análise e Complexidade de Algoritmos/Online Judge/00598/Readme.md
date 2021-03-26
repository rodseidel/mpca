## Autor
Rodrigo Seidel

## Breve explicação de como a técnica indicada foi utilizada
Após entrada dos dados necessários, de acordo com a opção selecionada ('*', 'n' ou 'a b') são produzidas todas as combinações dos jornais indicados, de maneira ordenada e sem repetição.

A técnica de pesquisa completa foi utilizada na produção de todas as combinações dos jornais indicados, de acordo com a opção selecioanda.


O resultado impresso pelo programa passou no uDebug em diversos casos de teste, porém ao submeter no OnlineJudge apresentou "Runtime error".

Exemplos de sucesso no uDebug são:
>1
>
>\*
>Times
>Herald-Tribune
>Post
>New Advocate
# 
>1
>
>\*
>Jornal 1
>Jornal 2
>Jornal 3
>Jornal 4
# 
>1
>
>2 3
>Times
>Herald-Tribune
>Post
>New Advocate
# 
>2
>
>\*
>Rodrigo
>Seidel
>
>2 3
>Times
>Herald-Tribune
>Post
>New Advocate
# 
>2
>
>2
>Rodrigo
>Seidel
>
>\*
>Jornal 1
>Jornal 2
>Jornal 3

## Análise da complexidade de tempo do programa desenvolvido



## Outras informações que o autor julgar apropriadas para o entendimento do trabalho realizado
Foi utilizada neste trabalho a biblioteca itertools, especificamente o método combinations (https://docs.python.org/3/library/itertools.html#itertools.combinations), através do qual se produz todas as combinações de elementos de uma lista, de maneira ordenada, sem repetição, de acordo com uma quantidade r informada.