nombre1 = float(input("Entrez le premier nombre :"))
nombre2 = float(input("Entrez le deuxieme nombre :"))
operation = input("choisissez l'operation (+,-,*,/):")

if operation =="+":
    resultat = nombre1 + nombre2
elif operation == "-":
    resultat = nombre1 - nombre2
elif operation == "*":
     resultat = nombre1 * nombre2
elif operation == "/":
    if nombre2 != 0:
     resultat = nombre1 /nombre2
else:
     resultat="Erreur (dividion pae zéro)"
else:
    resultat="opérateur invalide"
 print(f"Résultat :{resultat}")
 expect ValueError
  print("Erreur : Veuillez entrer des nombres valides.")