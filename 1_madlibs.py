#  on va creer un mini projet 
# qui s'appelle Madlibs 
'''
Madlib est un genre de contes ou d'histoires dans lesquels le lecteur doit remplacer des mots par des
autres pour en faire une histoire différente à chaque lecture. Pour cela, il a besoin de plusieurs
mots et phrases que l'on peut trouver sur internet.
Dans ce mini-projet, nous allons utiliser Python pour programmer cette application. Nous allons
donc créer un programme qui permettra au lecteur de choisir un thème (par exemple : "Voyage" ou "
Aventure") et de définir les mots et phrases correspondants. Le programme affichera ensuite ces
phrases avec les mots remplacés par le lecteur.

'''

# string concatenation (aka how to put strings together)
#  suppose we want to create a string that says "subscribe"

youtuber = 'my chanel'

#  a few ways to do this

# print( ' subscribe to' + youtuber)
# print('subscribe to {}'.format(youtuber))
# print(f"subscribe to {youtuber}")


adj = input('Adjective :')
verbe1 = input("Verbe : ")
verbe2 = input("Verbe : ")

famous_person = input("Famous person :")

madlib = f"""Computer programming is so {adj}! It makes me so excited all the time becuase \n
I love to {verbe1}. Stay hydrated and {verbe2} like you are {famous_person}!"""

print(madlib)