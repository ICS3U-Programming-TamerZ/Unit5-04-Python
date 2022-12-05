#!/usr/bin/env python3

# Created By: Tamer Zreg
# Date: Nov. 30, 2022
# This program calculates the number with a given
# operation.


def calculator(first_num, second_num, sign):
    if sign == "+":
        result = first_num + second_num
    elif sign == "-":
        result = first_num - second_num
    elif sign == "/":
        result = first_num / second_num
    elif sign == "*":
        result = first_num * second_num
    elif sign == "%":
        result = first_num % second_num
    return result


def main():

    first_num = input("What is your first number: ")
    second_num = input("What is your second number: ")
    sign = input("What operation would you like to do: ")

    try:
        first_num = float(first_num)
        second_num = float(second_num)
    except ValueError:
        print("Please enter a valid number")
        main()
    if sign == "+" or sign == "/" or sign == "-" or sign == "%" or sign == "*":
        calculator(first_num, second_num, sign)
        result = calculator(first_num, second_num, sign)
        print(f"{first_num} {sign} {second_num} = {result}")

    elif sign != "+" or sign != "/" or sign != "-" or sign != "%" or sign != "*":
        print("You must enter a Valid operation")
        main()


if __name__ == "__main__":
    main()
