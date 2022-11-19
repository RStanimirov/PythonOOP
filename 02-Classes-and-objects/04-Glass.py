class Glass(object):
    capacity = 250

    def __init__(self):
        self.content = 0

    def fill(self, qty):
        if self.content <= qty and Glass.capacity >= self.content + qty:
            self.content += qty
            return f"Glass filled with {qty} ml"
        else:
            return f"Cannot add {qty} ml"

    def empty(self):
        self.content = 0
        return f"Glass is now empty"

    def info(self):
        space_left = Glass.capacity - self.content
        return f"{space_left} ml left"


glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())
