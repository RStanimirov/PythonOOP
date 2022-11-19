# RS solution:
def number_increment(numbers):

    def increase():
        incremented_nums_list =[]
        for x in numbers:
            incremented_num = x + 1
            incremented_nums_list.append(incremented_num)
        return incremented_nums_list

    return increase()


print(number_increment([1, 2, 3]))