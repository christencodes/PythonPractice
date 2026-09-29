# person = {"name": "Chris", "age": 135, "ass": "fat"}


# # print(person["ass"])
# # print(person["age"])
# person["neck"] ="thick"
# person["age"] = 35
# # print(person["neck"])
# # print("ass" in person)
# # print("chest" in person)

# # for i, k in person.items():
# #   print(i, k)

# people = [
#     {"name": "Christina", "age": 55, "ass": "flat", "neck": "thin"},
#     {"name": "Ashley", "age": 85, "ass": "earth-like", "neck": "verbose"}
#   ]

# # for p in people:
# #     print(f"{p['name']} has a {p['ass']} ass")

# print(people[1]['age'])
# people[1]['age'] += 1
# print(people[1]['age'])  





citywide_count = 0
citywide_separations = 0
citywide_rate = 0

depts = [
    {"name": "Utilities", "headcount": 48, "separations": 6},
    {"name": "Solid Waste", "headcount": 62, "separations": 10},
    {"name": "Parks", "headcount": 35, "separations": 2},
    {"name": "Water", "headcount": 90, "separations": 21},
    {"name": "Streets", "headcount": 41, "separations": 9},
    {"name": "Library", "headcount": 0, "separations": 0},
]

status_counts = {"High": 0, "Watch": 0, "Normal": 0}

def turnoverRate(seps,count):
  return round((seps/count) * 100, 2) 

def getStatus(rate, high=20, watch=10):
    if rate >= high:
      return "High"
    elif rate >= watch:
      return "Watch"
    else:
      return "Normal"





for d in depts:
  if d["headcount"] == 0 or d["separations"] == 0:
    d['rate'] = 0
    d["status"] = getStatus(d["rate"])
  
    continue
  d["rate"] = turnoverRate(d["separations"],d["headcount"])
  d["status"] = getStatus(d["rate"])

for d in depts:
    print(f"{d['name']}: {d['rate']}% ({d['status']})")


for d in depts:
  if 'status' not in d:
    continue
  status_counts[d['status']] += 1



for d in depts:
  citywide_count += d['headcount']
  citywide_separations += d['separations']

print(f"{citywide_separations} out of {citywide_count}, {turnoverRate(citywide_separations, citywide_count)}%")


  
  





# for d in depts:
#   if d['separations'] and d['headcount'] == 0:
#     continue
#   d["rate"] = turnoverRate(d['separations'],d['headcount'])
#   print(d)
  