
class MyIterator:

    def __init__(self, input):
        self.input = input
        self.i = 0

    def has_next(self):
        if self.input is None or len(self.input) <= 0:
            return False
        if self.i < len(input):
            return True
        return False

    def get_next(self):
        while self.has_next():
            ret_val = self.input[self.i]
            self.i += 1
            if type(ret_val) == list:
                inner = MyIterator(ret_val)
                yield inner.get_next()

            yield ret_val


# input = None
# input = []
input = [1, 2, [3, 4], 5]

myI = MyIterator(input)

# while myI.has_next():
    # print(myI.get_next())

gen = myI.get_next()
for i in gen:
    print(i)
