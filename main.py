#amelia wilson
#401
#28 septembre 2022

#on créer une nouvelle fonction
def word_count(str):
    print("trouver le nombre de mots dans un texte")#résumé du but de code au lecteur
    word_count = str(input("écrit une/des phrase(s): "))#le lecetur inscrit le nombre de mots à compter
    number_word = len(word_count.split())#l'ordinateur compte le nombre de mots
    phrase = print("le nombre de mots est: ", str(number_word))#le lecteur recoit le nombre de mots
    return phrase #return de nombre de mots
word_count(str)