import pandas as pd
import matplotlib.pyplot as plt

table = pd.read_csv('donnees_patients.csv', sep=',')

print("Age moyen :", table['age'].mean())
print("Nombre de patients par traitement : \n", table['traitement'].value_counts())
print("Nombre de resultats par type :\n", table['résultat'].value_counts())
print("L'age moyen par sexe est: \n", table.groupby("sexe")["age"].mean())

pa = table[table['résultat'] == 'amélioration']
print("Patients ameliores :\n", pa)

gp = table[table['sequence_adn'] == "ACTCTCTCTATATTTATATATCGTCAGTGCTGGACTTGCATCGAGTTGC"] 
print("genes present :\n", gp) 

print("Moyenne d'age des patients améliorés :", pa['age'].mean())

table['sexe'].value_counts().plot(kind='bar', title='Nombre de patients par sexe')
plt.xlabel('Sexe')
plt.ylabel('Nombre de patients')
plt.tight_layout()
plt.savefig('nombre_de_patients_par_sexe.png')
plt.show()



table.groupby('sexe')['age'].mean().plot(kind='bar', title='Age moyen par sexe')
plt.xlabel('Sexe')
plt.ylabel('Age moyen')
plt.tight_layout()
plt.savefig('age_moyen_par_sexe.png')
plt.show()
