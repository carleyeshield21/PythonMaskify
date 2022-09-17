# This is the link to this Python Coding Challenge
# https://www.codewars.com/kata/5412509bd436bd33920011bc/train/python

class Maskify:
    def __init__(self, cc):
        self.cc = cc

    def result(self):
        # print(self.cc)
        cc_length = len(self.cc)
        str = ''
        j = 0
        for i in self.cc:
            # print(i)
            # str += i
            # j = 0
            while j <= cc_length - 5:
                str += '#'
                # print(j)
                j += 1

        for k in range(j, cc_length):
            # print(f'k = {k}')
            # print(self.cc[k])
            str += self.cc[k]
        print(str)

        # print(f'j = {j}')
        # print(str)
        # print(cc_length)