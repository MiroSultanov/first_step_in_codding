# To write a program that reads the day of the week (text) - entered by the user and prints on the console the price of a movie ticket according to the day of the week:
   
# Monday Tuesday Wednesday Thursday Friday Saturday Sunday
# 12       12     14          14      12     16      16

day_of_week = input()
if day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Friday':
    print(12)
elif day_of_week == 'Wednesday' or day_of_week == 'Thursday':
    print(14)
elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
    print(16)
