# How was the Neural Network made?
1. Take a very large corpus of sentences (I used Books).
2. Create a CSV file with this data:
Encrypted_sentence | Plaintext | Encryption method

For each sentence in the large corpus, randomly encrypt it with an encryption method that Ciphey can decrypt. And then create the CSV file above.

Next, add more onto the CSV file. Specifically:
* Length of text
* Range of letters / numbers (if the text is abc, it only contains the range "3". We can even one-hot encode this. This is because some encodings only use 2/10/12/14 letters)
* Puncuation used

Train the neural network using this data. The logic is as follows:
* Length of text - hashes follow specific lengths
* Range of letters - encodings often have a limited alphabet. For example, binary has a range of 2 (0 and 1). Base 10 has a range of 10, and so on.
* Puncuation used - A lot of encoding / hashing algorithms do not use puncuation. If puncuation is used, it is more likely to be encrypted (no science to back this up, logically it makes a slight bit of sense)

When we input unknown text to the neural network, it will return a softmax (probability) distribution of what it thinks it is.
If the unknown text is exactly 256bits long, it is likely to be a SHA256 hash and so on. 
We use this probability table to determine what encryptions to try first. We might try BASE64, but if that fails we try the _family_. In our case, the family is called _basic encodings_.
If the family fails, we move onto the 2nd most likely family and so on.

# Future updates
- [ ] Add the use of an "=" sign into the trianing so ciphey can identify bases easier
- [ ] Maybe also spaces? Cause bases don't use spaces, and neither do hashes?
- [ ] A much, much larger dataset / corpusq
- [ ] Check for puncuation too. Sometimes encryptions use puncuation whereas other encodings don't.

# Dataset ideas
I need to develop a larger corpus of data, and I've decided to create my own dataset. The dataset will contain:
* The entirety of the English wikipedia
* All Reddit comments: https://www.reddit.com/r/datasets/comments/3bxlg7/i_have_every_publicly_available_reddit_comment/
* British National Corpus
* https://datasets.quantumstat.com/
Then, use chi squared on the Reddit comments to only select English looking comments.

Should be a good dataset :)

I might even upload the crypto dataset that Ciphey uses too to Kaggle.
