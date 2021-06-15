class Temp:
    def __init__(self, ask):
        self.ask = ask

    def convert(self):
        if self.ask == '1':
            user = float(input('enter your value in celsius:'))
            con = input('convert into 1:fahrenheit, 2:kelvin:')
            if con == '1':
                f = (user * (9 / 5)) + 32
                print(f'{user}c in fahrenheit is {f}F )')
            elif con == '2':
                k = (user + 273.15)
                print(f'{user}C in kelvin is {k}K')

        elif self.ask == '2':
            user1 = float(input('enter your value in fahrenheit:'))
            con1 = input('convert into 1:celsius, 2:kelvin:')
            if con1 == '1':
                c = (user1 - 32) * (5 / 9)
                print(f'{user1}F in celsius is {c}C')
            elif con1 == '2':
                ke = ((user1 - 32) * (5 / 9)) + 273.15
                print(f'{user1}F in kelvin is {ke}K')

        elif self.ask == '3':
            user2 = float(input('enter your temperature in kelvin'))
            con2 = input('convert into 1:celsius, 2:fahrenheit:')
            if con2 == '1':
                ce = (user2 - 273.15)
                print(f'{user2}K in celsius is {ce}C')
            elif con2 == '2':
                fe = ((user2 - 273.15) * (9 / 5)) + 32
                print(f'{user2}K in fahrenheit is {fe}F')

