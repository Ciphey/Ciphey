Okay, imagine an (X, Y) plane. On this X, Y plane we have vectors like (10, 10), (0, 0), (9, 9) etc.

K-nearest neighbors says something like "the 3 nearest neighbors to (9, 0) should be clustered together as result ABC". 

KNN does not need to be trained, as data is just plotted onto a graph when it is called.

KNN does not use a 2-dimensional plane, but an x-dimensional hyper-plane. So each feature of the vector is a feature of the text. So we say like ("Contains the world Flag", "contains {", "contains }", "Is shorter than 10 chars") etc.

Each feature is a dimension, so KNN works in multi-dimensional space (you probably can understand this better than I can).

Now, when a user inputs their own text such as "CyberSoc{flag 1}" the KNN will place this near the cluster that returns "True, this is a flag".

This text the user inputted is turned into a feature vector as seen above, which means any similar vectors (other flags) will turn up as Positive.

KNN isn't really used for binary classification, but we can modify it to do so.

Becaus the vectors have high dimensions (many features), it is unlikely for "correct" vectors to mix with "incorrect" vectors. The more features we have, the kinda better accuracy we get (but eventually we can overfit which means no new vectors ever get classified as positive).

The way KNN works is also super fast. basically, to really dumb it down so i can write it down, we can say it returns positive if the vector is in the range (8, 8) or (10, 10) therefore (9, 9) returns true (but in the vectors we will have many features so it wont be as bad with the range)

Pros of KNN:
* User can easily add their own flag styles and 'train' (KNN isnt trained but you get the point) KNN instantly
* Super fast to use because its literally just comparing vectors to one another to see if they fall in the same range
* Can be used for binary classification (if we get the dataset right)
* No training time, because KNN isn't trained (which means its super fast for users to edit)
* Possible for the user to add their own flag styles to a text file (maybe json? or something) which will get converted with the KNN. So everytime a user loads up the KNN, they have their own "settings" file of custom built flags

Cons:
* You can't save a KNN model as you can't train it, which means everytime it runs it has to re-create itself. If the user adds their own flag styles and they add lots of it, converting their flag styles into the appropriate vectors will slow things down (but they need to add ALOT of flag styles)
* Not really meant for binary classification, but we can mod it to work
* The "negative" data will have to be like purely random, like it cant look like a flag at all. Cant use hashes as flags use that. Perhaps encrypted text from project gutenberg or something? Maybe with text like "{it was the dover road that lay}" as its unlikely to be a flag without something in front of it

Overall, KNN is rather fast and seems like a suitable candidate.
