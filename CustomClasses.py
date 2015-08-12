class Pair():
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __str__(self):
        return str(self.first.encode('utf-8', 'ignore'))[2:-1] + "\n" + self.second

    def get_second(self):
        return self.second