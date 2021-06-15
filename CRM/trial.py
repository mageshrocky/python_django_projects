from datetime import date, timedelta
import pymysql
import re
#d = date.today()

#data = pymysql.connect(host='localhost', user='root', passwd='', database='magesh01')
#z = data.cursor()
#z.execute('use magesh01')


#class New:
    #def __init__(self, c_name, mob_no, product, order_date, delivery_date):
        #self.name = c_name
        #self.mob_no = mob_no
        #self.product = product
        #self.order_date = order_date
        #self.delivery_date = delivery_date

    #def place_order(self):
        #print('name:', self.name)
        #print('mob_no:', self.mob_no)
        #print('product:', self.product)
        #print('order_date:', self.order_date)
        #print('delivery_date:', self.delivery_date)
        #f = z.execute('insert into customer(customer_name, mobile_num, product_ordered, order_date, delivery_date) values(%s,%s,%s,%s,%s)', (self.name, self.mob_no, self.product, self.order_date, self.delivery_date))
        #data.commit()
        #print(f)

#e = input('1:new user or 2:existing user:')
#if e == '1':
    #c_name = input('enter your name:')
    #mob_no = int(input('enter your mobile number:'))
    #order_date = d
    #product = input('enter the product:')
    #order_date = date.today()
    #delivery_date = input('delivery_date')
    #c = New(c_name, mob_no, product, order_date, delivery_date)
    #c.place_order()
#elif e == '2':
    #f=New()
    #f.place_order()

def mobile():
    while True:
        try:
            b = int(input('Enter your mobile number:'))
            if re.match(r'[6789]{1}\d{9}', b):
                print(b)
        except Exception as e:
            print(f'Invalid mobile number,{e}')
mobile()