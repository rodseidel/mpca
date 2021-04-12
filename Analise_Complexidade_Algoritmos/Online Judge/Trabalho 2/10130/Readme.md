# Análise e Complexidade de Algoritmos

**Rodrigo Seidel**

**PPComp — Campus Serra, Ifes**

**2021-03**

## Breve explicação de como a técnica indicada foi utilizada

O objetivo do problema é maximizar o valor que cada pessoa pode carregar, considerando o valor e o peso de cada item, e o peso máximo que cada pessoa pode carregar.

Primeiramente define-se o caso básico da recursão, que é quando o limite do peso da pessoa for zero ou quando a quantidade de itens informada for zero. 

Caso não seja o caso básico:
- verifica-se se o peso do item excede o peso que a pessoa consegue carregar, se isso acontecer, ele vai prosseguir sem incluir aquele item para a pessoa, verificando outro item. 
- caso o item não exceda o peso que a pessoa pode carregar, verifica-se se será considerado o item para a pessoa ou se é mais vantajoso desconsiderar aquele item, neste caso será feita a opção pelo que tiver maior valor entre as duas opções.

A técnica de programação dinâmica foi utilizada inicialmente através da utilização de um cache (variável cache) em matriz que relaciona a quantidade de itens que está se tentando entregar para a pessoa e capacidade de carga já utilizada da pessoa. Nessa matriz fica armazenado o valor que pode ser carregado considerando a quantidade de itens (colunas) e a capacidade de carga já utilizada (linhas), permitindo desta forma armazenar um resultado evitando a redundância de cálculos (sobreposição de subproblemas).

Ao submeter no Online Judge desta forma, obtive "Time limit exceeded". Tentei resolver essa questão inserindo um outro cache (variável cachePessoa) no qual armazena-se o maior valor que um peso X pode carregar, evitando-se, desta forma, utilizar o cache acima, assim, entendo eu, obtendo melhor performance na execução. Infelizmente consegui novamente "Time limit exceeded".

Ainda tentando o "Accepted", modifiquei a forma de utilização do primeiro cache que citei, alterando sua reinicialização, que anteriormente estava por pessoa, para a cada caso de teste. A matriz cache passou a ser inicializada considerando o maior peso da lista de pesos informada no caso de testes. Considerando que em cada caso de teste os itens permanecem os mesmos o que muda é o peso máximo das pessoas, esse cache pode ser reaproveitado, evitando mais cálculos redundantes.

Nesse último caso consegui apenas "Runtime error", conforme imagem a seguir (primeiro item da lista), entretanto, obtive sucesso nos 4 casos de teste no uDebug ao executar o código localmente (em todas as formas de cache indicadas acima), apresentado o resultado correto em todos eles.

![Veredito](./10130-veredito.png)


## Análise da complexidade de tempo do programa desenvolvido

Número casos de teste: T
- Inicializa cache: num_itens * maior_peso_pessoas
- sort itens lista: O(n log n)
- Número de pessoas: P
- Recursão para identificar melhor valor pessoa: num_itens*peso_da_pessoa (percorre-se todas as capacidades de peso da pessoa de 1 até o peso total).

Foram desconsiderados custos irrelevantes, como atribuição de váriáveis, append em dict, lista, etc, pois têm custo 1 (https://wiki.python.org/moin/TimeComplexity).

<div class="math">
\begin{equation}
T(n) =
  \begin{cases}
    1 & \text{se}~n = 1 \\
    T*((num_itens*maior_peso_pessoas) + (P*(num_itens*peso_da_pessoa))) & \text{caso contrário}
  \end{cases}
\end{equation}
</div>

Avaliando o retorno no Wolfram Alpha, entendi que a complexidade do algoritmo ficou em O(n).


## Outras informações que o autor julgar apropriadas para o entendimento do trabalho realizado
