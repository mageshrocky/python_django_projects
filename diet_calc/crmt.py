products = ['ice_cream', 'chocolate', 'pen', 'pencil', 'biscuit']
name = input('enter your name:')
cust = input('what do you want:')
c1 = {}
if cust in products:
    print('available')
else:
    print('not available')