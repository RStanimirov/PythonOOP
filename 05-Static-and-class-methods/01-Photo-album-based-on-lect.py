import math


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = self.init_photos(self.pages)

    # helper method to create matrix (self.photos):
    def init_photos(self, pages):
        matrix = []
        for i in range(pages):
            matrix.append([])
        return matrix

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(math.ceil(photos_count / PhotoAlbum.PHOTOS_PER_PAGE))

    def add_photo(self, label: str):
        page_counter = 0
        for x in self.photos:
            page_counter += 1
            if len(x) < PhotoAlbum.PHOTOS_PER_PAGE:
                x.append(label)
                return f"{label} photo added successfully on page {page_counter} slot {len(x)}"
        return "No more free slots"

    def display(self):
        separator = '-' * 11
        result = separator + "\n"
        for x in self.photos:
            result += ' '.join('[]' for y in x) + "\n"
            result += separator + "\n"
        return result.strip()


my_album = PhotoAlbum.from_photos_count(6)
print(my_album.add_photo("my first photo"))
print(my_album.add_photo("my second photo"))
print(my_album.add_photo("my third photo"))
print(my_album.add_photo("my fourth photo"))
print(my_album.add_photo("my fifth photo"))
print(my_album.add_photo("my sixth photo"))
print(my_album.add_photo("my seventh photo"))
print(my_album.add_photo("my eighth photo"))
print(my_album.add_photo("my ninth photo"))
print(my_album.add_photo("my tenth photo"))
print(my_album.add_photo("my eleventh photo"))
print(my_album.add_photo("my twelfth photo"))
print(my_album.add_photo("my thirteenth photo"))
print(my_album.photos)
print(my_album.display())

# album = PhotoAlbum(2)
# print(album.add_photo("baby"))
# print(album.add_photo("first grade"))
# print(album.add_photo("eight grade"))
# print(album.add_photo("party with friends"))
# print(album.photos)
# print(album.add_photo("prom"))
# print(album.add_photo("wedding"))
# print(album.display())
