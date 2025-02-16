class TransportNetwork:
    def __init__(self):
        self.routes = []
        self.schedules = {}
        self.passengers = defaultdict(list)
    
    def add_route(self, route_name):
        self.routes.append(route_name)
    
    def update_schedule(self, route_name, schedule):
        self.schedules[route_name] = schedule
    
    def add_passenger(self, schedule_name, passenger):
        self.passengers[schedule_name].append(passenger)
    
    def list_routes(self):
        return self.routes
