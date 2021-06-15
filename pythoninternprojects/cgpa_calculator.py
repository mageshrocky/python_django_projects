class Cgpa:
    def a(self):
        self.l1 = []
        self.ask = int(input('how many subjects you want to calculate CGPA:'))
        print('enter you marks out of 100')
        for i in range(1, self.ask + 1):
            while True:
                mark = input(f'enter your mark in subject{i}:')
                try:
                    val = int(mark)
                    convert = (val / 10)
                    self.l1.append(convert)
                    break
                except ValueError:
                    print('enter your mark in numbers only')

    def calc(self):
        if len(self.l1) == self.ask:
            total = sum(self.l1)
            cgpa = total / (len(self.l1))
            print(f'your CGPA is {cgpa} out of 10')


