import pymysql


data = pymysql.connect(host='localhost', user='root', passwd='', database='magesh01')
z = data.cursor()
z.execute('use magesh01')
c = input('product:')
z.execute('select product_name from shop')
result = z.fetchall()
l2 = []
for i in result:
    k=list(i)
    l2.append(k[0])
    print(type(i))
for i in l2:
    print(type(i))
if c in l2:
    print('ok')
else:
    print('nill')
print(l2)
m = 7339228061
z.execute('select * from customer where mobile_num = %s', m)
r = z.fetchall()
print(r)