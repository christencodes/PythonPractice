citywide_count = 0
citywide_separations = 0

depts = [
    {"name": "Utilities", "headcount": 48, "separations": 6},
    {"name": "Solid Waste", "headcount": 62, "separations": 10},
    {"name": "Parks", "headcount": 35, "separations": 2},
    {"name": "Water", "headcount": 90, "separations": 21},
    {"name": "Streets", "headcount": 41, "separations": 9},
    {"name": "Library", "headcount": 0, "separations": 0},
]

status_counts = {"High": 0, "Watch": 0, "Normal": 0}


def turnover_rate(seps, count):
    if count == 0:
        return 0
    return round((seps / count) * 100, 2)


def get_status(rate, high=20, watch=10):
    if rate >= high:
        return "High"
    elif rate >= watch:
        return "Watch"
    else:
        return "Normal"


for d in depts:
    d["rate"] = turnover_rate(d["separations"], d["headcount"])
    d["status"] = get_status(d["rate"])


for d in depts:
    print(f"{d['name']}: {d['rate']}% ({d['status']})")


for d in depts:
    status_counts[d["status"]] += 1


for d in depts:
    citywide_count += d["headcount"]
    citywide_separations += d["separations"]

print(
    f"{citywide_separations} out of {citywide_count}, {turnover_rate(citywide_separations, citywide_count)}%"
)

print(status_counts)
