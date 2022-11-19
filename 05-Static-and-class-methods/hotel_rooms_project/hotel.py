from hotel_rooms_project.room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    def get_total_guests(self):
        return sum([room.guests for room in self.rooms])

    @classmethod
    def from_stars(cls, start_count):
        return cls(f"{start_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = [x for x in self.rooms if x.number == room_number][0]
        return room.take_room(people)

    def free_room(self, room_number):
        room = [x for x in self.rooms if x.number == room_number][0]
        return room.free_room()

    def status(self):
        free_rooms = [room for room in self.rooms if not room.is_taken]
        taken_rooms = [room for room in self.rooms if room.is_taken]
        result = f"Hotel {self.name} has {self.get_total_guests()} total guests" + "\n"
        result += f"Free rooms: {', '.join(str(room.number) for room in free_rooms)}" + "\n"
        result += f"Taken rooms: {', '.join(str(room.number) for room in taken_rooms)}"
        return result


hotel = Hotel.from_stars(5)

first_room = Room(1, 3)
second_room = Room(2, 2)
third_room = Room(3, 1)

hotel.add_room(first_room)
hotel.add_room(second_room)
hotel.add_room(third_room)

hotel.take_room(1, 4)
hotel.take_room(1, 2)
hotel.take_room(3, 1)
hotel.take_room(3, 1)

print(hotel.status())
