name = input("please enter your name: ")
age = int(input("How old are you ,{0}? ".format(name)))
print(age)

if age < 18:
    print("Sorry !")
    print("Please come back in {0} years".format(18 - age))
elif age == 900:
    print("Sorry, Yoda, you die in return of the Jedi")
else:
    print("You eligible for vote")
    print("please put an x in the box")
