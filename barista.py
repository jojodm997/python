#print(input("What is your name"))
print("Hello, welcome to Fauzan Coffe")

name = input("What is your name?\n")

if name == "Ben" or name == "Patricia" or name == "Loki":
    evil_status = input("Are you evil?\n")
    good_deeds = int(input("How many good deed have you done today"))
    if evil_status == "Yes" and good_deeds < 4:
        print("Your are no welcome " + name + " Get Out!!")
        exit()
    else:
        print("You one of those good " + name )
else:
    print("Hello " + name + " , Thank you so much for coming in today. \n\n\n")

menu = "Black coffe, Espresso, Latte, Cappucino, Frapuccino"

print(name + ", what would you like from our menu today? Here is what we are serving.\n" + menu)

order = input()

if order == "Frapuccino":
    price = 13
elif order == "Black coffe":
    price = 8
elif order == "Capucinno":
    price = 9
elif order == "Espresso":
    price = 10
elif order == "Latte":
    price = 7
    cream = input("Do you want Whipped cream? ")
    if cream == "Yes":
        price = 11
else:
    print("Sorry, we dont have that here")
    exit()

quantity = input("How many coffees would you like?\n")

total = price * int(quantity)

print("Thank you . Your total is $" + str(total))

print("Sounds good " + name + ", we'll have that your " + quantity + " " + order + " ready for you in a moment. " )