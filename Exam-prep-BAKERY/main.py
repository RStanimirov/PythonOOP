from project.bakery import Bakery
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable
from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water

summer_table = OutsideTable(51, 6)
winter_table = InsideTable(1, 4)
print(summer_table.free_table_info())

crispy_bread = Bread("Crispy bread", 1.80)
sweet_cake = Cake("Sweet cake", 2.20)
green_tea = Tea("Green tea", 220, "Ceylon")
mineral_water = Water("Mineral water", 330, "Gorna bania")
print(repr(crispy_bread))
print(repr(sweet_cake))
print(repr(green_tea))
print(repr(mineral_water))

# summer_table.reserve(6)
# summer_table.order_food(crispy_bread)
# summer_table.order_food(sweet_cake)
# summer_table.order_drink(green_tea)
# summer_table.order_drink(mineral_water)
# print(summer_table.get_bill())

cafeteria = Bakery("Vienna Cafe")
cafeteria.add_food("Bread", "White bread", 1.50)
# print(cafeteria.food_menu)
cafeteria.food_menu.append(crispy_bread)
# print(cafeteria.food_menu)
# # print(cafeteria.add_food("Bread", "Crispy bread", 1.80))
cafeteria.add_food("Bread", "Black bread", 1.70)
print(cafeteria.food_menu)

cafeteria.add_drink("Tea", "Camomile tea", 225, "Fine Herbs")
print(cafeteria.drink_menu)
cafeteria.add_drink("Tea", "Mint tea", 228, "Fine Ferbs")
print(cafeteria.drink_menu)
# cafeteria.add_drink("Tea", "Mint tea", 228, "Herbal")
print(cafeteria.drink_menu)

print(cafeteria.add_table("OutsideTable", 52, 7))
print(cafeteria.add_table("OutsideTable", 53, 5))
print(cafeteria.tables_repository)

print(cafeteria.reserve_table(3))
# print(cafeteria.reserve_table(6))

# for x in cafeteria.tables_repository:
#     print(x.free_table_info())
print("==========Orders============")
print(cafeteria.order_food(52, "White bread", "Camomile tea", "Crispy bread", "Steak", "Beer"))
print("==========GetBill============")
print(cafeteria.leave_table(52))
print("===========FreeTables===========")
print(cafeteria.get_free_tables_info())
print("==========TotalIncome===========")
print(cafeteria.get_total_income())
