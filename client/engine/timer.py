import time


class Timer:
    def __init__(self, target: callable, duration: float, exec_first: bool = False, args: tuple | list = tuple(),
                 cyclic: bool = False):
        self.target = target
        self.duration = duration
        self.exec_first = exec_first
        self.args = args
        self.active = False
        self.cyclic = cyclic

        self.start_time = time.time()

    def activate(self):
        if not self.active:
            self.start_time = time.time()
            self.active = True
            if self.exec_first:
                self.target(*self.args)

    def update(self):
        if self.active:
            elapsed = time.time() - self.start_time
            if elapsed > self.duration:
                if not self.exec_first:
                    self.target(*self.args)
                self.active = False
                if self.cyclic:
                    self.activate()
