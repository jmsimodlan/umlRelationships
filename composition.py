class Engine:
    def start(self):
        print("The engine starts.")


class Car:
    def __init__(self):
        # The Car creates its own Engine
        self.engine = Engine()

    def start_car(self):
        print("Starting the car...")
        self.engine.start()


# Create a Car object
car = Car()

# Start the car and its engine
car.start_car()
