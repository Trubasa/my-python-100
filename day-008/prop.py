
class Clock(object):

    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self.__minute = minute
        self._second = second


my_clock = Clock(2, 3, 4)
print(my_clock._hour)
print(my_clock._Clock__minute)
