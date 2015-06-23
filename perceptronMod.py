from __future__ import print_function
import math, sys

# Calculates sigmoid of input
## Sigmoid ->
## -> The S-shaped curve of the large intestine where the colon joins the rectum.
## Hilarious!!
sigmoidFunction = lambda x: 1.0 / (1.0 + math.exp( - x))

# Calculates derivative of sigmoid
sigmoidDerivaive = lambda x: x * (1.0 - x)

# Error Calculation, going lambda crazy. This ones probably over the top. I should...
# ...really be studying
errCal = lambda y, output: y - output

# Calculates the expected output of a given state
def calculateOutput(weights, data_instance):
	input_weights_sum = 0
	BIAS_INDEX = 0
	for x in range(1, len(data_instance) - 1):
		input_weights_sum += (weights[x] * float(data_instance[x]))

	input_weights_sum += (weights[BIAS_INDEX] * float(data_instance[BIAS_INDEX]))

	return sigmoidFunction(input_weights_sum)

# Prints the weights and there column name in sorted order by weights.
def printWeights(names, weights):
	header = ("Attribute Name", "Weight Value")

	# names.insert(0, "BIAS")
	bias = weights[0]
	del weights[0]

	pp = zip(names, weights)

	# Sorts the list by the weight values then reverses it
	pp = reversed(sorted(pp, key = lambda x: x[1]))

	# List comprehension to change tuples to lists
	pp = [list(e) for e in pp]
	pp.insert(0, ("BIAS", bias))
	pp.insert(0, header)

	# Funky pretty print stuff
	for row in pp:
		print("{: >20} {: >20}".format(*row))

# Updates the confusion matrix of confusion. Confusioned much?
def confusionMatrixUpdate(output, confusionMatrix, y):
	# confusionMatrix = [tp, tn, fp, fn]
	if output > 0.5:
		if y == 1:
			confusionMatrix[0] += 1
		else:
			confusionMatrix[2] += 1
	elif output < 0.5:
		if y == 0:
			confusionMatrix[1] += 1
		else:
			confusionMatrix[3] += 1
	return confusionMatrix

# Prints confusion matrix of confusion. Perceptron is no longer confused.
def printConfusionMatrix(confusionMatrix):
	print("\nConfusion Matrix")
	print('1', '\t', '0')
	print(confusionMatrix[0], '\t', confusionMatrix[2], '\t', "<- Classified as Positive Emotion")
	print(confusionMatrix[3], '\t', confusionMatrix[1], '\t', "<- Classified as Negative Emotion")
	print("Classification Errors\t", confusionMatrix[2] + confusionMatrix[3])
	print("Correct Classifications\t", confusionMatrix[0] + confusionMatrix[1])
	print("Percent Correct\t\t", (float(confusionMatrix[0]) + float(confusionMatrix[1])) / 
		(float(sum(confusionMatrix))) * 100)

### Attribute Ranker Functions ###

# Checks if attribute ranker is complete, with a lambda for kicks.
isComplete = lambda x: sys.exit("Complete") if x == 1 else None

# Halts perceptron if all values in list equal zero
def onlyZeroRemaing(avgList, data):
	for num in avgList:
		if not num == 0:
			return data
	sys.exit("Remaining attributes are all zeros")

# Zips and maps the absolute weights
def listAvg(absWeights):
	#l = len(absWeights[0]) - 1
	#avg = lambda n: n / l
	#return map(avg, map(sum, absWeights[1:]))
	return absWeights[1:]

# Pretty print for attribute ranker
def printHighestAttribute(itemCount, name, remaining):
	# Funky pretty print stuff
	print("\r", " " * 100, end="")
	print("\r", end="")

	pp = [name, str(remaining) + " items remaining"]
	print("#", itemCount, "->", "{: >10} {: >20}".format(*pp))
