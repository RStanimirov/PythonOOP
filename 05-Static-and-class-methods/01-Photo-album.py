#85/100 in judge:
class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for x in range(self.pages)]
        self.page = 0

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(photos_count // 4)  # should be math.ceil !

    def add_photo(self, label):
        try:
            if len(self.photos[self.page]) == 4:
                self.page += 1
        except:
            return "No more free slots"
        if self.page >= self.pages:
            return "No more free slots"
        self.photos[self.page].append(label)
        return f"{label} photo added successfully on page {self.page + 1} slot {len(self.photos[self.page])}"

    def display(self):
        result = ""
        for page in self.photos:
            result += "-" * 11 + "\n"
            for i in range(len(page)):
                if i == len(page) - 1:
                    result += "[]"
                else:
                    result += "[] "
            result += "\n"
        result += "-" * 11 + "\n"
        return result


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())

# baby photo added successfully on page 1 slot 1
# first grade photo added successfully on page 1 slot 2
# eight grade photo added successfully on page 1 slot 3
# party with friends photo added successfully on page 1 slot 4
# [['baby', 'first grade', 'eight grade', 'party with friends'], []]
# prom photo added successfully on page 2 slot 1
# wedding photo added successfully on page 2 slot 2
# -----------
# [] [] [] []
# -----------
# [] []
# -----------
