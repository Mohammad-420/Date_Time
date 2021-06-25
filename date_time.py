from my_date import MyDate
from my_time import MyTime

class Date_Time(MyDate, MyTime):
    def __init__(self, year, month, day, hour, minute, second):
        MyDate.__init__(self, year, month, day)
        MyTime.__init__(self, hour, minute, second)

    def __str__(self):
        return f'{MyDate.__str__(self)}    {MyTime.__str__(self)}'

    def __repr__(self):
        return f'{MyDate.__repr__(self)}     {MyTime.__repr__(self)}'

    def __next__(self):
        MyTime.__next__(self)
        if self.isMidnight():
            MyDate.__next__(self)
        return self
        

if __name__ == "__main__":
    from datetime import datetime
    from time import sleep
    now = datetime.now()
    dt = Date_Time(now.year, now.month, now.day, now.hour, now.minute, now.second)
    while True:
        print(repr(next(dt)))
        # print(next(dt))
        sleep(1)
# else:
#     print('Welcome to date_time madule')