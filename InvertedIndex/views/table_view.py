class TableView:
    def __init__(self, table_controller):
        self.__table_controller = table_controller

    def show_options(self):
        print("")
        print("OPÇÕES")
        print("1 - ADICIONAR DADOS")
        print("2 - DELETAR DADO")
        print("3 - PESQUISA")
        print("4 - MOSTRAR TABELA")
        print("0 - SAIR")
        return input()

    def get_data(self, header):
        data = []
        print("")
        for col in header:
            data.append(input(f"{col.upper()}: ").upper())
        return data
    
    def show_table(self, table):
        i = 1
        print("")
        print("| {:^3}".format("ID") + " | {:^20} | {:^10} | {:^21} | {:^15} |".format(*table.header))
        print("-"*85)
        if table.rows and not len(table.vacant_space) == len(table.rows):
            for data in table.rows:
                if data:
                    print("| {:^3}".format(str(i)) + " | {:^20} | {:^10} | {:^21} | {:^15} |".format(*data))
                    i += 1
                else:
                    print("| {:^3}".format(str(i)) + " | " + "X"*75 + " |")
                    i += 1
        else:
            print("{:^85}".format("TABELA VAZIA!"))
        print("-"*85)

    def get_search_type(self, directories):
        print("")
        print("QUAL FILTRO DESEJA APLICAR?")
        print(f"CLASSES: {', '.join([x for x in directories[0].directory])}")
        print(f"CONSERVAÇÃO: {', '.join([x for x in directories[1].directory])}")
        print(f"PESO MÉDIO: {', '.join([x for x in directories[2].directory])}")
        filter = input("Escolha as opções separadas por espaço: ").upper()
        return filter.split()

    def show_results(self, filtered_set, table):
        print("")
        print("| {:^3}".format("ID") + " | {:^20} | {:^10} | {:^21} | {:^15} |".format(*table.header))
        print("-"*85)
        if filtered_set:
            for row_id in filtered_set:
                data = table.rows[row_id]
                if data:
                    print("| {:^3}".format(str(row_id+1)) + " | {:^20} | {:^10} | {:^21} | {:^15} |".format(*data))
                else:
                    print("| {:^3}".format(str(row_id+1)) + " | " + "X"*75 + " |")
        else:
            print("{:^85}".format("TABELA VAZIA!"))
        print("-"*85)

    def select_data(self):
        return input("SELECIONE O ID: ")
    
    def show_message(self, msg):
        print(msg)