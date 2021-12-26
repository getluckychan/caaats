class CheckMethod:
    def __init__(self):
        self.running = None

    def set_running(self, running):
        self.running = running

    def get_running(self):
        return self.running


a = CheckMethod()
a.set_running(1)
while a.get_running() == 1:
    b = int(input())
    if b == 3:
        a.set_running(2)
    elif b == 2:
        print("коты идут")
        print("идут ли коты")


