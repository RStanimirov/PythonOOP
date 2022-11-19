import math


class PhotoAlbum:

    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for i in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(math.ceil(photos_count / 4))

    def add_photo(self, label: str):
        for idx, x in enumerate(self.photos):
            if len(x) < 4:
                x.append(label)
                return f'{label} photo added successfully on page {idx + 1} slot {len(x)}'
        return 'No more free slots'

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
