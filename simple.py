import torch
from parse import parse
from n_gram import n_gram, table, pred

# Loss for bigram model: abt 2.42
# Loss for trigram model: abt 1.86
# (Negative log likelihood-loss)

n = 3
filename = "nilsholg.txt"
data = parse(filename)
d = {}
for element in data:
    d = n_gram(n, d, element)
probs = table(n, d, data.vocab())

def generate(m:int, s:str):
    if len(s)<n:
        s="\n"*n
    for k in range(m):
        y_int=pred(n, probs, s, data.vocabSize())
        s+=data.itos(y_int)
    return s