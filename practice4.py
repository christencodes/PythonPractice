

# sites = ['a','b','c','d','f']
# sub_sites = [10,20,30,40,50]

# for site in reversed(range(len(sites))):
#   print(f"Site: {sites[site] } ; Sub Site: {sub_sites[site]}")

departments = ["Utilities", "Solid Waste", "Parks", "Water", "Streets"]
headcounts = [48, 62, 35, 90, 41]
separations = [6, 10, 2, 21, 9]
turnover_rates = []
flagged = []
headcount_total = 0
separations_total = 0


def turnoverRate(seps,count):
  return round((seps/count) * 100, 2) 

def getStatus(rate, high=20, watch=10):
    if rate >= high:
      return "High"
    elif rate >= watch:
      return "Watch"
    else:
      return "Normal"

#turnover_rates
for i in range(len(headcounts)):
  turnover_rates.append(turnoverRate(separations[i], headcounts[i]))

#headcount_total
#separation_total
for i in range(len(departments)):
  headcount_total += headcounts[i]
  separations_total += separations[i]

#city turnover rate
city_turnover = turnoverRate(separations_total,headcount_total)

#flagged departments
for i in range(len(turnover_rates)):
  if getStatus(turnover_rates[i]) == "High":
    flagged.append(departments[i])

#department stat by department 
for i in range(len(departments)):
  print(f"{departments[i]}: {turnover_rates[i]}% ({getStatus(turnover_rates[i])})")

print(f"{separations_total} separations out of {headcount_total} employees, {city_turnover}% citywide, {len(flagged)} High, {flagged}")






