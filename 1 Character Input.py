import datetime
now = datetime.datetime.now()
now_year = (now.year)

#Ask user to enter their name.
name = input("Please can you tell me your name. ")

#Ask user to enter their age

age = int(input("How old are you? "))
#Address a mesage to them telling them the years they'll turn 100

years_to_100 = (100 - age)

date = str((now.year + years_to_100))

print("{} you will turn 100 years old in {}.".format(name, date))


#EXTRA ask user for a number then print out that many copies of above message

repeat = int(input("{} how many times would you like to be told this? ".format(name)))

print(repeat * ("{} you will turn 100 years old in {}\n".format(name,date)))
      
#SUCCESS
