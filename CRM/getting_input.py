
import pymysql
from datetime import date, timedelta

data = pymysql.connect(host='localhost', user='root', passwd='', database='magesh01')
z = data.cursor()
z.execute('use magesh01')


def name():
    while True:
        try:
            a = input('Enter your name:')
            return a
        except Exception as e:
            print(f'enter the name in correct format,{e}')


def mobile():
    while True:
        try:
            b = int(input('Enter your mobile number:'))
            return b
        except Exception as e:
            print(f'Invalid mobile number,{e}')


def product():
    while True:
        product_name = input('Enter the product:')
        z.execute('select product_name from shop')
        result = z.fetchall()
        l1 = []
        for i in result:
            k = list(i)
            l1.append(k[0])
        if product_name in l1:
            return product_name
        else:
            print('sorry, this product will be available within few days')
            continue


def order_date():
    o_d = date.today()
    return o_d


def delivery_date():
    j = date.today()
    h = int(input('when you want the product to be delivered:'))
    m = j + timedelta(h)
    return m


def customer():
    c = input('1:NEW CUSTOMER OR 2: ENQUIRY')
    return c


def up_to_date():
    u = input('do you wanna change your delivery date[y/n]:')
    return u


def val():
    z.execute('select mobile_num from customer')
    res = z.fetchall()
    l1 = []
    for i in res:
        f = list(i)
        l1.append(f[0])
    return l1


def delay():
    j = date.today()
    v = int(input('how many days you want to delay the delivery from today:'))
    m = j + timedelta(v)
    return m


def username():
    u1 = str(input('enter the username:'))
    return u1


def passwd():
    p = str(input('enter the password:'))
    return p



