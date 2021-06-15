from get_input import cgpa1, cgpa2


class Cgpa:
    def __init__(self):

        self.ask = cgpa1()
        self.l1 = []

    def a(self):
        print('enter you marks out of 100')
        for i in range(self.ask):
            mark = cgpa2()
            convert = (mark / 10)
            self.l1.append(convert)

    def calc(self):
        if len(self.l1) == self.ask:
            total = sum(self.l1)
            cgpa = total / (len(self.l1))
            print(f'your CGPA is {cgpa} out of 10')
