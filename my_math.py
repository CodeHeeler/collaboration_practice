from add import add
from subtract import subtract
from multiply import multiply
from divide import divide
from remainder import remainder
from exponent import exponent


def main():
    print("\n\nWelcome to My Math!\n")
    a = int(input("Enter your first whole number: "))
    b = int(input("Enter your second whole number: "))
    print("\n{} + {} = {}".format(a, b, add(a, b)))
    print("\n{} - {} = {}".format(a, b, subtract(a, b)))
    print("\n{} * {} = {}".format(a, b, multiply(a, b)))
    print("\n{} / {} = {}".format(a, b, divide(a, b)))
    print("\n{} % {} = {}".format(a, b, remainder(a, b)))
    print("\n{} ^ {} = {}".format(a, b, exponent(a, b)))


if __name__ == "__main__":
    main()
