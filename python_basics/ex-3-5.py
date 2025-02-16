all_stations = set(unique_stations)
for route in schedules.values():
    for _, station in route:
        all_stations.add(station)

total_unique_stations = len(all_stations)