# lagerlof_0 
is a character-level language model based on the novel *Nils Holgerssons underbara resa genom Sverige* (eng: *The wonderful adventures of Nils*).
## Bigram model
The *bigram.py* file "trains" a bigram model by simply conting all the occuring bigrams in the novel. The loss (NLL) over the entire corpus is about 5.9.
## One layer feedforward neural network
The ambition with this one is to achieve similar performance as with the bigram model, but instead taking a deep learning approach. Because of the nature of a one layer model, the loss is expected to be similar to the bigram model. 