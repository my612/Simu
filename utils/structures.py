import time


class Change:
    def __init__(self, inputName, inputValue):
        self.input_name = inputName
        self.input_value = inputValue

class Timer:
    def __init__(self):
        self.start = time.perf_counter()
    def get_time(self):
        return time.perf_counter() - self.start
