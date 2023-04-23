from node import Node

class DoublyLinkedList():
    def __init__(self, max):
        try:
            self.__first = None
            self.__cursor = None
            self.__num_elements = 0
            if max <= 0:
                raise Exception("Absurd list size!")
            self.__max = max
        except Exception as err:
            print(err)
            exit(1)


    #Ambas "is_max" e "is_empty" retornam valores boleanos baseados
    def is_max(self):
        return True if self.__num_elements == self.__max else False
    
    def is_empty(self):
            return True if self.__num_elements == 0 else False

    def access_cursor(self):
        try:
            if self.__cursor is not None:
                return self.__cursor
            else:
                raise IndexError("Cursor is empty!")
        except IndexError as err:
            print(err)
            exit(1)

    #TODAS AS FUNÇÕES DE INSERÇÃO VERIFICAM SE A LISTA ESTÁ VAZIA PRA INSERIR O PRIMEIRO NÓ
    #TODAS AS FUNCÕES DE INSERÇÃO DEIXAM O CURSOR EM CIMA DO NOVO NÓ
    def insert_in_prev_cursor(self, value):
        if self.__num_elements == 0:
            self.first_insert(value)
        else:
            try:
                if not self.__num_elements == self.__max:
                    node = Node(value)
                    next = self.access_cursor()
                    self.__backwards_n_pos(1)
                    prev = self.access_cursor()
                    prev.next_node = node
                    next.prev_node = node
                    node.next_node = next
                    node.prev_node = prev
                    self.__forwards_n_pos(1)
                    self.__num_elements += 1
                else:
                    raise IndexError("List is full!")
            except IndexError as err:
                print(err)
    
    def insert_in_next_cursor(self, value):
        if self.__num_elements == 0:
            self.first_insert(value)
        else:
            try:
                if not self.__num_elements == self.__max:
                    node = Node(value)
                    prev = self.access_cursor()
                    self.__forwards_n_pos(1)
                    next = self.access_cursor()
                    prev.next_node = node
                    next.prev_node = node
                    node.next_node = next
                    node.prev_node = prev
                    self.__backwards_n_pos(1)
                    self.__num_elements += 1
                else:
                    raise IndexError("List is full!")
            except IndexError as err:
                print(err)

    #Insere um novo nó na ultima posição, deixa o cursor em cima do nó recém criado
    def insert_as_last(self, value):
        if self.__num_elements == 0:
            self.first_insert(value)
        else:
            try:
                if not self.__num_elements == self.__max:
                    node = Node(value)
                    self.__goto_last()
                    prev = self.access_cursor()
                    self.__goto_first()
                    next = self.access_cursor()
                    prev.next_node = node
                    next.prev_node = node
                    node.next_node = next
                    node.prev_node = prev
                    self.__goto_last()
                    self.__num_elements += 1
                else:
                    raise IndexError("List is full!")
            except IndexError as err:
                print(err)

    #Insere um novo nó na primeira posição, deixa o cursor em cima do nó recém criado
    def insert_as_first(self, value):
        if self.__num_elements == 0:
            self.first_insert(value)
        else:
            try:
                if not self.__num_elements == self.__max:
                    node = Node(value)
                    self.__goto_last()
                    prev = self.access_cursor()
                    self.__goto_first()
                    next = self.access_cursor()
                    prev.next_node = node
                    next.prev_node = node
                    node.next_node = next
                    node.prev_node = prev
                    self.__first = node
                    self.__goto_first()
                    self.__num_elements += 1
                else:
                    raise IndexError("List is full!")
            except IndexError as err:
                print(err)

    #A seleção de posição se comporta igual ao indice do python, começando no zero
    def insert_in_pos(self, n, value):
        if self.__num_elements == 0:
            self.first_insert(value)
        else:
            try:
                if not self.__num_elements == self.__max:
                    if n+1 > self.__max:
                        raise IndexError("Number out of bounds!")
                    if n == 0:
                        self.insert_as_first(value)
                    else:
                        if n > self.__num_elements:
                            self.__goto_last()
                        else:
                            self.__goto_first()
                            self.__forwards_n_pos(n-1)
                        node = Node(value)
                        prev = self.access_cursor()
                        self.__forwards_n_pos(1)
                        next = self.access_cursor()
                        prev.next_node = node
                        next.prev_node = node
                        node.next_node = next
                        node.prev_node = prev
                        self.__backwards_n_pos(1)
                        self.__num_elements += 1
                else:
                    raise IndexError("List is full!")
            except IndexError as err:
                print(err)

    #INFELIZMENTE O GARBAGE COLLECTOR DO PYTHON NÃO COLETA OBJETOS QUE POSSUEM REFERENCIA A SI PRÓPRIO
    #É necessário setar o cursor manualmente por causa do garbage collector, bem provável que tenha uma maneira melhor de fazer isso
    def remove_in_cursor(self):
        try:
            if self.__num_elements == 0:
                raise IndexError("List is empty!")
            if self.__num_elements == 1:
                self.last_deletion()
            node = self.access_cursor().next_node
            prev = self.access_cursor().prev_node
            self.access_cursor().prev_node = None
            self.access_cursor().next_node = None
            node.prev_node = prev
            prev.next_node = node
            self.__cursor = node
            self.__num_elements -= 1
        except IndexError as err:
            print(err)

    def remove_first(self):
        try:
            if self.__num_elements == 0:
                raise IndexError("List is empty!")
            if self.__num_elements == 1:
                self.last_deletion()
            self.__goto_first()
            node = self.access_cursor().next_node
            prev = self.access_cursor().prev_node
            self.access_cursor().prev_node = None
            self.access_cursor().next_node = None
            self.__first = node
            node.prev_node = prev
            prev.next_node = node
            self.__goto_first()
            self.__num_elements -= 1
        except IndexError as err:
            print(err)

    def remove_last(self):
        try:
            if self.__num_elements == 0:
                raise IndexError("List is empty!")
            if self.__num_elements == 1:
                self.last_deletion()
            self.__goto_last()
            node = self.access_cursor().next_node
            prev = self.access_cursor().prev_node
            self.access_cursor().prev_node = None
            self.access_cursor().next_node = None
            node.prev_node = prev
            prev.next_node = node
            self.__goto_last()
            self.__num_elements -= 1
        except IndexError as err:
            print(err)

    def remove_node(self, value):
        try:
            if self.__num_elements == 0:
                raise IndexError("List is empty!")
            if self.__num_elements == 1:
                self.last_deletion()
            self.__goto_first()
            while not self.__cursor.value == value:
                self.__forwards_n_pos(1)
                if self.__cursor == self.__first:
                    raise IndexError("Node not found!")
            node = self.access_cursor().next_node
            prev = self.access_cursor().prev_node
            self.access_cursor().prev_node = None
            self.access_cursor().next_node = None
            node.prev_node = prev
            prev.next_node = node
            if self.__cursor == self.__first:
                self.__first = node
            self.__cursor = node
            self.__num_elements -= 1
        except IndexError as err:
            print(err)

    def remove_pos(self, n):
        try:
            if self.__num_elements == 0:
                raise IndexError("List is empty!")
            if self.__num_elements == 1:
                self.last_deletion()
            self.__goto_first()
            if n == 0:
                self.remove_first()
            else:
                if n+1 <= self.__num_elements:
                    self.__forwards_n_pos(n)
                    self.remove_in_cursor()
                else:
                    raise IndexError("Out of bounds!")
        except IndexError as err:
            print(err)
    
    def node_deleter(self):
        pass


    #Função que cuida do primeiro nó a ser criado, o mesmo é posto como primeiro e tem o cursor o selecionando
    #O primeiro nó é posto em um laço consigo mesmo
    def first_insert(self, value):
        node = Node(value)
        node.prev_node = node
        node.next_node = node
        self.__first = node
        self.__cursor = node
        self.__num_elements += 1

    #Função que cuida do último nó a ser deletado, por motivos do garbage collector do python agir estranho, tive que por tudo como None
    def last_deletion(self):
        self.access_cursor().next_node = None
        self.access_cursor().prev_node = None
        self.__first = None
        self.__cursor = None
        self.__num_elements = 0

    def search(self, value):
        self.__goto_first()
        while not self.__cursor.value == value:
            self.__forwards_n_pos(1)
            if self.__cursor == self.__first:
                return False
        return True
        

    #FUNÇÕES PRIVADAS QUE MANIPULAM O CURSOR

    #Coloca o cursor no primeiro nó da lista, se first == None, o cursor também ficará vazio
    def __goto_first(self):
        self.__cursor = self.__first

    #Coloca o cursor no último nó da lista, indo até o primeiro e retornando uma casa, visto que a lista é um laço
    def __goto_last(self):
        self.__cursor = self.__first.prev_node

    #Anda o cursor n casas para frente
    def __forwards_n_pos(self, n):
        for num in range(n):
            self.__cursor = self.__cursor.next_node

    #Anda o cursor n casa para trás
    def __backwards_n_pos(self, n):
        for num in range(n):
            self.__cursor = self.__cursor.prev_node



    #pra testes
    @property
    def num_elements(self):
        return self.__num_elements
