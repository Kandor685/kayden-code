print ("Hello! Welcome to the program!")
def details():
    name = input("What is your name? ")
    print ("Hello,", name, "!")
    age = input("How old are you? ")
    Location = input ("Where do you live? (Roughly) ")
    confirm = input ("So your name is", name, "and you are", age, "years old and you live in", Location, "is that correct?")
    if confirm == "yes" or confirm == "Yes":
        print ("Good to know!")
        quit()
    else:
        print ("I'm sorry! Let's start again!")
        details()
details()
quit()