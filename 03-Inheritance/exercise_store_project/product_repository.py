from exercise_store_project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for x in self.products:
            if x.name == product_name:
                return x

    def remove(self, product_name):
        for x in self.products:
            if x.name == product_name:
                self.products.remove(x)

    def __repr__(self):
        print_result = ''
        for x in self.products:
            print_result += f"{x.name}: {x.quantity}\n"

        return print_result.strip()

