#!/usr/bin/python3.6


import argparse
import csv
import sys
import platform
import operator



#
##
###
#### argparse launch options
###
##
#

parser = argparse.ArgumentParser(conflict_handler='resolve')
parser.add_argument("-v", "--version", help="Affiche la version de pyton", action="store_true")
parser.add_argument("-l","--list", help="Affiche le contenu de la liste", action="store_true")
parser.add_argument("-a","--add", nargs="+" ,type=int, help="Ajouter des éléments à la liste.Par exemple, “./NOM_Prenom_kholle_1.py -a 5 3”, ajoutera les chiffres 5 et 3 dans la liste")
parser.add_argument("-c", "--cut", help="Supprime tous les éléments de la liste", action="store_true")
parser.add_argument("-s", "--max", help="Affiche la valeur maximum contenue dans la liste", action="store_true")
parser.add_argument("-s", "--min", help="Affiche la valeur minimum contenue dans la liste", action="store_true")
parser.add_argument("-s", "--moy", help="Affiche la moyenne de tous les éléments dans la liste", action="store_true")
parser.add_argument("-s", "--sum", help="Affiche la somme de tous les éléments dans la liste", action="store_true") 
parser.add_argument("-t", "--tri", help="Trie la liste dans l’ordre croissant", action="store_true")
parser.add_argument("-t --desc", help="Trie la liste dans l’ordre décroissant", action="store_true")
args = parser.parse_args()




# FUNCTIONS

def write_csv():
	with open('list.csv', 'w') as outfile:
		writer = csv.writer(outfile)
		values = args.add
		writer.writerow(values)

def readAndPrint():
	with open('list.csv') as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		for row in readCSV:
			print(row)


def cleanFile():
	f = open("list.csv", "w")
	f.truncate()
	f.close()








# PROGRAM


if args.add:
	with open('list.csv', newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
		write_csv()


# SHOW PYTHON VERSION

elif args.version:
	print("Python version:")
	print(platform.python_version())


# LIST ELEMENT
		
elif args.list:
	readAndPrint()


#CLEAN CSV FILE

elif args.cut:
	cleanFile()


# RETURN MIN VALUE OF LIST IN CSV FILE

elif args.min:
	with open('list.csv') as csvfile:
		list = csv.reader(csvfile, delimiter=',')
		min_value = min(list)
		print(min_value)
		

elif args.max:
	print('z')



### NOT WORKING YET ###

elif args.tri:
	file = open('list.csv','r')
	thewriter = csv.reader(file, delimiter=',')
	sort = sorted(thewriter, key=operator.itemgetter(0))
	for eachline in sort:
		print (eachline)


# IF NO OPTION WAS SELECTED
else:
	print('Merci d\'entrer une option. Quel intérêt sinon? ')
