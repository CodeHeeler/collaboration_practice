import my_functions/add.py
import my_functions/subtract.py
import my_functions/multiply.py
import my_functions/divide.py
import my_functions/remainder.py
import my_functions/exponent.py


def main():
    print("\n\nWelcome to My Math!\n")
    a = input("Enter your first number: ")
    b = input("Enter your second number: ")
    print("\n{} + {} = {}".format(a, b, add(a, b)))
    print("\n{} - {} = {}".format(a, b, subtract(a, b)))
    print("\n{} * {} = {}".format(a, b, multiply(a, b)))
    print("\n{} / {} = {}".format(a, b, divide(a, b)))
    print("\n{} % {} = {}".format(a, b, remainder(a, b)))
    print("\n{} ^ {} = {}".format(a, b, exponent(a, b)))


if __name__ == "__main__":
    main()
