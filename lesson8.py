import csv

rows = [
    {"name": "Police", "rate": 10.5, "status": "Normal"},
    {"name": "Fire", "rate": 21.5, "status": "Watch"},
]

with open("test.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "rate", "status"])
    writer.writeheader()
    writer.writerows(rows)
