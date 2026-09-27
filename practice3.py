

# sites = ['a','b','c','d','f']
# sub_sites = [10,20,30,40,50]

# for site in reversed(range(len(sites))):
#   print(f"Site: {sites[site] } ; Sub Site: {sub_sites[site]}")

departments = ["Utilities", "Solid Waste", "Parks", "Water", "Streets"]
headcounts = [48, 62, 35, 90, 41]
separations = [6, 10, 2, 21, 9]
turnover_rates = []
status = []
flagged = []
high_departments = len(flagged)
headcount_total = 0
separations_total = 0


for i in range(len(departments)):
  headcount_total += headcounts[i]
  separations_total += separations[i]

city_turnover = round((separations_total / headcount_total) * 100, 2)



for i in range(len(separations)):
  turnover_rates.append(round((separations[i]/headcounts[i]) * 100,2))

for i in range(len(turnover_rates)):
  if turnover_rates[i] >= 20:
    status.append("High")
  elif turnover_rates[i] >= 10:
    status.append("Watch")
  else:
    status.append("Normal")

for i in range(len(status)):
  if status[i] == "High":
    flagged.append(departments[i])

for i in range(len(departments)):
  print(f"{departments[i]}: {turnover_rates[i]}% ({status[i]})")

print(f"{separations_total} separations out of {headcount_total} employees, {city_turnover}% citywide, {high_departments} High, {flagged}")






