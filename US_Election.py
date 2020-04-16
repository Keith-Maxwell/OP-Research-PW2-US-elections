import pulp
import pandas as pd

''' Hypothesis :
The population is over 18 years old, and citizens.
Puerto Rico has the right to vote or not, we will do both cases.
Puerto Rico voted for Hillary Clinton at 100%
Variable number of great electors 
'''

while True:
    try:  # ensures the input is either 1 or 0 and not something else
        yesno = int(input('Does Puerto-Rico have the right of vote ? (1: yes, 0: no) \n'))
        if yesno >= 0:
            if yesno <= 1:
                break
    except ValueError:
        print('please enter either 1 or 0')
while True:
    try:
        min_nb_electors = int(input("Enter the minimum number of great electors per state :\n"))
        if type(min_nb_electors) == int:
            break
    except ValueError:
        print("Please enter a number")


N_votes = 538  # nombre de grands électeurs


# extraction des données depuis le fichier .csv
if yesno == 0:
    data = pd.read_csv('US_voters_without_PuertoRico.csv')  # données du site census.gov, citoyens de + de 18 ans
else:
    data = pd.read_csv('US_voters.csv')


# définition du problème
prob = pulp.LpProblem("répartition des grands électeurs", pulp.LpMinimize)


# définition des variables (u, v et les alpha_i) du problème
u = pulp.LpVariable('u', 0, None, pulp.LpContinuous)
v = pulp.LpVariable('v', 0, None, pulp.LpContinuous)

alpha_list = []  # la variable 'alpha' représente le nombre de grands électeurs dans l'Etat 'i'
population_list = []  # population dans l'Etat 'i'
for i in range(data.__len__()):
    alpha_i = pulp.LpVariable(str(data.iloc[i, 0]), min_nb_electors, None,
                              pulp.LpInteger)  # définition des variables alpha_i
    alpha_list.append(alpha_i)
    population_list.append(int(data.iloc[i, 1]))


# définition de la fonction objectif
prob += u - v, 'objectif'


# définition des contraintes
for i in range(len(alpha_list)):
    prob += alpha_list[i] * 1e6 / float(population_list[i]) - u <= 0
    prob += v - alpha_list[i] * 1e6 / float(population_list[i]) <= 0
prob += alpha_list[8] == min_nb_electors  # the district of columbia cannot have
# more than the minimum number of great electors
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

'''
When Puerto-Rico can vote, Trump wins with 312 votes, even though Puerto-Rico votes for Clinton.

When Puerto-Rico cannot vote, Trump still wins but with only 310 votes. The electors are split differently

Whatever the minimum number of great electors per state, Trump always wins 

Even if Florida, which had 49% for Trump and 48% for Clinton, switched for Clinton, Trump would still win. (both cases : with and without PuertoRico)
'''
