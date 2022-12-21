import random


class ParkingLot:
    slot_width = 8
    slot_length = 12
    total_width = 0
    total_length = 0
    slot_count = 0
    slots = {}

    def __init__(self, width, length):
        self.total_width = width
        self.total_length = length
        count1 = width // self.slot_width * length // self.slot_length
        count2 = length // self.slot_width * width // self.slot_length
        self.slot_count = count1 if count1 > count2 else count2

    def get_slots_count(self):
        return self.slot_count

    def get_all_car_details(self):
        return self.slots


class Car:
    number_plate = ""
    slot = -1

    def __init__(self, number_plate):
        self.number_plate = number_plate

    def __str__(self):
        return self.number_plate

    def park(self, parking_lot, slot):
        if parking_lot.slot_count < slot:
            return False
        elif slot in parking_lot.slots:
            return False
        else:
            parking_lot.slots[slot] = self.number_plate
            self.slot = slot
            return True

    def get_slot(self):
        return self.slot


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    width = int(input("Enter parking lot width : "))
    length = int(input("Enter parking lot length : "))
    pl = ParkingLot(width, length)
    print("Number of cars can be parked in the specified parking lot : {0}", pl.get_slots_count())
    number_of_cars = int(input("Enter number of cars needed to be parked : "))
    for x in range(number_of_cars):
        number_plate = input("Enter car number : ")
        car = Car(number_plate)
        status = False
        while not status:
            slot = int(random.random() * pow(10, 15) % pl.get_slots_count()) + 1
            status = car.park(pl, slot)

        if status:
            print("Car with license plate {0} is parked successfully at slot {1}", car, car.get_slot())
        else:
            print("Car with license plate {0} is not parked successfully", car)
        if pl.get_slots_count() == len(pl.slots):
            print("Parking lot is full")
            break

    print(pl.get_all_car_details())
