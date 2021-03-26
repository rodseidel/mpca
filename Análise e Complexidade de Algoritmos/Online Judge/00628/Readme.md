## Autor
Rodrigo Seidel

## Breve explicação de como a técnica indicada foi utilizada
Após entrada dos dados necessários, foi primeiramente realizada o produto das senhas inicialmente inseridas x as regras de formação informadas.
Antes de se realizar o produto, é trocado o caracter 0 das regras por um outro caracter de fora do conjunto permitido para não haver mistura de caracteres 0 da senha com a regra de formação '0'.

O produto destas senhas geradas mantém ainda o '0' das regras, porém os # foram substituídos com a palavra gerada no produto realizado.

Com a lista do produto das senhas em mãos, é aplicada, para cada uma delas a regra de expansão do '0', que gera as sequências de 0 a 9. 

Estas sequencias são geradas fazendo-se o produto de todos dos caracteres 0...9 de acordo com a quantidade de '0' contidos na regra.

Com a lista do produto destes caracteres numérico em mãos, é feita, para cada um deles a substituição dos '0' da lista de palavras acima, produzindo ao final a lista de senhas de acordo com as regras definidas, inclusive a ordem.



## Análise da complexidade de tempo do programa desenvolvido



## Outras informações que o autor julgar apropriadas para o entendimento do trabalho realizado
Foi utilizada neste trabalho a biblioteca itertools, especificamente o método product (https://docs.python.org/3/library/itertools.html#itertools.product), através do qual se faz o produto cartesiano de elementos de uma lista.