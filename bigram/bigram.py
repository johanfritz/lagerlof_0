import torch
import matplotlib.pyplot as plt
file="/home/johanfritz/Dokument/Python/github/lagerlof_0/nilsholg.txt"
list=[]
with open(file, "r") as file:
    for letter in file:
        list.append(letter)
dictionary={} #this keeps track of all the bigrams in the corpus, and their respective counts in key-value pairs: (bigram)->count
for element in list:
    for k in range(len(element)):
        bigram=(element[k-1], element[k])
        dictionary[bigram]=dictionary.get(bigram, 0) + 1
letters=[] #set of all the letters in the corpus
for element in dictionary:
    if not element[0] in letters:
        letters.append(element[0])
letters.sort() #ditto in alphabetical order
lettoind={} #key-value pairs mapping the letters to respective indicies: (letter)-> index
for k in range(len(letters)):
    lettoind[letters[k]]=k
indtolet={} #(index)-> letter, as per above. 
for element in lettoind:
    indtolet[lettoind[element]]=element
mat=torch.ones((len(letters), len(letters)), dtype=torch.int) 
#mat is a lookup table for the counts in dictionary, 
#mat[i, j] contains the count of the bigram (i, j) as per 'dictionary'
for element in dictionary:
    mat[lettoind[element[0]], lettoind[element[1]]]=dictionary[element]
probs=torch.zeros_like(mat, dtype=torch.float)
#probs is the same concept at 'mat', but the elements are probabilities rather than counts.
for k in range(len(mat)):
    probs[k]=mat[k]/sum(mat[k])
# plt.imshow(probs)
# plt.show()
# s=" "
# ind=torch.multinomial(probs[0].float(), num_samples=1).item()
# while True:
#     s+=indtolet[ind]
#     ind=torch.multinomial(probs[int(ind)].float(), num_samples=1).item()
#     if s[-1]=="\n" and s[-2]=="\n":
#         break
# print(s)