perceptron.py

Use the perceptron learning algorithm, based on a sigmoid activation function and squared error minimization to learn and evaluate a perceptron that predicts the polarity attribute (i.e., the sentiment) based on the other attributes in the data, in an incremental learning set-up. To do this, you need to incrementally read in each row of data, make a prediction based on the current weights of the perceptron and the attribute values in that row, compare the prediction to the actual polarity in the data, and then update the weights of the perceptron accordingly, based on the gradient descent update rule. You program also needs to keep track of how many classification errors are made during this process.

The learning rate for the updates should be a user-specified parameter for your program. Initially, the values of all weights should be set to 0. There also needs be a bias input whose value is always -1, so there are 101 weights in total.

The program should be called Perceptron and it must be possible run it from the command-line on the given data file (in compressed or uncompressed form, that's up to you). The first commandline argument must be the name of the data file and the second command-line argument must be the learning rate.

Your program should output the final set of 101 weights, obtained after all the input data has been processed, as well as the number of classification errors encountered during the training process. Note that the first weight should be the bias weight.

perceptronAttributeRanker.py

It is interesting to consider the weight that each of the attributes receives in the classification process. We can easily verify that the attributes with the largest weights (in absolute terms) are the most important ones. To this end, make a new version of your code, called PerceptronAttributeRanker, which implements the following steps:

Learn perceptron as in Part 1, but also keep track of average absolute value of each weight. That is, after every update, record the absolute weight of each input and average the weights at the end of learning.
Output the name of attribute with largest average absolute weight and output total number of correct classifications for the perceptron.
Remove attribute with largest average absolute weight from data (see below for a trick to this).
If at least one attribute remains, go to step 1.
In Step 2, the attribute name and the number of correct classifications should be output in one line, separated by a space. There is no need to output the complete set of weights for this part of the assignment.

This process will output a ranking of the attributes, and you will be able to see that the attributes with the largest weight have the most impact on the accuracy of the learning algorithm.

learningRatePerceptron.py

The standard perceptron learning algorithm is based on a fixed learning rate for the weight updates. This is often not ideal. In this part of the assignment your task is to make a new version of the Perceptron class, called AdaptiveLearningRatePerceptron, that implements a simple heuristic for modifying the learning rate during the learning process. This class should accept two additional parameters so that it can be called from the command-line as follows:

java AdaptiveLearningRatePerceptron <file name> <learning rate α> <batch size N> <multiplier γ>

How can we adapt the learning rate in a reasonable manner? We can do this based on observed classification performance, decreasing or increasing the learning rate if necessary. The idea is to always maintain three perceptron models rather than just one, trained with three different learning rates:  \alpha _{cur}, \gamma \times \alpha _{cur}, and \frac{1}{ \gamma } \times \alpha _{cur}, where initially \alpha _{cur} is set to the \alpha value provided by the user. We can then monitor the number of classification errors of these three perceptrons for a little while to figure out which one works best; thus we effectively "race" the perceptrons to identify the best one.

To this end, after N training examples have been seen, where N is specified by the user, we compare the number of classification errors of the three perceptrons and identify that learning rate that yields the lowest number of errors. Let's call this best learning rate \alpha _{new}. It assigned either  \alpha _{cur}, \gamma \times \alpha _{cur}, or \frac{1}{ \gamma } \times \alpha _{cur} (i.e. select the learning rate with the fewest classification errors). Then we make two copies of the perceptron associated with this learning rate and discard the two worse perceptrons, thus obtaining, again, three perceptrons, all with identical weights, just as at the start of the learning process. This enables us to restart the racing process with learning rates  \alpha _{new}, \gamma \times \alpha _{new}, or \frac{1}{ \gamma } \times \alpha _{new}, and we can again monitor these three perceptrons' accuracy until we have seen another N examples. At that point the best perceptron and corresponding learning may change again.

This process of adapting the learning rate based on observed performance is repeated until all the data has been processed.

As in Part 1 of this assignment, the final output should be the set of 101 weights associated with the adaptive perceptron (that is, perceptron using the best weights), and the number of classification errors obtained with the adaptive strategy.

By choosing appropriate values for the batch size (e.g., 10,000) and multiplier (e.g., 1.5) you should be able to decrease the number of classifications errors compared to the perceptron with a single, fixed learning rate (as implemented by Perceptron from Part 1). Make sure ALL the code you submit is your own code. Also, make sure your code is well-documented with lots of comments. Assignment submission is online, as usual.