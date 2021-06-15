from get_input import choice
from calculations.cgpa import Cgpa
from calculations.age import Age
from calculations.bmi import Bmi
from calculations.temperature import Temp


class Start:
    def __init__(self):
        self.choice = choice()

    def run(self):
        if self.choice == '1':
            print('CGPA CALCULATOR')
            z = Cgpa()
            z.a()
            z.calc()
            print('THANK YOU FOR USING CGPA CALCULATOR')

        elif self.choice == '2':
            print('AGE CALCULATOR')
            d = Age()
            d.dob()
            print('THANK YOU FOR USING AGE CALCULATOR')

        elif self.choice == '3':
            print('welcome to BMI CALCULATOR')
            user = Bmi()
            user.body_mass_index()
            print('THANK YOU FOR USING BMI CALCULATOR')

        elif self.choice == '4':
            print('WELCOME TO TEMPERATURE CONVERTER')
            t = Temp()
            t.convert()
