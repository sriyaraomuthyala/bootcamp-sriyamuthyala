from collections import Counter
station_visits = Counter([station for route in schedules.values() for _, station in route])
most_frequented = station_visits.most_common(1)