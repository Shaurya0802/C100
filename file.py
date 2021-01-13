class Car(object):
    def __init__(self, color, company, model, speed_limit):
        self.color = color
        self.company = company
        self.model = model
        self.speed_limit = speed_limit

    def speed(self):
        print("Speeding up")

    def acceleration(self):
        print("Accelerating")

    def start(self):
        print("Starting")

    def stop(self):
        print("Stoping")

    def change_gear(self, gear_type):
        print("Changing Gear")

Maruti_Suzuki = Car("white", "Maruti Suzuki", "Top", 100)
print(Maruti_Suzuki.speed())