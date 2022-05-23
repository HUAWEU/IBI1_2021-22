<<<<<<< HEAD
from xml.dom.minidom import parse
import xml.dom.minidom
import numpy as np
import matplotlib.pyplot as plt
DOMTree = xml.dom.minidom.parse("Go_obo.xml")
collection = DOMTree.documentElement
terms = collection.getElementsByTagName("term")
num_term = terms.length
print("The total number of terms:" + str(num_term))


def num_parent(go):  # Calculate the total childNodes of each term.
    global dic
    n = len(parent[go])
    for b in range(0, n):
        dic[parent[go][b]] = 1
    for subgo in parent[go]:
        num_parent(subgo)
    return len(dic.keys())


parent = {}
translation = []
num_childNotes = []
num_translations = []
for term in terms:  # Create a dictionary where the id of terms is key and a blank list which will contain childNodes.
    Id = term.getElementsByTagName('id')[0]
    parent[Id.childNodes[0].data] = []

for term in terms:  # Filling the blank lists with all the childNodes.
    Id = term.getElementsByTagName('id')[0]
    is_a = term.getElementsByTagName('is_a')
    for i in range(0, is_a.length):
        a = term.getElementsByTagName('is_a')[i]
        parent[a.childNodes[0].data].append(Id.childNodes[0].data)

for term in terms:  # To find terms associate with translation.
    Id = term.getElementsByTagName('id')[0]
    defstr = term.getElementsByTagName('defstr')[0]
    if "translation" in defstr.childNodes[0].data:
        translation.append(Id.childNodes[0].data)

for term in terms:
    dic = {}
    Id = term.getElementsByTagName('id')[0]
    num_childNotes.append(num_parent(Id.childNodes[0].data))

for tra in translation:
    dic = {}
    num_translations.append(num_parent(tra))

num1 = num_childNotes
num2 = num_translations
plt.boxplot(num1,
            vert=True,
            whis=1.5,
            patch_artist=True,
            meanline=True,
            showbox=True,
            showcaps=True,
            showfliers=True,
            notch=False
            )
plt.ylabel('Number of ChildNodes')
plt.xlabel('Terms')
plt.title('Distribution of ChildNodes across terms')
plt.show()

plt.boxplot(num2,
            vert=True,
            whis=1.5,
            patch_artist=True,
            meanline=True,
            showbox=True,
            showcaps=True,
            showfliers=True,
            notch=False
            )
plt.ylabel('Number of ChildNodes')
plt.xlabel('Terms')
plt.title("Distribution of ChildNodes across terms associated with 'translation'")
plt.show()
# The 'translation' terms contain, on average, a small number of child nodes than the overall Gene Ontology.
print("The 'translation' terms contain, on average, a small number of child nodes than the overall Gene Ontology.")
=======
from xml.dom.minidom import parse
import xml.dom.minidom
import numpy as np
import matplotlib.pyplot as plt
DOMTree = xml.dom.minidom.parse("Go_obo.xml")
collection = DOMTree.documentElement
terms = collection.getElementsByTagName("term")
num_term = terms.length
print("The total number of terms:" + str(num_term))


def num_parent(go):
    global dic
    n = len(parent[go])
    for b in range(0, n):
        dic[parent[go][b]] = 1
    for subgo in parent[go]:
        num_parent(subgo)
    return len(dic.keys())


parent = {}
translation = []
num_childNotes = []
num_translations = []
for term in terms:
    Id = term.getElementsByTagName('id')[0]
    parent[Id.childNodes[0].data] = []

for term in terms:
    Id = term.getElementsByTagName('id')[0]
    is_a = term.getElementsByTagName('is_a')
    for i in range(0, is_a.length):
        a = term.getElementsByTagName('is_a')[i]
        parent[a.childNodes[0].data].append(Id.childNodes[0].data)

for term in terms:
    Id = term.getElementsByTagName('id')[0]
    defstr = term.getElementsByTagName('defstr')[0]
    if "translation" in defstr.childNodes[0].data:
        translation.append(Id.childNodes[0].data)

for term in terms:
    dic = {}
    Id = term.getElementsByTagName('id')[0]
    num_childNotes.append(num_parent(Id.childNodes[0].data))

for tra in translation:
    dic = {}
    num_translations.append(num_parent(tra))

num1 = num_childNotes
num2 = num_translations
plt.boxplot(num1,
            vert=True,
            whis=1.5,
            patch_artist=True,
            meanline=True,
            showbox=True,
            showcaps=True,
            showfliers=True,
            notch=False
            )
plt.ylabel('Number of ChildNodes')
plt.xlabel('Terms')
plt.title('Distribution of ChildNodes across terms')
plt.show()

plt.boxplot(num2,
            vert=True,
            whis=1.5,
            patch_artist=True,
            meanline=True,
            showbox=True,
            showcaps=True,
            showfliers=True,
            notch=False
            )
plt.ylabel('Number of ChildNodes')
plt.xlabel('Terms')
plt.title("Distribution of ChildNodes across terms associated with 'translation'")
plt.show()
# The 'translation' terms contain, on average, a small number of child nodes than the overall Gene Ontology.
print("The 'translation' terms contain, on average, a small number of child nodes than the overall Gene Ontology.")
>>>>>>> e22e09b592cc8a054107ad38ad83d7f407d9cd31
