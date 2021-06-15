import datetime
from datetime import date


def c_date():
    cd = datetime.datetime.strftime(datetime.datetime.today(), '%Y=%m-%d-%H')
    print(cd)


c_date()