from getting_input import input1
from diet.food import X


class Y:
    def __init__(self):
        self.c = input1()

    def choice(self):
        f = X()

        if self.c == 1:
            f.curd_rice()
        elif self.c == 2:
            f.veg_biriyani()
        elif self.c == 3:
            f.chicken_biriyani()
        elif self.c == 4:
            f.sambar_rice()
        elif self.c == 5:
            f.fried_rice()
