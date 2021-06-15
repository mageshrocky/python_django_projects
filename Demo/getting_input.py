def getting_integer():
    while True:
        try:
            a = int(input('Enter the value:'))
            return a
        except Exception as e:
            print(f'Invalid input:{e}')
