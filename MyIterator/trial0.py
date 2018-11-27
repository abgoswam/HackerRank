class MyIterator:

    def __init__(self, input):
        self.input = input
        self.i = 0

    def get_inputs(self):
        ret = []
        for i in range(len(self.input)):
            ret.append(self.input[i])
        return ret

    def get_inputs_gen(self):
        for i in range(len(self.input)):
            yield self.input[i]


input = [1, 2, 3, 4, 5]

myI = MyIterator(input)
print(myI.get_inputs())

print(myI.get_inputs_gen())
gen = myI.get_inputs_gen()
for i in gen:
    print(i)

