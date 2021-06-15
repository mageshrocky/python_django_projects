from getting_input import name, mobile, product, order_date, delivery_date, up_to_date, delay, val
import pymysql

data = pymysql.connect(host='localhost', user='root', passwd='', database='magesh01')
z = data.cursor()
z.execute('use magesh01')


class New:
    def __init__(self):
        self.name = name()
        self.mobile = mobile()
        self.product = product()
        self.order = order_date()
        self.delivery = delivery_date()

    def place_order(self):
        z.execute(
            'insert into customer(customer_name, mobile_num, product_ordered, order_date, delivery_date) values(%s,'
            ' %s,%s,%s,%s)',
            (self.name, self.mobile, self.product, self.order, self.delivery))
        data.commit()


class Old:
    def __init__(self):
        self.m = mobile()

    def validation(self):
        l = val()
        s = str(self.m)
        if s in l:
            z.execute('select * from customer where mobile_num=%s', self.m)
            details = z.fetchall()
            print(details)
            self.u = up_to_date()
            if self.u == 'y':
                new_date = delay()
                z.execute('update customer set delivery_date=%s where mobile_num=%s', (new_date, self.m))
                data.commit()
                print(new_date)

            elif self.u == 'n':
                print('thank you for visiting our shop')
                pass
        else:
            print('no data found')

