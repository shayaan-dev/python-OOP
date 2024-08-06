class Car:
    def __init__(self, company, car, hp, color):
        self.company = company
        self.car = car
        self.hp = hp
        self.color = color

    def run(self):
        print(f"{self.color} {self.company} {self.car} of {self.hp} horsepower")


def ask_question():
    car_name = input("COMPANY: ")
    company_name = input("CAR NAME: ")
    color_name = input("COLOR: ")
    print("THANK YOU")
    print("_" * 250)

    return company_name, car_name, color_name


# Asking questions and creating car objects
company_name, car_name, color_name = ask_question()
mom_car = Car(company_name, car_name, 2000, color_name)

company_name, car_name, color_name = ask_question()
dad_car = Car(company_name, car_name, 2500, color_name)

company_name, car_name, color_name = ask_question()
sister_car = Car(company_name, car_name, 1800, color_name)

print("Mom")
mom_car.run()
print("Dad")
dad_car.run()
print("Sister")
sister_car.run()
