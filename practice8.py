import csv

# variables
skipped = []
depts = []
citywide_count = 0
citywide_separations = 0
status_counts = {"High": 0, "Watch": 0, "Normal": 0}


# functions
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


with open("departments.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        try:
            row["name"] = row["name"].strip()
            row["headcount"] = int(row["headcount"])
            row["separations"] = int(row["separations"])
            depts.append(row)
        except ValueError as er:
            skipped.append({"name": row["name"], "error": str(er)})

# report
print("--------Departments-------")

# rate addition
for d in depts:
    d["rate"] = turnover_rate(d["separations"], d["headcount"])
    d["status"] = get_status(d["rate"])

# print out Name, Turnover Rate, Status
for d in depts:
    print(f"{d['name']}: {d['rate']}% ({d['status']})")

# count statuses
for d in depts:
    status_counts[d["status"]] += 1

# sum of all headcounts
# sum of all separations
for d in depts:
    citywide_count += d["headcount"]
    citywide_separations += d["separations"]

print()
# Number of separations out of headcount
print(
    f"{citywide_separations} out of {citywide_count}, {turnover_rate(citywide_separations, citywide_count)}%"
)

print(status_counts)

# data issues
print()

if not skipped:
    print("No data issues")
else:
    print("-----Data Issues-----")
    print(f"{len(skipped)} rows skipped")
    for row in skipped:
        print(f"{row['name']} : {row['error']}")

with open("turnover_report.csv", "w", newline="") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["name", "headcount", "separations", "rate", "status"],
    )
    writer.writeheader()
    writer.writerows(depts)

with open("data_issues.txt", "w") as file:
    if not skipped:
        file.write("No data issues\n")
    else:
        file.write("-----Data Issues-----\n")
        file.write(f"{len(skipped)} rows skipped\n")
        for row in skipped:
            file.write(f"{row['name']} : {row['error']}\n")
