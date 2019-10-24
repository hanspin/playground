class Roadlight:
    'Playground road light'
    battery = 0

    def __init__(self):
        self.battery = 0

    def switch_on(self):
        if self.battery > 0:
            print("light light light")
            self.battery -= 1
        else:
            print("power low, please recharge")

    def switch_off(self):
        print("good night")

    def recharge(self):
        self.battery += 1
