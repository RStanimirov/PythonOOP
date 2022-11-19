class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.end:
            current_iteration = self.start
            self.start += 1
            return current_iteration
        raise StopIteration()


# class custom_range:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#         self.counter = self.start - 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.counter += 1
#         if self.counter == self.end + 1:
#             raise StopIteration()
#         return self.counter


one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)