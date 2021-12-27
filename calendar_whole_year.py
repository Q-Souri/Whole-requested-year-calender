import calendar

#To display calendar of whole requested year

year = int(input("Please enter the year: "))

my_cal = calendar.calendar(year) 

print(my_cal)
