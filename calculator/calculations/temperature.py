from get_input import temp1, temp2, temp3, temp4, temp5, temp6, temp7

class Temp:
    def __init__(self):
        self.ask = temp1()

    def convert(self):
        if self.ask == '1':
            user = temp2()
            con = temp3()
            if con == '1':
                f = (user * (9 / 5)) + 32
                print(f'{user}c in fahrenheit is {f}F')
            elif con == '2':
                k = (user + 273.15)
                print(f'{user}C in kelvin is {k}K')

        elif self.ask == '2':
            user1 = temp4()
            con1 = temp5()
            if con1 == '1':
                c = (user1 - 32) * (5 / 9)
                print(f'{user1}F in celsius is {c}C')
            elif con1 == '2':
                ke = ((user1 - 32) * (5 / 9)) + 273.15
                print(f'{user1}F in kelvin is {ke}K')

        elif self.ask == '3':
            user2 = temp6()
            con2 = temp7()
            if con2 == '1':
                ce = (user2 - 273.15)
                print(f'{user2}K in celsius is {ce}C')
            elif con2 == '2':
                fe = ((user2 - 273.15) * (9 / 5)) + 32
                print(f'{user2}K in fahrenheit is {fe}F')

