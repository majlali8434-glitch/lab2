phrase = input("Entrez une phrase : ")


print(f"Longueur : {len(phrase)}")             
print(f"Majuscules : {phrase.upper()}")        
print(f"Minuscules : {phrase.lower()}")        
print(f"Inversion : {phrase[::-1]}")           


inverse = phrase[::-1]
if phrase.lower() == inverse.lower():
    print("C'est un palindrome !")
else:
    print("Ce n'est pas un palindrome.")