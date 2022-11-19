import math


class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        matrix = []
        for i in range(self.pages):
            matrix.append([])
        self.photos = matrix

    @classmethod
    def from_photos_count(cls, photos_count):
        PhotoAlbum.pages = math.ceil(photos_count / 4)
        return cls(PhotoAlbum.pages)

    def add_photo(self, label):
        page_counter = 0
        for x in self.photos:
            page_counter += 1
            if len(x) < 4:
                x.append(label)
                return f"{label} photo added successfully on page {page_counter} slot {len(x)}"
        return "No more free slots"

    def display(self):
        separator = '-' * 11 + '\n'
        result = separator
        for x in self.photos:
            line = ('[] ' * len(x)).rstrip(' ') + '\n'
            result += line + separator
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

# my_album = PhotoAlbum.from_photos_count(7)
# print(my_album.add_photo("my first photo"))
# print(my_album.add_photo("my second photo"))
# print(my_album.add_photo("my third photo"))
# print(my_album.add_photo("my fourth photo"))
# print(my_album.add_photo("my fifth photo"))
# print(my_album.add_photo("my sixth photo"))
# print(my_album.add_photo("my seventh photo"))
# # print(my_album.add_photo("my eighth photo"))
# # print(my_album.add_photo("my ninth photo"))
# # print(my_album.add_photo("my tenth photo"))
# # print(my_album.add_photo("my eleventh photo"))
# # print(my_album.add_photo("my twelfth photo"))
# # print(my_album.add_photo("my thirteenth photo"))
# # print(my_album.photos)
# print(my_album.display())