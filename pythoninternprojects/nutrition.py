def c():
    curd_rice = {'calories': 130,
                 'fat': 3.48,
                 'carbs': 18.07,
                 'protein': 5.73,
                 'fibre': 0.8}
    c = curd_rice.values()
    d = curd_rice.keys()
    l1 = []
    l2 = []
    for i, j in zip(c, d):
        z = i * q
        l1.append(j)
        l2.append(z)
    result = {l1[i]: l2[i] for i in range(len(l1))}
    r = {f'{q} bowl of curd_rice consist of': result}
    print(r)


def v():
    veg_biriyani = {'calories': 241,
                    'fat': 17.9,
                    'carbs': 13.9,
                    'protein': 4.8,
                    'fibre': 3.3}
    c = veg_biriyani.values()
    d = veg_biriyani.keys()
    l1 = []
    l2 = []
    for i, j in zip(c, d):
        z = i * q
        l1.append(j)
        l2.append(z)
    result = {l1[i]: l2[i] for i in range(len(l1))}
    r = {f'{q} bowl of veg_biriyani consist of': result}
    print(r)


def Cb():
    chicken_biriyani = {'calories': 139,
                        'fat': 3.9,
                        'carbs': 19.23,
                        'protein': 6.36,
                        'fibre': 2.2}
    c = chicken_biriyani.values()
    d = chicken_biriyani.keys()
    l1 = []
    l2 = []
    for i, j in zip(c, d):
        z = i * q
        l1.append(j)
        l2.append(z)
    result = {l1[i]: l2[i] for i in range(len(l1))}
    r = {f'{q} bowl of chicken_biriyani consist of': result}
    print(r)


def s():
    sambar_rice = {'calories': 139,
                   'fat': 5.4,
                   'carbs': 18.4,
                   'protein': 5.2,
                   'fibre': 2.8}
    c = sambar_rice.values()
    d = sambar_rice.keys()
    l1 = []
    l2 = []
    for i, j in zip(c, d):
        z = i * q
        l1.append(j)
        l2.append(z)
    result = {l1[i]: l2[i] for i in range(len(l1))}
    r = {f'{q} bowl of sambar_rice consist of': result}
    print(r)


def fri():
    fried_rice = {'calories': 130,
                  'fat': 3.48,
                  'carbs': 18.07,
                  'protein': 5.73,
                  'fibre': 0.8}
    c = fried_rice.values()
    d = fried_rice.keys()
    l1 = []
    l2 = []
    for i, j in zip(c, d):
        z = i * q
        l1.append(j)
        l2.append(z)
    result = {l1[i]: l2[i] for i in range(len(l1))}
    r = {f'{q} bowl of fried_rice consist of': result}
    print(r)


def choice():
    if food == '1':
        c()
    elif food == '2':
        v()
    elif food == '3':
        Cb()
    elif food == '4':
        s()
    elif food == '5':
        fri()


food = input('''choose your food: 
               1:curd_rice
               2:veg_biriyani
               3:chicken_biriyani
               4:sambar_rice
               5:fried_rice:''')
print('each bowl consist of 100g of food')
q = float(input('how many bowl:'))
choice()
