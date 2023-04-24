from doubly_linked_list import DoublyLinkedList


class Main():

    '''
    Em baixo alguns testes simples, para facilitar os testes para verificar se tudo está ok, usei força bruta para rodar funções como "__goto_first".
    Depois de cada mudança na lista, está em comentário o valor esperado seguido de um print para ver o que realmente aconteceu.
    A lista é mostrada da seguinte forma: NÓ_ANTERIOR, NÓ_ATUAL, NÓ_PRÓXIMO para poder verificar o encadeamento
    '''

    lista = DoublyLinkedList(10)
    lista.insert_in_next_cursor(25)
    #cursor -> 25
    print("Cursor:", lista.access_cursor().value)
    #lista -> 25
    print("VERIFICACAO NA ORDEM ESQUERDA/DIREITA")
    lista._DoublyLinkedList__goto_first()
    for num in range(lista.num_elements):
        print(lista.access_cursor().prev_node.value,
              lista.access_cursor().value, lista.access_cursor().next_node.value)
        lista._DoublyLinkedList__forwards_n_pos(1)
    print("")

    lista.insert_as_first(30)
    #cursor -> 30
    print("Cursor:", lista.access_cursor().value)
    #lista -> 30 25
    print("VERIFICACAO NA ORDEM ESQUERDA/DIREITA")
    lista._DoublyLinkedList__goto_first()
    for num in range(lista.num_elements):
        print(lista.access_cursor().prev_node.value,
              lista.access_cursor().value, lista.access_cursor().next_node.value)
        lista._DoublyLinkedList__forwards_n_pos(1)
    print("")

    lista.insert_as_first(40)
    #cursor -> 40
    print("Cursor:", lista.access_cursor().value)
    #lista -> 40 30 25
    print("VERIFICACAO NA ORDEM ESQUERDA/DIREITA")
    lista._DoublyLinkedList__goto_first()
    for num in range(lista.num_elements):
        print(lista.access_cursor().prev_node.value,
              lista.access_cursor().value, lista.access_cursor().next_node.value)
        lista._DoublyLinkedList__forwards_n_pos(1)
    print("")

    lista._DoublyLinkedList__goto_first()
    lista._DoublyLinkedList__forwards_n_pos(1)
    lista.insert_in_next_cursor(10)
    lista.insert_in_prev_cursor(5)
    #cursor -> 5
    print("Cursor:", lista.access_cursor().value)
    #lista -> 40 30 5 10 25
    print("VERIFICACAO NA ORDEM ESQUERDA/DIREITA")
    lista._DoublyLinkedList__goto_first()
    for num in range(lista.num_elements):
        print(lista.access_cursor().prev_node.value,
              lista.access_cursor().value, lista.access_cursor().next_node.value)
        lista._DoublyLinkedList__forwards_n_pos(1)
    print("")

    lista.insert_in_pos(3, 15)
    #cursor -> 15
    print("Cursor:", lista.access_cursor().value)
    #lista -> 40 30 5 15 10 25
    print("VERIFICACAO NA ORDEM ESQUERDA/DIREITA")
    lista._DoublyLinkedList__goto_first()
    for num in range(lista.num_elements):
        print(lista.access_cursor().prev_node.value,
              lista.access_cursor().value, lista.access_cursor().next_node.value)
        lista._DoublyLinkedList__forwards_n_pos(1)
    print("")

    lista._DoublyLinkedList__goto_first()
    lista.insert_in_prev_cursor(90)
    #cursor -> 90
    print("Cursor:", lista.access_cursor().value)
    #lista -> 90 40 30 5 15 10 25
    print("VERIFICACAO NA ORDEM ESQUERDA/DIREITA")
    lista._DoublyLinkedList__goto_first()
    for num in range(lista.num_elements):
        print(lista.access_cursor().prev_node.value,
              lista.access_cursor().value, lista.access_cursor().next_node.value)
        lista._DoublyLinkedList__forwards_n_pos(1)
    print("")

    lista.remove_first()
    #cursor -> 40
    print("Cursor:", lista.access_cursor().value)
    #lista -> 40 30 5 15 10 25
    print("VERIFICACAO NA ORDEM ESQUERDA/DIREITA")
    lista._DoublyLinkedList__goto_first()
    for num in range(lista.num_elements):
        print(lista.access_cursor().prev_node.value,
              lista.access_cursor().value, lista.access_cursor().next_node.value)
        lista._DoublyLinkedList__forwards_n_pos(1)
    print("")

    lista.remove_last()
    #cursor -> 10
    print("Cursor:", lista.access_cursor().value)
    #lista -> 40 30 5 15 10
    print("VERIFICACAO NA ORDEM ESQUERDA/DIREITA")
    lista._DoublyLinkedList__goto_first()
    for num in range(lista.num_elements):
        print(lista.access_cursor().prev_node.value,
              lista.access_cursor().value, lista.access_cursor().next_node.value)
        lista._DoublyLinkedList__forwards_n_pos(1)
    print("")

    lista.remove_node(40)
    #cursor -> 30
    print("Cursor:", lista.access_cursor().value)
    #lista -> 30 5 15 10
    print("VERIFICACAO NA ORDEM ESQUERDA/DIREITA")
    lista._DoublyLinkedList__goto_first()
    for num in range(lista.num_elements):
        print(lista.access_cursor().prev_node.value,
              lista.access_cursor().value, lista.access_cursor().next_node.value)
        lista._DoublyLinkedList__forwards_n_pos(1)
    print("")

    lista.remove_pos(2)
    #cursor -> 10
    print("Cursor:", lista.access_cursor().value)
    #lista -> 30 5 10
    print("VERIFICACAO NA ORDEM ESQUERDA/DIREITA")
    lista._DoublyLinkedList__goto_first()
    for num in range(lista.num_elements):
        print(lista.access_cursor().prev_node.value,
              lista.access_cursor().value, lista.access_cursor().next_node.value)
        lista._DoublyLinkedList__forwards_n_pos(1)
    print("")   

    #resultado -> TRUE
    print(lista.search(5))
    #cursor -> 5
    print("Cursor:", lista.access_cursor().value)
    print("")

    #resultado -> FALSE
    print(lista.search(3))
    #cursor -> 30
    print("Cursor:", lista.access_cursor().value)    