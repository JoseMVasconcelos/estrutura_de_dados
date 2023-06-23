class DataTable:
    def __init__(self, header):
        self.__header = header
        self.__rows = []
        self.__vacant_space = []

    def add_data(self, data):
        if self.__vacant_space:
            self.__rows[self.__vacant_space[0]] = data
            self.__vacant_space.pop()
        else:
            self.__rows.append(data)

    def delete_data(self, row_id):
        self.__rows[row_id] = None
        self.__vacant_space.append(row_id)

    def get_index(self, data):
        return self.__rows.index(data)

    @property
    def header(self):
        return self.__header
    
    @property
    def rows(self):
        return self.__rows
