from cgpa_calculator import Cgpa
from age_calculator import Age
from bmi_calculator import Bmi
from temperature_conversion import Temp


def recall():
    choice = input('''please select your calculator
                            1:CGPA CALCULATOR
                            2:AGE CALCULATOR
                            3:BMI CALCULATOR
                            4:TEMPERATURE CONVERTOR
                            5:EXIT:''')

    if choice == '1':
        print('CGPA CALCULATOR')
        z = Cgpa()
        z.a()
        z.calc()
        print('THANK YOU FOR USING CGPA CALCULATOR')
        recall()
    elif choice == '2':
        print('AGE CALCULATOR')
        d = Age()
        d.dob()
        print('THANK YOU FOR USING AGE CALCULATOR')
        recall()

    elif choice == '3':
        print('welcome to BMI CALCULATOR')
        weight = float(input('enter your weight in kg:'))
        h = float(input('enter your height in centimeter:'))
        user = Bmi(weight, h)
        user.body_mass_index()
        print('THANK YOU FOR USING BMI CALCULATOR')
        recall()
    elif choice == '4':
        print('WELCOME TO TEMPERATURE CONVERTER')
        ask = (input('please select your input format| 1:celsius, 2:fahrenheit, 3:kelvin:'))
        t = Temp(ask)
        t.convert()
        print('THANK YOU FOR USING TEMPERATURE CONVERTER')
        recall()
    elif choice == '5':
        pass


recall()
