#!/usr/bin/python3.6


import argparse
import csv
import sys
import platform
import operator


#------------------
#
# OPTIONS
#
#------------------

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



#------------------
#
# FUNCTIONS
#
#------------------

def getVersion():
	print("Python version:")
	print(platform.python_version())


def readCsv():
	with open('list.csv', newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')




def write_csv():
	with open('list.csv', 'w') as outfile:
		writer = csv.writer(outfile)
		values = args.add
		writer.writerow(values)
	

def listValues():
	with open('list.csv') as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		for row in readCSV:
			print(row)


def cleanFile():
	f = open("list.csv", "w")
	f.truncate()
	f.close()


def returnSum():
	with open('list.csv') as csvfile:
		spamreader = csv.reader(csvfile)
		sum = 0
		for row in spamreader:
			for i in row:
				sum += int(i)
	print("La somme totale des valeurs insérées est de : ", sum)


def returnAverage():
	with open('list.csv') as csvfile:
		spamreader = csv.reader(csvfile)
		sum = 0
		total = 0
		for row in spamreader:
			for i in row:
				sum += int(i)
				total = total+1
	print("La moyenne des valeurs insérées est de : ", sum/total)


def returnMaxValue():
	with open("list.csv", "r") as f_input:
		lmax_row = []
		for row in csv.reader(f_input):
			row = map(int, row)
			lmax_row.append(max(row))
			lmax_row = str(lmax_row)
	print("La valeur maximum de la liste actuelle est : ", lmax_row)


def returnMinValue():
	with open("list.csv", "r") as f_input:
		lmin_row = []
		for row in csv.reader(f_input):
			row = map(int, row)
			lmin_row.append(min(row))
			lmin_row = str(lmin_row)
	print("La valeur minimum de la liste actuelle est : ", lmin_row)





#------------------
#
# PROGRAM
#
#------------------

# ADD VALUES IN CSV FILE

if args.add:
	readCsv()
	write_csv()


# SHOW PYTHON VERSION

elif args.version:
	getVersion()

# LIST VALUES
		
elif args.list:
	listValues()


#CLEAN CSV FILE

elif args.cut:
	cleanFile()


# RETURN MIN VALUE FROM CSV FILE

elif args.min:
	returnMinValue()


# RETURN MAX VALUE FROM CSV FILE

elif args.max:
	returnMaxValue()


# RETURN SUM FROM CSV FILE

elif args.sum:
	returnSum()


# RETURN AVERAGE FROM CSV FILE

elif args.moy:
	returnAverage()



### NOT WORKING YET ###

elif args.tri:
	with open('list.csv', mode='rt') as f, open('sorted.csv', 'w') as final:
		writer = csv.writer(final, delimiter='\t')
		reader = csv.reader(f, delimiter=',')
		sorted2 = sorted(reader, key=lambda row: (row))        	
		for row in sorted2:
			writer.writerow(row)		

# IF NO OPTION WAS SELECTED
else:
	print('Merci d\'entrer une option. Quel intérêt sinon? ')


