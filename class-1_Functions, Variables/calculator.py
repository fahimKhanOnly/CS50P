"""
x = float(input("What's x? "))
y = float(input("What's y? "))
z = round(x / y, 2)
print(f"{z}")


solved same problem using different way
z = x / y
print(f"{z:.2f}")
"""





"""
# function
def main():
    name = input("What's your name? ")
    greet(name)


def greet(to):
    if to.strip() == "":
        to = "World!"
        print(f"Hello {to}")
    else:
        print(f"Hello {to.strip()}.")


main()
"""





"""
# return value
def calculate():
    x = int(input("What's x? "))
    print("x squared is", square(x))



def square(n):
    # solved same problem using multiple ways
    # return n * n
    # return n ** 2
    # return pow(n, 2)


calculate()
"""
