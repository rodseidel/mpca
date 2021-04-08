# Análise e Complexidade de Algoritmos

**Rodrigo Seidel**

**PPComp — Campus Serra, Ifes**

**2021-03**

## Breve explicação de como a técnica indicada foi utilizada

O objetivo do problema é maximizar o valor que cada pessoa pode carregar, considerando o valor e o peso de cada item, e o peso máximo que cada pessoa pode carregar.

Primeiramente defini-se o caso básico da recursão, que é quando o limite do peso da pessoa for zero ou quando a quantidade de itens informada for zero. 

Caso não seja o caso básico:
- verifica-se se o peso do item excede o peso que a pessoa consegue carregar, se isso acontecer, ele vai prosseguir sem incluir aquele item para a pessoa, verificando outro item. 
- caso o item não exceda o peso que a pessoa pode carregar, verifica-se se será considerado o item para a pessoa ou se é mais vantajoso desconsiderar aquele item, neste caso será feita a opção pelo que tiver maior valor entre as duas opções.

A técnica de programação dinâmica foi utilizada inicialmente através da utilização de um cache em matriz que relaciona a quantidade de itens que está se tentando entregar para a pessoa e
capacidade de carga já utilizada da pessoa. Nessa matriz fica armazenavo o valor que pode ser carregado considerando a quantidade de itens (eixo x) e a capacidade de carga já utilizada (eixo y), permitindo desta forma armazenar um resultado de forma a evitar a redundância de cálculos.

Ao submeter no Online Judge desta forma, obtive "Time limit exceeded". Tentei resolver essa questão inserindo um outro cache no qual armazena-se o maior valor que um peso X pode carregar, evitando-se até se chegar a utilizar o cache acima, assim, entendo eu, obtendo melhor performance na execução. 

Mesmo assim, consegui apenas "Time limit exceeded", conforme imagem a seguir (primeiro item da lista). Entretanto, obtive sucesso nos 4 casos de teste no uDebug, apresentado o resultado correto em todos eles.

![Veredito](./10130-veredito.png)


## Análise da complexidade de tempo do programa desenvolvido



## Outras informações que o autor julgar apropriadas para o entendimento do trabalho realizado
