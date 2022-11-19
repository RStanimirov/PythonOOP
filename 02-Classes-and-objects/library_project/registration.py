from library_project.library import Library
from library_project.user import User


class Registration:
    def __init__(self):
        pass

    def add_user(self, user: User, library: Library):
        if user not in library.user_records:
            library.user_records.append(user)
        else:
            return f"User with id = {user.user_id} already registered in the library!"

    def remove_user(self, user: User, library: Library):
        if user in library.user_records:
            library.user_records.remove(user)
            if user.username in library.rented_books:
                del library.rented_books[user.username]
        else:
            return "We could not find such user to remove!"

    def change_username(self, user_id: int, new_username: str, library: Library):
        for x in library.user_records:
            if x.user_id == user_id:
                if x.username != new_username:
                    old_username = x.username
                    x.username = new_username
                    if old_username in library.rented_books.keys():
                        library.rented_books[new_username] = library.rented_books[old_username]
                        del library.rented_books[old_username]
                    return f"Username successfully changed to: {new_username} for user id: {user_id}"

                else:
                    return "Please check again the provided username - it should be different than the username used so far!"
            else:
                return f"There is no user with id = {user_id}!"
