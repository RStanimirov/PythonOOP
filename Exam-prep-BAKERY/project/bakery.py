from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable
from project.table.table import Table


class Bakery:
    def __init__(self, name):
        self.name = name

        self.food_menu = []
        self.drink_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '' or value.isspace():
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type, name, price):
        # if any(x.name == name for x in self.food_menu):
        for x in self.food_menu:
            if x.name == name:
                raise Exception(f"{food_type} {name} is already in the menu!")
        if food_type == "Bread":
            food = Bread(name, price)
            self.food_menu.append(food)
            return f"Added {name} ({food_type}) to the food menu"
        elif food_type == "Cake":
            food = Cake(name, price)
            self.food_menu.append(food)
            return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type, name, portion, brand):
        # if any(x.name == name for x in self.drink_menu):
        for x in self.drink_menu:
            if x.name == name:
                raise Exception(f"{drink_type} {name} is already in the menu!")
        if drink_type == "Tea":
            drink = Tea(name, portion, brand)
            self.drink_menu.append(drink)
            return f"Added {name} ({brand}) to the drink menu"
        elif drink_type == "Water":
            drink = Water(name, portion, brand)
            self.drink_menu.append(drink)
            return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type, table_number, capacity):
        # if any(x.table_number == table_number for x in self.tables_repository):
        for x in self.tables_repository:
            if x.table_number == table_number:
                raise Exception(f"Table {table_number} is already in the bakery!")
        if table_type == "InsideTable":
            table = InsideTable(table_number, capacity)
            self.tables_repository.append(table)
            return f"Added table number {table_number} in the bakery"
        elif table_type == "OutsideTable":
            table = OutsideTable(table_number, capacity)
            self.tables_repository.append(table)
            return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        for x in self.tables_repository:
            if not x.is_reserved and x.capacity >= number_of_people:
                x.reserve(number_of_people)
                return f"Table {x.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def order_food(self, table_number, *food):
        asked_food = list(food)
        matching_food_items = []
        tbl = None
        ordered_food = f"Table {table_number} ordered:\n"
        rejected_food = f"{self.name} does not have in the menu:\n"
        for tbl in self.tables_repository:
            if tbl.table_number == table_number:
                break
            else:
                return f"Could not find table {table_number}"
        for x in asked_food:
            for y in self.food_menu:
                if x == y.name:
                    matching_food_items.append(y)
                    asked_food.remove(x)
        for fd_obj in matching_food_items:
            tbl.order_food(fd_obj)
            ordered_food += repr(fd_obj) + '\n'
        for name in asked_food:
            rejected_food += name + '\n'
        return ordered_food + rejected_food.strip()

    def order_drink(self, table_number, *drinks):
        asked_drinks = list(drinks)
        matching_drink_items = []
        tbl = None
        ordered_drinks = f"Table {table_number} ordered:\n"
        rejected_drinks = f"{self.name} does not have in the menu:\n"
        for tbl in self.tables_repository:
            if tbl.table_number == table_number:
                break
            else:
                return f"Could not find table {table_number}"
        for x in asked_drinks:
            for y in self.drink_menu:
                if x == y.name:
                    matching_drink_items.append(y)
                    asked_drinks.remove(x)
        for dr_obj in matching_drink_items:
            tbl.order_food(dr_obj)
            ordered_drinks += repr(dr_obj) + '\n'
        for name in asked_drinks:
            rejected_drinks += name + '\n'
        return ordered_drinks + rejected_drinks.strip()

    def leave_table(self, table_number):
        current_table = None
        for x in self.tables_repository:
            if x.table_number == table_number:
                current_table = x
        table_bill = current_table.get_bill()
        self.total_income += table_bill
        current_table.clear()

        return f"Table: {table_number}\nBill: {table_bill:.2f}"

    def get_free_tables_info(self):
        result = ''
        for x in self.tables_repository:
            if not x.is_reserved:
                result += x.free_table_info() + '\n'
        return result.strip()

    def get_total_income(self):
        return f'Total income: {self.total_income:.2f}lv'
