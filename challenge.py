department = "Solid Waste"
headcount = "62"
separations = 7
#True not true
is_reviewed = True

#casting issue
turnover_rate = (separations / int(headcount)) * 100

#proper bracket and quotation placement
print(f"Department:  {department}")
print(f"Separations:  {separations}")
print(f"Turnover rate: {round(turnover_rate, 1)}%")
print(f"Reviewed: {is_reviewed}")