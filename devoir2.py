#Après plusieurs longues heures de travail, je dois dire que je n'ai pas les capacités pour faire ce devoir. 
#Je conteste un peu le fait qu'il faille fouiller sur des blogs obscures pour résoudre un travail universitaire. 

#coding: utf-8

import csv

fname = "concordia1.csv"
file = open(fname)

reader = csv.reader(file)


#Ci-dessous, une tentative de créer la variable longtitre qui n'a pas réussi. 
#longTitre = (len(fname[2]))
#print(longTitre)

#Ci-dessous, tentative réussie de faire la variable longtitre. 
for longtitre in reader:

   print(len(longtitre[2]))

   
   #tentative échouée de faire la variable type
#for type in reader:
   # if type[6] == "M"
   # "M" = "Maitrise"
    #print(type[6])
    #elif type[6] == "ph"
    #"ph" = Doctorat
    #print(type[6])
  
  #ci-dessous, une tentative de décoder les chiffres romains, un autre échec.
import re
s = 0;
a = dict();
b = dict();
r = "MMCMXCVIII"

a['CM'] = 900;
a['IX'] = 9;
a ['IV'] = 4;
a ['XL'] = 40;
a ['CD'] = 400;
a ['XC'] = 90;

b['M'] = 1000;
b['C'] = 100;
b['D'] = 500;
b['X'] = 10;
b['V'] = 5;
b['L'] = 50;
b['I'] = 1;
    
for key in a:
        if key in r: 
            r = re.sub(key,'',r)
            s+=a[key];
            
for key in b:
         s+= r.count(key) * b[key];
         
print(s)


for nbPages in reader:
    print(nbPages[5])
   
  #Pour finir, une tentative de créer un fichier csv, un autre échec. 
   
#ifile  = open("concordia1.csv", "rb")
#reader = csv.reader(ifile)
#ofile  = open("tconcordia1.csv", "wb")
#writer = csv.writer(ofile, delimiter='', quotechar='"', quoting=csv.QUOTE_ALL)

#for row in reader:
  #  writer.writerow(row)
    
    
    
#writer = csv.writer(file)


#print(writer.writerow( ("longTitre", "type", "nbPages") ))

