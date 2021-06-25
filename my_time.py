class MyTime:
    def __init__(self, hour, minute, second):
        self.__hour = 0
        self.__minute = 0
        self.__second = 0
        self.hour = hour
        self.minute = minute
        self.second = second

    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, h):
        if isinstance(h, int) and 0 <= h < 24:
            self.__hour = h
        else:
            raise ValueError('hour Value Error')

    @property
    def minute(self):
        return self.__minute

    @minute.setter
    def minute(self, m):
        if isinstance(m, int) and 0 <= m < 60:
            self.__minute = m
        else:
            raise ValueError('minute Value Error')

    @property
    def second(self):
        return self.__second

    @second.setter
    def second(self, s):
        if isinstance(s, int) and 0 <= s < 60:
            self.__second = s
        else:
            raise ValueError('second Value Error')

    def isMidnight(self):
        return self.hour == 0 and self.minute == 0 and self.second == 0

    def ding(self):
        import winsound
        from random import randrange
        if self.isMidnight():
            for _ in range(5):
                winsound.Beep(randrange(100, 4500), 200)
            print('Ding Ding Ding')

    def __str__(self):
        return f'{self.hour:02}:{self.minute:02}:{self.second:02}'

    def __repr__(self):
        if self.hour < 12:
            return f'{self.hour:02}:{self.minute:02}:{self.second:02} AM'
        elif self.hour == 12:
            return f'{self.hour:02}:{self.minute:02}:{self.second:02} PM'
        else:
            return f'{self.hour-12:02}:{self.minute:02}:{self.second:02} AM'

    def tik(self):
        self.__second = (self.__second+1) % 60
        if self.__second == 0:
            self.__minute = (self.__minute+1) % 60
            if self.__minute == 0:
                self.__hour = (self.__hour+1) % 24

    def __next__(self):
        self.tik()
        if self.isMidnight():
            self.ding()
        return self


if __name__ == "__main__":
    from datetime import datetime
    from time import sleep
    now = datetime.now()
    t = MyTime(now.hour, now.minute, now.second)
    while True:
        print(repr(next(t)))
        sleep(1)
# else:
#     print('Welcome to my_time madule')