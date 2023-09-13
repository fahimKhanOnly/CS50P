def userInput():
    name = input("What's your name? ")
    check(name.title())


def check(name):
    match name:
        case "Harry" | "Hermione" | "Ron":
            print("Gryffindor")
        case "Draco":
            print("Slytherin")
        case _:
            print("Who?")


userInput()
