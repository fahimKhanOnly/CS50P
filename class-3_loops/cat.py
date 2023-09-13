# while loop
i = 3
while i != 0:
    print("Meow.")
    i -= 1





print("\t\"for\"")
# for loop
def main():
    n = int(input("What's is n? "))
    get_number(n)


def get_number(n):
    for _ in range(n):
        print("meow")


main()




print("\t\"List of dictionary\"")
# List of dictionary
students = [
    {"name": "Hermone", "house": "Gryffindor", "patronus": "Other"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Slytherin", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=" : ")






print("\t\"nested loop\"")
# nested loop
def main():
    print_square(3)


def print_square(size):
    for i in range(size):
        print("#")


main()
