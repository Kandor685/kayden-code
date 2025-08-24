print("Welcome to the mad libs generator! This project will generate a silly sentence based on your responses to the following questions...")
def generate_mad_libs():
    name = input("What is your name? ")
    adjective = input("Enter an adjective (describing word): ")
    verb = input("Enter a verb: ")
    place = input("Enter a place: ")
    food = input("Enter a food: ")
    vehicle = input("Enter a vehicle: ")
    sentence = name + " is a very " + adjective + " person to be around. They love to " + verb + " in " + place + ". Their favourite food is " + food + " which they eat in a " + vehicle
    print(sentence)
generate_mad_libs()