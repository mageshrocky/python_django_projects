def input1():
    print('''choose your food: 
                        1:curd_rice
                        2:veg_biriyani
                        3:chicken_biriyani
                        4:sambar_rice
                        5:fried_rice''')
    while True:

        try:
            a = int(input('enter the food:'))
            return a
        except Exception as e:
            print(f'Invalid input:{e}')


def input2():

    while True:
        try:
            print('each bowl consist of 100g of food')
            b = int(input('how much bowl do you consume:'))
            return b
        except Exception as e:
            print(f'Invalid input:{e}')

