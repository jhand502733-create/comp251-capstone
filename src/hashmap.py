class DepotMap:
    def __init__(self):
        self.map = {}

    def add_depot(self, depot_name, info):
        self.map[depot_name] = info

    def get_depot(self, depot_name):
        return self.map.get(depot_name, "Depot not found")

    def display(self):
        for depot in self.map:
            print(depot, "->", self.map[depot])
