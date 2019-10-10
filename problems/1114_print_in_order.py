# Solution with Various Concurrency Method (Barrier, Lock, Event, Semaphore, Condition)

from threading import Barrier

class Foo:
    def __init__(self):
        self.barriers = (Barrier(2), Barrier(2))

    def first(self, printFirst):
        printFirst()
        self.barriers[0].wait()

    def second(self, printSecond):
        self.barriers[0].wait()
        printSecond()
        self.barriers[1].wait()

    def third(self, printThird):
        self.barriers[1].wait()
        printThird()


from threading import Lock

class Foo:
    def __init__(self):
        self.locks = (Lock(),Lock())
        self.locks[0].acquire()
        self.locks[1].acquire()

    def first(self, printFirst):
        printFirst()
        self.locks[0].release()

    def second(self, printSecond):
        with self.locks[0]:
            printSecond()
            self.locks[1].release()

    def third(self, printThird):
        with self.locks[1]:
            printThird()


from threading import Event

class Foo:
    def __init__(self):
        self.events = (Event(),Event())

    def first(self, printFirst):
        printFirst()
        self.events[0].set()

    def second(self, printSecond):
        self.events[0].wait()
        printSecond()
        self.events[1].set()

    def third(self, printThird):
        self.events[1].wait()
        printThird()


from threading import Semaphore

class Foo:
    def __init__(self):
        self.gates = (Semaphore(0),Semaphore(0))

    def first(self, printFirst):
        printFirst()
        self.gates[0].release()

    def second(self, printSecond):
        with self.gates[0]:
            printSecond()
            self.gates[1].release()

    def third(self, printThird):
        with self.gates[1]:
            printThird()


from threading import Condition

class Foo:
    def __init__(self):
        self.condition = Condition()
        self.order = 0
        self.first_finish = lambda: self.order == 1
        self.second_finish = lambda: self.order == 2

    def first(self, printFirst):
        with self.condition:
            printFirst()
            self.order = 1
            self.condition.notify(2)

    def second(self, printSecond):
        with self.condition:
            self.condition.wait_for(self.first_finish)
            printSecond()
            self.order = 2
            self.condition.notify(1)

    def third(self, printThird):
        with self.condition:
            self.condition.wait_for(self.second_finish)
            printThird()
