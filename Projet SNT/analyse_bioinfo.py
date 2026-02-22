import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('donnees_patients.csv', sep=',')

print("Age moyen :", df['age'].mean())
print("Nombre de patients par traitement : \n", df['traitement'].value_counts())
print("Nombre de resultats par type :\n", df['résultat'].value_counts())
print("L'age moyen par sexe est: \n", df.groupby("sexe")["age"].mean())

patients_ameliores = df[df['résultat'] == 'amélioration']
print("Patients ameliores :\n", patients_ameliores)

### Les lignes suivantes sont commentées pour le bon fonctionnement du code.

#gene = df[df['sequence_adn'] == "sequence_ADN"] 
#print("genes present :\n", gene) 

### "sequence_ADN" est non fourni. 
### De plus sous cette syntaxe, sequence_ADN doit être EGALE et non pas contenue.
### Cette syntaxe correspond mieux :

#gene = df[df['sequence_adn'].str.contains("sequence_ADN")]

print("Moyenne d'age des patients améliorés :", patients_ameliores['age'].mean())

df['sexe'].value_counts().plot(kind='bar', title='Nombre de patients par sexe')
plt.xlabel('Sexe')
plt.ylabel('Nombre de patients')
plt.tight_layout()
plt.savefig('graphique_nombre_de_patients_par_sexe.png')
plt.show()



df.groupby('sexe')['age'].mean().plot(kind='bar', title='Age moyen par sexe')
plt.xlabel('Sexe')
plt.ylabel('Age moyen')
plt.tight_layout()
plt.savefig('graphique_age_moyen_par_sexe.png')
plt.show()
