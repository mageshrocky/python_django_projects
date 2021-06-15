def cgpa1():
    while True:
        try:
            c = int(input('how many subjects you want to calculate CGPA:'))
            return c
        except ValueError:
            print('Invalid number')


def cgpa2():
    while True:
        try:
            m = int(input(f'enter your mark in subject:'))
            return m
        except ValueError:
            print('enter your mark in numbers only')


def dob1():
    print('Date Of Birth format must be in DD-MM-YYY')
    u = input("enter your Date Of Birth:")
    return u


def bmi1():
    while True:
        try:
            weight = float(input('enter your weight in kg:'))
            return weight
        except ValueError:
            print('enter your weight in numbers')


def bmi2():
    while True:
        try:
            h = float(input('enter your height in centimeter:'))
            return h
        except ValueError:
            print('enter your height in numbers(cm)')


def temp1():
    ask = (input('please select your input format| 1:celsius, 2:fahrenheit, 3:kelvin:'))
    return ask


def temp2():
    user = float(input('enter the value in celsius:'))
    return user


def temp3():
    con = input('convert into 1:fahrenheit, 2:kelvin:')
    return con


def temp4():
    u1 = float(input('enter your value in fahrenheit:'))
    return u1


def temp5():
    c1 = input('convert into 1:celsius, 2:kelvin:')
    return c1


def temp6():
    u2 = float(input('enter your temperature in kelvin'))
    return u2


def temp7():
    c2 = input('convert into 1:celsius, 2:fahrenheit:')
    return c2


def choice():
    c = input('''please select your calculator
                                1:CGPA CALCULATOR
                                2:AGE CALCULATOR
                                3:BMI CALCULATOR
                                4:TEMPERATURE CONVERTOR:''')

    return c

