import datetime
from datetime import date


class Age:

    def dob(self):
        while True:
            print('Date Of Birth format must be in DD-MM-YYY')
            user = input("enter your Date Of Birth:")
            date_string = user
            date_format = '%d-%m-%Y'
            try:
                db = datetime.datetime.strptime(date_string, date_format)
                x = date.today()
                age = x.year - db.year - ((x.month, x.day) < (db.month, db.day))
                print(f'your age is {age}')
                break
            except ValueError:
                print('enter valid date of birth,the format should be in DD-MM-YYYY')


