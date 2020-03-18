from pulp import *

prob = pulp.LpProblem("Diet", pulp.LpMinimize)

# Decision variables

x1 = LpVariable("Steak", 0, None, LpInteger)
x2 = LpVariable("Peanutbutter", 0, None, LpInteger)

# Objective

prob += 2 * x2 + 3 * x1, "total cost"

# Constraints

prob += 2 * x1 + x2 >= 4, "Minimum protein intake"

# --------------

prob.solve()

print("status : ", LpStatus[prob.status])
for v in prob.variables():
    print(v.name, " = ", v.varValue)

print("Optimal solution to the problem : ", value(prob.objective), " dollars")