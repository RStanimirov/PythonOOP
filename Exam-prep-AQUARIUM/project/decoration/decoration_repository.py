from project.decoration.base_decoration import BaseDecoration


class DecorationRepository:
    def __init__(self):
        self.decorations = []

    def add(self, decoration: BaseDecoration):
        self.decorations.append(decoration)

    def remove(self, decoration):
        if decoration not in self.decorations:
            return False
        else:
            self.decorations.remove(decoration)
            return True

    def find_by_type(self, decoration_type):
        for x in self.decorations:
            if x.__class__.__name__ == decoration_type:
                return x
        return "None"


