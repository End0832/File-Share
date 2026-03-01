df <- read.csv("donnees_patients.csv", sep = ",") 

head(df)

moyenne <- mean(df$age)
ecart_type <- sd(df$age)

print(paste("Moyenne d'age :", moyenne))
print(paste("Ecart-type :", ecart_type))

table(df$traitement, df$résultat)

barplot(table(df$résultat), main="TITRE QUE TU DOIS REMPLACER", col="red")
