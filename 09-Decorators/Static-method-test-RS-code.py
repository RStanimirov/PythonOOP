class Holiday:
    def __init__(self, holiday_name, gifts):
        self.holiday_name = holiday_name
        self.gifts = gifts
        self.kisses = True

    @staticmethod
    def date(date):
        return f"Today is {date}."

    def greeting(self):
        return f"Happy {self.holiday_name}!"

    def present_gifts(self):
        return f"Accept theses {self.gifts}!"

    def __str__(self):
        return f"This celebration is {self.holiday_name} and gentlemen are expected\n" \
               f"to endow the ladies with lots of {', '.join(self.gifts)}."


while True:
    try:
        holiday_date = input()
        # is_holiday = False

        if holiday_date == "8 March":
            # is_holiday = True
            march_celebration = Holiday("Women's Day", ["tulips", "snowdrops", "carnations"])
            print(Holiday.date(holiday_date))
            print(march_celebration.greeting())
            print(march_celebration)
            break

        elif holiday_date == "14 February":
            # is_holiday = True
            valentines_day = Holiday("St. Valentine's Day", ["roses", "chocolates", "wine"])
            print(Holiday.date(holiday_date))
            print(valentines_day.greeting())
            print(valentines_day)
            break

        elif holiday_date == "24 April":
            # is_holiday = True
            easter_celebration = Holiday("Easter", ["candies", "fruit", "eggs"])
            print(Holiday.date(holiday_date))
            print(easter_celebration.greeting())
            print(easter_celebration)
            break

    except:
        print("There is no holiday on this date. Please enter a valid holiday:")
        continue

