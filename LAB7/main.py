import vehicle
import fleet_manager

if __name__ == "__main__":
    my_vehicles = [
        vehicle.Car("V001", "BYD Seal", 2023, "Electric", 4),
        vehicle.Car("V002", "Honda Civic", 2018, "Petrol", 4),
        vehicle.Truck("T101", "Scania R590", 2019, 25000, 6),
        vehicle.Truck("T102", "BMC Pro 940", 2021, 18000, 4),
        vehicle.Motorcycle("M301", "Ducati 998", 2024, 998, "Sport"),
        vehicle.Motorcycle("M302", "BMW R1200", 2015, 1200, "Cruiser")
    ]

    fleet_manager.save_fleet_to_file(my_vehicles, "fleet.txt")

    print("Loading fleet data from 'fleet.txt'...")
    loaded_fleet = fleet_manager.load_fleet_from_file("fleet.txt")
    print(f"{len(loaded_fleet)} vehicles loaded successfully.\n")

    print("All Vehicles ---")
    for v in loaded_fleet:
        print(v)

    print("\nRecent Vehicles (Last 4 Years) ---")
    for v in loaded_fleet:
        if v.is_new(4):
            print(v)

    print("\nElectric Cars Only ---")
    for v in loaded_fleet:
        if isinstance(v, vehicle.Car) and v.fuel_type == "Electric":
            print(v)