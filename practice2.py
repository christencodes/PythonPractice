department = "Solid Waste"
headcount = "62"
separations = 10
is_reviewed = True

#casting issue
turnover_rate = (separations / int(headcount)) * 100

#proper bracket and quotation placement
print(f"Department:  {department}")
print(f"Separations:  {separations}")
print(f"Turnover rate: {round(turnover_rate, 1)}%")
print(f"Reviewed: {is_reviewed}")

status =  ""

if turnover_rate >= 20:
  status = "High"
elif turnover_rate >= 10:
  status = "Watch"
else:
  status = "Normal"

print(f"Solid Waste status: {status}")

if separations > 5 and int(headcount) < 50:
  print("Flag: small department with heavy losses")

if not is_reviewed:
  print("Needs review")