Matrice = ("Une Fille","Un Garçon","Une Fille","Un Garçon","Un Garçon","Un Garçon","Un Garçon","Un Garçon","Un Garçon","Un Garçon","Un Garçon","Un Garçon",
           "Un Garçon","Une Fille","Un Garçon","Une Fille","Une Fille","Un Garçon","Un Garçon","Une Fille","Un Garçon","Un Garçon","Une Fille","Une Fille",
           "Une Fille","Un Garçon","Une Fille","Un Garçon","Un Garçon","Un Garçon","Un Garçon","Un Garçon","Un Garçon","Une Fille","Un Garçon","Un Garçon",
           "Un Garçon","Une Fille","Une Fille","Une Fille","Une Fille","Une Fille","Une Fille","Une Fille","Une Fille","Une Fille","Une Fille","Une Fille",
           "Une Fille","Un Garçon","Un Garçon","Une Fille","Un Garçon","Une Fille","Une Fille","Un Garçon","Une Fille","Une Fille","Une Fille","Une Fille",
           "Un Garçon","Un Garçon","Un Garçon","Une Fille","Un Garçon","Un Garçon","Une Fille","Une Fille","Une Fille","Un Garçon","Un Garçon","Une Fille",
           "Un Garçon","Une Fille","Une Fille","Un Garçon","Un Garçon","Une Fille","Un Garçon","Une Fille","Un Garçon","Un Garçon","Une Fille","Un Garçon",
           "Une Fille","Un Garçon","Une Fille","Un Garçon","Une Fille","Un Garçon","Une Fille","Un Garçon","Une Fille","Un Garçon","Un Garçon","Un Garçon",
           "Un Garçon","Un Garçon","Un Garçon","Un Garçon","Un Garçon","Une Fille","Un Garçon","Une Fille","Une Fille","Un Garçon","Une Fille","Une Fille",
           "Une Fille","Une Fille","Un Garçon","Un Garçon","Une Fille","Un Garçon","Une Fille","Une Fille","Un Garçon","Une Fille","Un Garçon","Un Garçon",
           "Un Garçon","Un Garçon","Un Garçon","Une Fille","Une Fille","Un Garçon","Une Fille","Un Garçon","Une Fille","Une Fille","Un Garçon","Une Fille",
           "Une Fille","Un Garçon","Une Fille","Une Fille","Un Garçon","Une Fille","Un Garçon","Un Garçon","Une Fille","Un Garçon","Une Fille","Une Fille",
           "Un Garçon","Un Garçon","Une Fille","Un Garçon","Une Fille","Un Garçon","Un Garçon","Un Garçon","Un Garçon","Un Garçon","Un Garçon","Un Garçon",
           "Un Garçon","Un Garçon","Un Garçon","Un Garçon","Une Fille","Une Fille","Un Garçon","Une Fille","Un Garçon","Une Fille","Une Fille","Une Fille",
           "Un Garçon","Une Fille","Une Fille","Un Garçon","Une Fille","Un Garçon","Un Garçon","Une Fille","Un Garçon","Un Garçon","Une Fille","Un Garçon",
           "Une Fille","Un Garçon","Un Garçon","Une Fille","Une Fille","Un Garçon","Une Fille","Un Garçon","Une Fille","Un Garçon","Un Garçon","Une Fille",
           "Un Garçon","Un Garçon","Une Fille","Une Fille","Un Garçon","Une Fille","Un Garçon","Un Garçon","Une Fille","Un Garçon","Une Fille","Une Fille",
           "Un Garçon","Une Fille","Un Garçon","Une Fille","Un Garçon","Une Fille","Un Garçon","Une Fille","Un Garçon","Un Garçon","Une Fille","Un Garçon",
           "Un Garçon","Une Fille","Un Garçon","Un Garçon","Un Garçon","Une Fille","Un Garçon","Un Garçon","Une Fille","Une Fille","Une Fille","Une Fille",
           "Une Fille","Une Fille","Un Garçon","Une Fille","Une Fille","Une Fille","Un Garçon","Une Fille","Une Fille","Un Garçon","Un Garçon","Un Garçon",
           "Un Garçon","Un Garçon","Une Fille","Une Fille","Un Garçon","Une Fille","Une Fille","Un Garçon","Une Fille","Une Fille","Un Garçon","Une Fille",
           "Une Fille","Une Fille","Un Garçon","Une Fille","Une Fille","Une Fille","Un Garçon","Une Fille","Un Garçon","Un Garçon","Une Fille","Un Garçon",
           "Un Garçon","Un Garçon","Un Garçon","Une Fille","Un Garçon","Une Fille","Un Garçon","Une Fille","Un Garçon","Une Fille","Une Fille","Un Garçon",
           "Une Fille","Une Fille","Un Garçon","Une Fille","Un Garçon","Un Garçon","Une Fille","Une Fille","Un Garçon","Une Fille","Un Garçon","Une Fille",
           "Un Garçon","Une Fille","Une Fille","Un Garçon","Un Garçon","Un Garçon","Un Garçon","Un Garçon","Une Fille","Un Garçon","Une Fille","Un Garçon",
           "Une Fille","Un Garçon","Une Fille","Une Fille","Un Garçon","Un Garçon","Un Garçon","Une Fille","Une Fille","Une Fille","Un Garçon","Un Garçon",
           "Un Garçon","Une Fille","Une Fille","Une Fille","Un Garçon","Une Fille","Un Garçon","Un Garçon","Une Fille","Un Garçon","Une Fille","Un Garçon",
           "Une Fille","Un Garçon","Une Fille","Un Garçon","Une Fille","Une Fille","Un Garçon","Une Fille","Un Garçon","Une Fille","Un Garçon","Une Fille")

while 1 == 1:
    age = int(input("Entrez votre age à la conception : "))
    mois = int(input("Entrez le mois de conception en chiffre : "))
    if age not in range(18,46) and mois not in range(1,13):
        print("Veuillez indiquer un age compris entre 18 et 45 ans et un mois compris entre 1 et 12")
    else:
        print("Ce sera "+ Matrice[((age-18)*12)+mois-1])
        print("Félicitations")

