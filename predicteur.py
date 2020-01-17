Matrice = ("Fille","Garçon","Fille","Garçon","Garçon","Garçon","Garçon","Garçon","Garçon","Garçon","Garçon","Garçon",
           "Garçon","Fille","Garçon","Fille","Fille","Garçon","Garçon","Fille","Garçon","Garçon","Fille","Fille",
           "Fille","Garçon","Fille","Garçon","Garçon","Garçon","Garçon","Garçon","Garçon","Fille","Garçon","Garçon",
           "Garçon","Fille","Fille","Fille","Fille","Fille","Fille","Fille","Fille","Fille","Fille","Fille",
           "Fille","Garçon","Garçon","Fille","Garçon","Fille","Fille","Garçon","Fille","Fille","Fille","Fille",
           "Garçon","Garçon","Garçon","Fille","Garçon","Garçon","Fille","Fille","Fille","Garçon","Garçon","Fille",
           "Garçon","Fille","Fille","Garçon","Garçon","Fille","Garçon","Fille","Garçon","Garçon","Fille","Garçon",
           "Fille","Garçon","Fille","Garçon","Fille","Garçon","Fille","Garçon","Fille","Garçon","Garçon","Garçon",
           "Garçon","Garçon","Garçon","Garçon","Garçon","Fille","Garçon","Fille","Fille","Garçon","Fille","Fille",
           "Fille","Fille","Garçon","Garçon","Fille","Garçon","Fille","Fille","Garçon","Fille","Garçon","Garçon",
           "Garçon","Garçon","Garçon","Fille","Fille","Garçon","Fille","Garçon","Fille","Fille","Garçon","Fille",
           "Fille","Garçon","Fille","Fille","Garçon","Fille","Garçon","Garçon","Fille","Garçon","Fille","Fille",
           "Garçon","Garçon","Fille","Garçon","Fille","Garçon","Garçon","Garçon","Garçon","Garçon","Garçon","Garçon",
           "Garçon","Garçon","Garçon","Garçon","Fille","Fille","Garçon","Fille","Garçon","Fille","Fille","Fille",
           "Garçon","Fille","Fille","Garçon","Fille","Garçon","Garçon","Fille","Garçon","Garçon","Fille","Garçon",
           "Fille","Garçon","Garçon","Fille","Fille","Garçon","Fille","Garçon","Fille","Garçon","Garçon","Fille",
           "Garçon","Garçon","Fille","Fille","Garçon","Fille","Garçon","Garçon","Fille","Garçon","Fille","Fille",
           "Garçon","Fille","Garçon","Fille","Garçon","Fille","Garçon","Fille","Garçon","Garçon","Fille","Garçon",
           "Garçon","Fille","Garçon","Garçon","Garçon","Fille","Garçon","Garçon","Fille","Fille","Fille","Fille",
           "Fille","Fille","Garçon","Fille","Fille","Fille","Garçon","Fille","Fille","Garçon","Garçon","Garçon",
           "Garçon","Garçon","Fille","Fille","Garçon","Fille","Fille","Garçon","Fille","Fille","Garçon","Fille",
           "Fille","Fille","Garçon","Fille","Fille","Fille","Garçon","Fille","Garçon","Garçon","Fille","Garçon",
           "Garçon","Garçon","Garçon","Fille","Garçon","Fille","Garçon","Fille","Garçon","Fille","Fille","Garçon",
           "Fille","Fille","Garçon","Fille","Garçon","Garçon","Fille","Fille","Garçon","Fille","Garçon","Fille",
           "Garçon","Fille","Fille","Garçon","Garçon","Garçon","Garçon","Garçon","Fille","Garçon","Fille","Garçon",
           "Fille","Garçon","Fille","Fille","Garçon","Garçon","Garçon","Fille","Fille","Fille","Garçon","Garçon",
           "Garçon","Fille","Fille","Fille","Garçon","Fille","Garçon","Garçon","Fille","Garçon","Fille","Garçon",
           "Fille","Garçon","Fille","Garçon","Fille","Fille","Garçon","Fille","Garçon","Fille","Garçon","Fille")

while 1 == 1:
    age = int(input("Entrez votre age à la conception : "))
    mois = int(input("Entrez le mois de conception en chiffre : "))
    if age not in range(18,46) and mois not in range(1,13):
        print("Veuillez indiquer un age compris entre 18 et 45 ans et un mois compris entre 1 et 12")
    else:
        print("Ce sera un.e "+ Matrice[((age-18)*12)+mois-1])
        print("Félicitations")