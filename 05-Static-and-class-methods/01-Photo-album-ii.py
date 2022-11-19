# 85/100 in judge:
class PhotoAlbum:
    MAX_PHOTOS_PER_PAGE = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for page in range(pages)]
        self.capacity = len(self.photos) * self.MAX_PHOTOS_PER_PAGE

    @staticmethod
    def has_avail_spots(photos, capacity):
        photos_count = sum(len(page) for page in photos)
        return photos_count < capacity

    @staticmethod
    def page_repr(page):
        dash_separator = "-----------"
        return f"{dash_separator}\n{' '.join('[]' for photo in page)}\n"

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = photos_count // 4  # should be math.ceil !
        return cls(pages)

    def add_photo_to_available_spot(self, label):
        for i in range(len(self.photos)):
            page_index = i + 1
            page = self.photos[i]
            if len(page) < self.MAX_PHOTOS_PER_PAGE:
                page.append(label)
                photo_index = page.index(label) + 1
                return f"{label} photo added successfully on page {page_index} slot {photo_index}"

    def add_photo(self, label):
        if not self.has_avail_spots(self.photos, self.capacity):
            return "No more free slots"

        return self.add_photo_to_available_spot(label)

    def display(self):
        return "".join(self.page_repr(page) for page in self.photos) + "-----------\n"


# album = PhotoAlbum(2)
#
# print(album.add_photo("baby"))
# print(album.add_photo("first grade"))
# print(album.add_photo("eight grade"))
# print(album.add_photo("party with friends"))
# print(album.photos)
# print(album.add_photo("prom"))
# print(album.add_photo("wedding"))
#
# print(album.display())

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
