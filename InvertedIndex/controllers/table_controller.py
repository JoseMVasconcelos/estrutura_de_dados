from models.data_table import DataTable
from models.inverted_index import InvertedIndex
from views.table_view import TableView

class TableController:
    def __init__(self, header):
        self.__table_view = TableView(self)
        self.__table = DataTable(header)
        self.__directories = [InvertedIndex(), InvertedIndex(), InvertedIndex()]


    def open_view(self):
            switcher = {
                1: self.add_data,
                2: self.delete_data,
                3: self.search,
                4: self.show_data,
                0: self.stop
            }

            while True:
                try:
                    switcher[int(self.__table_view.show_options())]()
                except ValueError:
                    self.__table_view.show_message("OPÇÃO INVÁLIDA")
                except KeyError:
                    self.__table_view.show_message("OPÇÃO INVÁLIDA")

    def add_data(self):
        data = self.__table_view.get_data(self.__table.header)
        if data:
            if data in self.__table.rows:
                self.__table_view.show_message("DADO DUPLICADO!")
            else:
                self.__table.add_data(data)
                self.add_to_dir(data)
        
            
    def get_id(self, row):
        return self.__table.get_index(row)

    def delete_data(self):
        self.show_data()
        try:
            if self.__table.rows:
                row_id = int(self.__table_view.select_data())-1
                if self.__table.rows[row_id]:
                    self.__table.delete_data(row_id)
                    self.del_from_dir(row_id)
                else:
                    raise IndexError
            else:
                raise IndexError
        except IndexError("Dado não encontrado!") as err:
            self.__table_view.show_message(err)

    def search(self):
        if self.__directories[0].directory:
            filters = self.__table_view.get_search_type(self.__directories)
            filtered_set = self.search_filter(filters)
            self.__table_view.show_results(filtered_set, self.__table)
        else:
            self.__table_view.show_message("NÃO EXISTEM FILTROS!")

    def search_filter(self, filters):
        filtered_set = set()
        first_flag = True
        for filter in filters:
            for i in range(len(self.__directories)):
                filtering_set = self.__directories[i].directory.get(filter)
                if filtering_set is not None:
                    if not filtered_set and first_flag == True:
                        filtered_set = filtering_set
                    else:
                        filtered_set = filtered_set.intersection(filtering_set)
            first_flag = False
        return filtered_set

    def show_data(self):
        self.__table_view.show_table(self.__table)

    def add_to_dir(self, data):
        row_id = self.get_id(data)
        for i in range(len(self.__directories)):
            self.__directories[i].add_ref(data[i+1], row_id)

    def del_from_dir(self, row_id):
        for i in range(len(self.__directories)):
            self.__directories[i].del_ref(row_id)

    def stop(self):
        exit(0)

    def add_data_dev(self, data):
        self.__table.add_data(data)
        self.add_to_dir(data)