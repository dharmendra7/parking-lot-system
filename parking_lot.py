class ParkingLot:
    def __init__(self):
        self.levels = {'A': [0] * 21, 'B': [0] * 21}
        self.vehicle_mapping = {} 

    def assign_parking_spot(self, vehicle_number):
        for level, spots in self.levels.items():
            for spot in range(1, len(spots)):
                if spots[spot] == 0:
                    spots[spot] = 1
                    self.vehicle_mapping[vehicle_number] = {'level': level, 'spot': spot}
                    return {'level': level, 'spot': spot}

    def retrieve_parking_spot(self, vehicle_number):
        if vehicle_number in self.vehicle_mapping:
            return self.vehicle_mapping[vehicle_number]
        else:
            return None

    def unpark_vehicle(self, vehicle_number):
        if vehicle_number in self.vehicle_mapping:
            spot_info = self.vehicle_mapping[vehicle_number]
            level, spot = spot_info['level'], spot_info['spot']
            self.levels[level][spot] = 0
            del self.vehicle_mapping[vehicle_number]
            return {'level': level, 'spot': spot}
        else:
            return None

    def retrieve_nearest_parking_location(self, level):
        for spot in range(1, len(self.levels[level])):
            if self.levels[level][spot] == 0:
                return {'level': level, 'spot': spot}
