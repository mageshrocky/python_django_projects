from getting_input import getting_integer


class BasicCalc:
    def __init__(self):
        self.a = getting_integer()

    def som_calc(self):
        result = 0

        while self.a != 0:
            temp = self.a % 10
            result += temp
            self.a //= 10
        return result
