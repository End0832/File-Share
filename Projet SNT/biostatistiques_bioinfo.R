df <- read.csv("donnees_patients.csv", sep = ",") 

# L'ajout du print() est nécessaire pour l'affichage de head()
print(head(df))

moyenne <- mean(df$age)
ecart_type <- sd(df$age)

print(paste("Moyenne d'age :", moyenne))
print(paste("Ecart-type :", ecart_type))

# L'ajout du print() est nécessaire pour l'affichage de table()
print(table(df$traitement, df$résultat))

barplot(table(df$résultat), main="Histogramme de la repartition des patients en fonction du resultat de l'action du medicament", col="blue")
