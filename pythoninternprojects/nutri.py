class A:
    def c(self):
        curd_rice = {'calories': 130,
                     'fat': 3.48,
                     'carbs': 18.07,
                     'protein': 5.73,
                     'fibre': 0.8}
    def v(self):
        veg_biriyani = {'calories': 241,
                        'fat': 17.9,
                        'carbs': 13.9,
                        'protein': 4.8,
                        'fibre': 3.3}
    def Cb(self):
        chicken_biriyani = {'calories': 241,
                            'fat': 17.9,
                            'carbs': 13.9,
                            'protein': 4.8,
                            'fibre': 3.3}
    def s(self):
        sambar_rice = {'calories': 139,
                       'fat': 5.4,
                       'carbs': 18.4,
                       'protein': 5.2,
                       'fibre': 2.8}
    def fri(self):
        fried_rice = {'calories': 130,
                      'fat': 3.48,
                      'carbs': 18.07,
                      'protein': 5.73,
                      'fibre': 0.8}

class X:

    def choice(self):
        food = input('''choose your food: 
                       1:curd_rice
                       2:veg_biriyani
                       3:chicken_biriyani
                       4:sambar_rice
                       5:fried_rice''')

        if food == '1':
            A.c()
        elif food == '2':
            A.v()
        elif food == '3':
            A.Cb()
        elif food == '4':
            A.s()
        elif food == '5':
            A.fri()



def calc():
    self.p =
    c = .values()
    d = fried_rice.keys()
    l1 = []
    l2 = []
    for i, j in zip(c, d):
        z = i * q
        l1.append(j)
        l2.append(z)
        result = {l1[i]: l2[i] for i in range(len(l1))}
        print(result)

