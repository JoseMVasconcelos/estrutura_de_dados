from doubly_linked_list import DoublyLinkedList

class Main():
    lista = DoublyLinkedList(7)
    lista.insert_in_next_cursor(25)
    
    lista.insert_as_first(30)
    lista.insert_as_first(40)
    #lista -> 40 30 25

    lista._DoublyLinkedList__forwards_n_pos(1)
    lista.insert_in_next_cursor(10)
    lista.insert_in_prev_cursor(5)
    #lista -> 40 30 5 10 25
    lista.insert_in_pos(3, 15)
    #lista -> 40 30 5 15 10 25

    lista.remove_first()
    #lista -> 30 5 15 10 25

    lista.remove_last()  
    #lista -> 30 5 15 10

    lista.remove_pos(0)
    print(lista.access_cursor().value)
    #lista -> 5 15 10
    lista.remove_pos(1)
    print(lista.access_cursor().value)
    #lista -> 5 10

    print("VERIFICACAO NA ORDEM ESQUERDA/DIREITA")
    lista._DoublyLinkedList__goto_first()
    for num in range(lista.num_elements):
        print(lista.access_cursor().prev_node.value, lista.access_cursor().value, lista.access_cursor().next_node.value)
        lista._DoublyLinkedList__forwards_n_pos(1)
    print("")

    print("VERIFICACAO NA ORDEM DIREITA/ESQUERDA")
    lista._DoublyLinkedList__goto_last()
    for num in range(lista.num_elements):
        print(lista.access_cursor().prev_node.value, lista.access_cursor().value, lista.access_cursor().next_node.value)
        lista._DoublyLinkedList__backwards_n_pos(1)
    print("SE ALGO DER DIFERENTE TU FEZ MERDA")
