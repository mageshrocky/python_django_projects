from getting_input import input1, input2


class X:
    def __init__(self):
        self.b = input2()

    def curd_rice(self):
        curd = {'calories': 130,
                'fat': 3.48,
                'carbs': 18.07,
                'protein': 5.73,
                'fibre': 0.8}

        c = curd.values()
        d = curd.keys()
        l1 = []
        l2 = []
        for i, j in zip(c, d):
            z = i * self.b
            l1.append(j)
            l2.append(z)
        result = {l1[i]: l2[i] for i in range(len(l1))}
        r = {f'{self.b} bowl of curd_rice consist of': result}
        print(r)

    def veg_biriyani(self):

        veg = {'calories': 241,
               'fat': 17.9,
               'carbs': 13.9,
               'protein': 4.8,
               'fibre': 3.3}
        c = veg.values()
        d = veg.keys()
        l1 = []
        l2 = []
        for i, j in zip(c, d):
            z = i * self.b
            l1.append(j)
            l2.append(z)
        result = {l1[i]: l2[i] for i in range(len(l1))}
        r = {f'{self.b} bowl of veg_biriyani consist of': result}
        print(r)

    def chicken_biriyani(self):
        chick = {'calories': 241,
                 'fat': 17.9,
                 'carbs': 13.9,
                 'protein': 4.8,
                 'fibre': 3.3}
        c = chick.values()
        d = chick.keys()
        l1 = []
        l2 = []
        for i, j in zip(c, d):
            z = i * self.b
            l1.append(j)
            l2.append(z)
        result = {l1[i]: l2[i] for i in range(len(l1))}
        r = {f'{self.b} bowl of chicken_rice consist of': result}
        print(r)

    def sambar_rice(self):
        sambar = {'calories': 139,
                  'fat': 5.4,
                  'carbs': 18.4,
                  'protein': 5.2,
                  'fibre': 2.8}
        c = sambar.values()
        d = sambar.keys()
        l1 = []
        l2 = []
        for i, j in zip(c, d):
            z = i * self.b
            l1.append(j)
            l2.append(z)
        result = {l1[i]: l2[i] for i in range(len(l1))}
        r = {f'{self.b} bowl of sambar_rice consist of': result}
        print(r)

    def fried_rice(self):
        fried = {'calories': 130,
                 'fat': 3.48,
                 'carbs': 18.07,
                 'protein': 5.73,
                 'fibre': 0.8}
        c = fried.values()
        d = fried.keys()
        l1 = []
        l2 = []
        for i, j in zip(c, d):
            z = i * self.b
            l1.append(j)
            l2.append(z)
        result = {l1[i]: l2[i] for i in range(len(l1))}
        r = {f'{self.b} bowl of fried_rice consist of': result}
        print(r)

# f.curd_rice()
# f.veg_biriyani()
# f.chicken_biriyani()
# f.sambar_rice()
# f.fried_rice()
