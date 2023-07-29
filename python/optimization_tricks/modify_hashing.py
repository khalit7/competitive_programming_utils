from random import getrandbits

RANDOM = getrandbits(32)

class IntWrapper(int):
    def __init__(self, x):
        int.__init__(x)

    def __hash__(self):
        # larger hashing values ===> less collision (less time complexity) but more memory (more space complexity)
        return super(IntWrapper, self).__hash__() ^ RANDOM