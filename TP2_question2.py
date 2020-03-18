from pulp import *

# --------------------------
# Problème 1 dans R
# --------------------------

# Définition du problème linéaire
prob1 = pulp.LpProblem("Prob 1", LpMinimize)

# Définition des variables
x1 = LpVariable("x1", 0, None, LpContinuous)
x2 = LpVariable("x2", 0, None, LpContinuous)

# Définition de l'objectif
prob1 += -8 * x1 - 5 * x2, "Objectif prob1"

# Définitions des contraintes
prob1 += x1 + x2 <= 6, "contrainte 1"
prob1 += 9 * x1 + 5 * x2 <= 45, "contrainte 2"

prob1.solve()

print("status : ", LpStatus[prob1.status])
for v in prob1.variables():
    print(v.name, " = ", v.varValue)
print("Optimal solution to the problem : ", value(prob1.objective))
print("--------------------")

# --------------------------
# Problème 1 dans N
# --------------------------

# Définition du problème linéaire
prob2 = pulp.LpProblem("Prob 2", LpMinimize)

# Définition des variables
x1 = LpVariable("x1", 0, None, LpInteger)
x2 = LpVariable("x2", 0, None, LpInteger)

# Définition de l'objectif
prob2 += -8 * x1 - 5 * x2, "Objectif prob2"

# Définitions des contraintes
prob2 += x1 + x2 <= 6, "contrainte 1"
prob2 += 9 * x1 + 5 * x2 <= 45, "contrainte 2"

prob2.solve()

print("status : ", LpStatus[prob2.status])
for v in prob2.variables():
    print(v.name, " = ", v.varValue)
print("Optimal solution to the problem : ", value(prob2.objective))
print("--------------------")


# ========================================================================================

# --------------------------
# Problème 2 dans R
# --------------------------

# Définition du problème linéaire
prob3 = pulp.LpProblem("Prob 3", LpMinimize)

# Définition des variables
x1 = LpVariable("x1", 0, None, LpContinuous)
x2 = LpVariable("x2", 0, None, LpContinuous)
x3 = LpVariable("x3", 0, None, LpContinuous)

# Définition de l'objectif
prob3 += 2 * x1 + 7 * x2 + 2 * x3, "Objectif prob3"

# Définitions des contraintes
prob3 += x1 + 4 * x2 + x3 >= 10, "contrainte 1"
prob3 += 4 * x1 + 2 * x2 + 2*x3 >= 13, "contrainte 2"
prob3 += x1 + x2 - x3 >= 0, "contrainte 3"


prob3.solve()

print("status : ", LpStatus[prob3.status])
for v in prob3.variables():
    print(v.name, " = ", v.varValue)
print("Optimal solution to the problem : ", value(prob3.objective))
print("--------------------")

# --------------------------
# Problème 2 dans N
# --------------------------

# Définition du problème linéaire
prob4 = pulp.LpProblem("Prob 4", LpMinimize)

# Définition des variables
x1 = LpVariable("x1", 0, None, LpInteger)
x2 = LpVariable("x2", 0, None, LpInteger)
x3 = LpVariable("x3", 0, None, LpInteger)

# Définition de l'objectif
prob4 += 2 * x1 + 7 * x2 + 2 * x3, "Objectif prob4"

# Définitions des contraintes
prob4 += x1 + 4 * x2 + x3 >= 10, "contrainte 1"
prob4 += 4 * x1 + 2 * x2 + 2*x3 >= 13, "contrainte 2"
prob4 += x1 + x2 - x3 >= 0, "contrainte 3"


prob4.solve()

print("status : ", LpStatus[prob4.status])
for v in prob4.variables():
    print(v.name, " = ", v.varValue)
print("Optimal solution to the problem : ", value(prob4.objective))
print("--------------------")
