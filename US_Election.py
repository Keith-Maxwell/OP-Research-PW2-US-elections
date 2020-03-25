import pulp
import pandas as pd

N_votes = 538  # nombre de grands électeurs
# extraction des données depuis le fichier .csv
data = pd.read_csv('US_voters_without_PuertoRico.csv')  # données du site census.gov, citoyens de + de 18 ans

# définition du problème
prob = pulp.LpProblem("répartition des grands électeurs", pulp.LpMinimize)

# définition des variables (u, v et les alpha_i) du problème
u = pulp.LpVariable('u', 0, None, pulp.LpContinuous)
v = pulp.LpVariable('v', 0, None, pulp.LpContinuous)
alpha_list = []  # la variable 'alpha' représente le nombre de grands électeurs dans l'Etat 'i'
population_list = []  # population dans l'Etat 'i'
for i in range(data.__len__()):
    alpha_i = pulp.LpVariable(str(data.iloc[i, 0]), 3, None, pulp.LpInteger)  # définition des variables alpha_i
    alpha_list.append(alpha_i)
    population_list.append(int(data.iloc[i, 1]))

# définition de la fonction objectif
prob += u - v, 'objectif'

# définition des contraintes
for i in range(len(alpha_list)):
    prob += alpha_list[i] * 1e6 / float(population_list[i]) - u <= 0
    prob += v - alpha_list[i] * 1e6 / float(population_list[i]) <= 0
prob += sum(alpha_list) == N_votes

# résolution du problème
prob.solve()
print("status : ", pulp.LpStatus[prob.status])

# affichage des résultats
states = [v.name for v in prob.variables()]
nb_electors = [v.varValue for v in prob.variables()]
states = states[:-2]  # on enlève les deux dernières variables qui sont u et v car elles ne nous intéressent pas
nb_electors = nb_electors[:-2]
df = pd.DataFrame(nb_electors, index=states)  # création d'une DataFrame Pandas juste pour le format d'affichage
print(df)

# addition des votes (pour D. Trump)
s = 0
for i in range(data.__len__()):
    s += data.iloc[i, 2] * nb_electors[i]

# Résultats des votes
if s > N_votes / 2:
    print('Donald Trump wins ! with : ', s, ' votes')
elif s < N_votes / 2:
    print('Hillary Clinton wins ! with : ', N_votes - s, ' votes')
else:
    print("it's a draw !")
