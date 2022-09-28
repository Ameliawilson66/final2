#amelia wilson
#401
#28 septembre 2022

print("trouver le nombre de mots dans un texte")  # résumé du but de code au lecteur
word_count2 = str(input("écrit une/des phrase(s): "))  # le lecetur inscrit le nombre de mots à compter

#on créer une nouvelle fonction
def word_count(word_count2):
    number_word = len(word_count2.split())#l'ordinateur compte le nombre de mots
    return  number_word #return de nombre de mots
reponse = word_count(word_count2)
print(reponse)

