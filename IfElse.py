def age_checker():
    age = int((input("Enter Age: ")))

    if age == int:
        if age < 0:
            print("You're not even born!")
            age_checker()

        elif age <= 12:
             print ("Child")

        elif age > 12 and age < 18:
            print ("Teenager")

        elif age >= 18 and age < 65:
            print ("Adult")

        elif age >= 65 and age < 100:
            print ("Senior")

        elif age >= 123:
            print("You're not really alive")
            age_checker()

        else:
            print("ERROR: Invalid input")
            age_checker()
    else:
        print("ERROR: Input must be an interger")
        age_checker()
age_checker()