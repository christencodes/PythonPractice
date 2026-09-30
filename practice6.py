import csv

depts = []

with open("departments.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        depts.append(
            {
                "name": row["name"],
                "headcount": int(row["headcount"]),
                "separations": int(row["separations"]),
            }
        )

for d in depts:
    print(d)

citywide_count = 0
citywide_separations = 0


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


# TypeError: int() argument must be a string, a bytes-like object or a real number, not 'NoneType'
