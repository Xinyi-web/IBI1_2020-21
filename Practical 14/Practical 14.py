import re
import os
import matplotlib.pyplot as plt
import xml.dom.minidom
from xml.dom.minidom import parse

# I find it hard for me to eliminate the redundancy, so I discussed and wrote this method with my classmates

#use the common codes to read and parse the xml.
DOMTree = xml.dom.minidom.parse("go_obo(1)(1)(1)(1).xml")
collection = DOMTree.documentElement
terms = collection.getElementsByTagName("term")

#set up a dictionary to store
dict = {}
#get the text of id in every term "original father"
for term in terms:
    id_1 = term.getElementsByTagName('id')[0].childNodes[0].data
    dict[id_1] = []
#get the text of is_a in the term "original son"
for term in terms:
    id = term.getElementsByTagName('id')#this can't be omitted
    is_a = term.getElementsByTagName('is_a')
    for ia in is_a:
        dict[ia.firstChild.data].append(id[0].firstChild.data)

#the function that count the childnodes
def counter(Input):
    for i in Input:
        if i not in list:
            list.append(i)#add the new childnodes into list
            counter(dict[i])#use the recursion
    return len(list)#I didn't mention the "len()" at first, so I can't get the expected results

#the function that used to see whether the id is related & calculate the childnodes number
def counter2(Input2):
    global list
    for term in terms:
        defstr = term.getElementsByTagName('defstr')[0].firstChild.data
        id_x = term.getElementsByTagName('id')[0].childNodes[0].data#get the id information
        #identify whether this id is a related gene
        if Input2 in defstr:
            if dict[id_x] != 0:
                n = counter(dict[id_x])
    return n

list=[]
DNAs=counter2('DNA')
print('the number of childnodes of DNA is:',str(DNAs))
list=[]
RNAs=counter2('RNA')
print('the number of childnodes of RNA is:',str(RNAs))
list=[]
protein1=counter2('Protein')
list=[]
protein2=counter2('protein')
proteins=protein2+protein1
print('the total childnodes number of protein is:',str(proteins))
list=[]
carbohydrate1=counter2('carbohydrate')#choose carbohydrate
list=[]
carbohydrate2=counter2('Carbohydrate')
carbohydrates=carbohydrate1+carbohydrate2
print('the total childnodes number of carbohydrate is:',str(carbohydrates))

#draw the plot 
sizes=[DNAs,RNAs,proteins,carbohydrates]
labels = ['DNA','RNA','Protein','Carbohydrate']
explode = (0,0.1,0,0.05)
plt.title('The number of Childnodes of DNA,RNA,Protein,and Carbohydrate')
plt.pie(sizes,explode=explode,labels=labels,labeldistance = 1.1,autopct = '%1.1f%%',shadow = True,startangle = 90)

plt.show()
