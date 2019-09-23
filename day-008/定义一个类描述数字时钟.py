from time import sleep

class Clock(object):

    def __init__(self,hour=0,minute=0,second=0):
        self._hour=hour
        self._minute=minute
        self._second=second

    def run(self):
        while True:
            sleep(1)
            self._second += 1
            if self._second >= 60:
                self._second = 0
                self._minute += 1
                if self._minute >= 60:
                    self._minute = 0
                    self._hour += 1
                    if self._hour >= 60:
                        self._hour = 0
            self.show_time()


    def show_time(self):
        print(f"{self._hour}:{self._minute}:{self._second}")


my_clock=Clock(2,3,4)
my_clock.run()