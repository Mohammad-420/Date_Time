class MyDate:
    def __init__(self, year, month, day, monthType='lunar' ):

        self.months = [31 for _ in range(6)]  # 6 mah aval sal 31 roz
        self.months.extend(30 for _ in range(5))  # 5 mah bad 30 roz
        self.months.append(29)  # akharin mah sal 29 roz
        # solar month
        if monthType == 'solar':
            self.monthNames = ('فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد',
                               'شهریور', 'مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند')
        # lunar month
        elif monthType == 'lunar':
            self.monthNames = ('January', 'February', 'March', 'April', ' May', 'June',
                               'July', 'August', 'September', 'October', 'November', 'December')

        self.__year = 1400 if monthType == 'solar' else 2021 # default year
        self.__month = 1  # default month
        self.__day = 1  # default day

        self.year = year  # set year
        self.month = month  # set month
        self.day = day  # set day

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, y):
        if isinstance(y, int) and 0 < y:
            self.__year = y
        else:
            raise ValueError('year Value Error')

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, m):
        if isinstance(m, int) and 1 <= m <= 12:
            self.__month = m
        else:
            raise ValueError('month Value Error')

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, d):
        if isinstance(d, int) and 1 <= d <= self.months[self.__month-1]:
            self.__day = d
        else:
            raise ValueError('day Value Error')

    def __str__(self):
        return f'{self.year}/{self.month}/{self.day}'

    def __repr__(self):
        return f'{self.year}/{self.monthNames[self.month-1]}/{self.day}'

    def __next__(self):
        self.__day += 1
        if self.__day == self.months[self.__month-1]:
            self.__day = 1
            self.__month += 1
            if self.__month == 13:
                self.__month = 1
                self.__year += 1
        return self


if __name__ == "__main__":
    from datetime import datetime
    now = datetime.now()
    t = MyDate(now.year, now.month, now.day)
    print(t)
# else:
#     print('Welcome to my_date madule')
