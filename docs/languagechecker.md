# Language Checker Documentation

# Chi Squared
Chi squared is a metric for determining how closely a statisitical distribution of letters is to another statistical distribution.

In this case, we are examining how closely the distribution of letters in the text is to the distribution of English (e is the most popular letter etc).

The lower the number, the closer it is.

If Chi Squared is 1 standard deviation below the average, it is likely to be English.

# Check 1000 words
Sometimes the chi square score is _just_ outside of the accecptable range. For example, if the message contains a lot of mathematics the Chi squared score is off.

For this reason, if chi squared fails, the program quickly checks to see if **any** words in the decrypted text are in the top 1000 words of English.

This discludes single letter words, such as i or a. As they can appear randomly in text. However, 2 letter words such as "he" or "of" are likely to appear, but statisically less likely than a single letter word.

# Dictionary Checker
Once one of the 2 conditions (chi squared, check 1000 words) returns True, the program them enters dictionary mode.

Dictionary checker checks to see if 75% or more of the words contained in the decrypted text are in the English dictionary. This is a rather slow process. Hence why we check firstly with chi squared (which is very fast), and then with check 1000 words before we perform an exhaustive, much slower search to triple check.

# How does average work?
The language checker object is instanstiated and sent to parent classes, and then to sub-classes. To add up the averages (to create an average chi squared of the program) it uses the magic method `__add__`.