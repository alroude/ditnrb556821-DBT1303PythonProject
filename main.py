print('\t\tWelcome to NMS Parking')
car = input("Car price: ")
car = int(car)
bike = input("Bike Price: ")
bike = int(bike)
truck = input("Truck Price: ")
truck = int(truck)
bicycle = input("Bicycle Price: ")
bicycle = int(bicycle)
bus = input("Bus Price: ")
bus = input(bus)
maxx = input("Enter Maximum Parking Slots: ")
print('\n*****************')
maxx = int(maxx)
total = 0
tcar=pcar=tbike=pbike=ttruck=ptruck=tbicycle=pbicycle=tbus=pbus=tslot=0
tslot = maxx
while maxx:
    print(f'Total Slots::{tslot}\t\tFree Slots::{maxx}\n')
    vehicle = input("Enter 1 for Car\nEnter 2 for Bike\nEnter 3 for Truck\nEnter 4 for Bicycle\nEnter 5 for Bus\nEnter 6 to view Record\nEnter 7 to delete record")
    print('\n**********************************')
    vehicle = int(vehicle)
    if vehicle == 1:
        total+=car
        tcar+=1
        pcar+=car
    elif vehicle == 2:
        total+=bike
        tbike+=1
        pbike+=bike
    elif vehicle == 3:
        total+=truck
        truck+=1
        ptruck+=truck
    elif vehicle == 4:
        total+=bicycle
        tbicycle+=1
        pbicycle+=bicycle
    elif vehicle == 5:
        total+=bus
        tbus+=1
        pbus+=bus
    elif vehicle == 6:
        print(f'Total cars: {tcar}\t\tcars total price: {pcar}\nTotal Bikes: {tbike}\t\tbikes total price: {pbike}\nTotal Trucks: {ttruck}\t\ttrucks total price: {ptruck}\nTotal Bicycles: {tbicycle}\t\tbicycles total price: {pbicycle}\nTotal Buses: {tbus}\t\tbus total price: {pbus}')
        print('\n******************************************')
        maxx+=1
    elif maxx == 0:
        print(" Slots are Full")
        print(f'total::{total}')


