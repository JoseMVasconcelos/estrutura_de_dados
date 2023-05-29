# INE5609 - Estrutura de Dados - Relatório: Lista Duplamente Encadeada (com cursor)

Esse documento é referente ao trabalho 1 de estrutura de dados, no qual foi solicitado a implementação de uma lista duplamente encadeada (com cursor).

### Sumário:

- [Comentários iniciais](#comentários-iniciais)
- [Atributos do nó](#atributos-node)
- [Atributos da lista](#atributos-doublylinkedlist)
- [Métodos do nó](#métodos-node)
- [Métodos da lista](#métodos-doublylinkedlist)


### Comentários Iniciais

O trabalho foi realizado apenas por mim, e a parte mais dificil foi definitivamente a lógica por trás da lista. Depois que consegui ter uma boa imagem mental de como as coisas se encaixavam, o trabalho fluiu razoavelmente bem. 

Acabei descobrindo que o garbage collector do Python age de maneira inusitada, um objeto não é apagado da memória caso exista uma auto-referencia, então para não causar nenhum memory leak tive que ter certeza de antes de apagar um nó, remover toda referencia a outros nós que ele fazia.

No arquivo ***main.py*** tem uma série de testes para demonstrar a lista funcionando. Em comentário está a posição do cursor e a lista completa esperada, logo abaixo, duas funções que **print** que verificam a posição do cursor real e a lista completa real. Quando a lista é printada, é mostrada junto o valor anterior e o próximo valor, para verificar se o encadeamento está correto.

O modelo da lista impressa é:

NÓ ANTERIOR / NÓ ATUAL / PRÓXIMO NÓ

Link do repositório no github: https://github.com/JoseMVasconcelos/estrutura_de_dados/tree/master/ListaDuplamenteEncadeada(ComCursor)
## Atributos

### Atributos Node

- **value**: O valor que o nó representa
- **next_node**: O nó sucessor. Caso o nó atual seja o último da lista, o **next_node** aponta para o primeiro da lista.
- **prev_node**: O nó antecessor. Caso o nó atual seja o primeiro da lista, o **prev_node** aponta para o último da lista.

### Atributos DoublyLinkedList (com cursor)

- **num_elements**: Mostra quantos nós estão na lista, serve principalmente para verificar se a lista está cheia ou vazia.
- **max**: O limite da lista, se o **num_elements** e **max** forem iguais, a lista está cheia e não pode receber mais nenhum nó. 
- **cursor**: O **cursor** se movimenta pela lista e seleciona os nós para resolução das operações
- **first**: Aponta para o primeiro nó da lista. Como a lista é cíclica, é possível descobrir o **último** nó voltando um valor a partir do primeiro (**first**).

## Métodos

### Métodos Node

Métodos básicos para atualização dos nós.
- **getters**: Todos os atributos do nó possuem um **getter**
- **setters**: Tanto o **next_node** e **prev_node** possuem **setters**, o **value** do nó não pode ser alterado depois de instanciado .

### Métodos DoublyLinkedList (com cursor)


#### Métodos de inserção

Todos os métodos de inserção deixam o cursor no nó recém criado.

- **insert_in_prev_cursor**: Baseado na posição do **cursor**, insere um nó atrás do atual.
- **insert_in_next_cursor**: Baseado na posição do **cursor**, insere um nó na frente do atual.
- **insert_as_first**: Insere um nó como o novo primeiro (**first**) da fila. O método não substitui o **first** antigo. Deixa o **cursor** no primeiro nó (**first**).
- **insert_as_last**: Insere um nó no final na lista. O método não substitui o último da lista antigo.
- **insert_in_pos**: Insere um nó na posição requerida. A posição age como um index -> ***0 ... max-1***

Estes métodos verificam se a lista está vazia antes de realizar as operações, caso esteja, as funções redirecionam para a função seguinte:

- **first_insert**: A primeira inserção da lista, age caso **num_elements** esteja 0. Essa função que cria o comportamento cíclico da lista.

#### Métodos de remoção

O garbage collector do python age estranhamente com objetos que fazer auto-referência. Foi necessário implementar um código adicional que garante que o nó apagado não tenha nenhum nó posto em **next_node** e **prev_node**.

Todos os métodos de remoção tentam deixar o cursor no nó a direita do nó removido (**next_node**). Caso o nó removido seja o último, o cursor fica no novo último.

Todos os métodos verificam para ver se um nó está só na lista, caso verdadeiro, a função **last_deletion** é chamada. Isso foi necessário por causa do garbage collector do python.

- **remove_in_cursor**: Baseado na posição do **cursor**, remove o nó selecionado.
- **remove_first**: Remove o nó em primeiro (**first**).
- **remove_last**: Remove o nó em último.
- **remove_node**: Recebe um valor e verifica se um nó com o mesmo se encontra na lista, caso verdadeiro, remove o nó.
- **remove_pos**: Recebe uma posição e remove o nó da mesma. A posição age como um index -> ***0 ... max-1***
- **delete_node**: Função criada para diminuir a repetição de código. Esta que realmente remove o nó selecionado e emenda o **prev_node** com o **next_node**
- **last_deletion**: Função criada para apagar o último elemento da lista.

#### Método de pesquisa

- **search**: Método de pesquisa da lista, é passado um valor a ser procurado. Caso o nó esteja na lista, o cursor o seleciona e a função retorna **True**, caso não esteja, o cursor volta para o primeiro (**first**) e a função retorna **False**.
- **access_cursor**: Retorna o valor do cursor

#### Métodos manipuladores do cursor

- **__goto_first**: Coloca o cursor no primeiro (**first**) da lista.
- **__goto_last**: Coloca o cursor no último da lista.
- **__forwards_n_pos**: Avança n nós da lista..
- **__backwards_n_pos**: Retrocede n nós da lista.


###### José Victor Machado de Vasconcelos - 22100906 - INE5609 