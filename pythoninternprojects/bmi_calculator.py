class Bmi:
    def __init__(self, weight, h):
        self.weight = weight
        self.h = h

    def body_mass_index(self):
        height = self.h / 100
        bmi = self.weight / (height * height)
        if bmi <= 18.5:
            print(f'your BMI is {bmi}, which means you are underweight ')
        elif 18.5 < bmi < 25:
            print(f'your BMI is {bmi}, which means you are normal ')
        elif 25 < bmi < 30:
            print(f'your BMI is {bmi}, which means you are overweight ')
        elif bmi > 30:
            print(f'your BMI is {bmi}, which means you are obese ')



