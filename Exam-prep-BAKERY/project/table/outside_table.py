from project.table.table import Table


class OutsideTable(Table):
    MIN_TABLE_NUM = 51
    MAX_TABLE_NUM = 100

    def __init__(self, table_number: int, capacity: int):
        super(OutsideTable, self).__init__(table_number, capacity)

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        if value < self.MIN_TABLE_NUM or value > self.MAX_TABLE_NUM:
            raise ValueError("Outside table's number must be between 51 and 100 inclusive!")
        self.__table_number = value
