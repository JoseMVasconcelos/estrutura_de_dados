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
            data.append(input(f"{col.upper()}: ".upper()))
        return data
    
    def show_table(self, table):
        i = 1
        print("")
        print("ID  |  " + "  |  ".join(table.header))
        for data in table.rows:
            if data:
                print(str(i) + "  |  "+  "  |  ".join(data))
                i += 1
            else:
                print(str(i) + "  |  Empty")
                i += 1

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
        print("ID  |  " + "  |  ".join(table.header))
        if filtered_set:
            for row_id in filtered_set:
                data = table.rows[row_id]
                if data:
                    print(str(row_id+1) + "  |  "+  "  |  ".join(data))
                else:
                    print(str(row_id+1) + "  |  Empty")
        else:
            print("TABELA VAZIA!")

    def select_data(self):
        return input("SELECIONE O ID: ")
    
    def show_message(self, msg):
        print(msg)