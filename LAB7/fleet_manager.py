from vehicle import Car, Truck, Motorcycle


def save_fleet_to_file(vehicles, filename):
    with open(filename, "w") as f:
        for v in vehicles:
            if isinstance(v, Car):
                line = f"Car, {v.vid}, {v.model}, {v.year}, {v.fuel_type}, {v.doors}\n"
            elif isinstance(v, Truck):
                line = f"Truck, {v.vid}, {v.model}, {v.year}, {v.max_load}, {v.axles}\n"
            elif isinstance(v, Motorcycle):
                line = f"Motorcycle, {v.vid}, {v.model}, {v.year}, {v.engine_cc}, {v.m_type}\n"
            f.write(line)


def load_fleet_from_file(filename):
    fleet = []
    with open(filename, "r") as f:
        for line in f:
            parts = [p.strip() for p in line.split(",")]
            v_type = parts[0]

            if v_type == "Car":
                obj = Car(parts[1], parts[2], int(parts[3]), parts[4], int(parts[5]))
            elif v_type == "Truck":
                obj = Truck(parts[1], parts[2], int(parts[3]), int(parts[4]), int(parts[5]))
            elif v_type == "Motorcycle":
                obj = Motorcycle(parts[1], parts[2], int(parts[3]), int(parts[4]), parts[5])

            fleet.append(obj)
    return fleet