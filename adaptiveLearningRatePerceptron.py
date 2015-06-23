from __future__ import print_function

import sys, math

from perceptronMod import *
from csvparse import *

global BATCH_SIZE, MULTIPLIER, data

# Perceptron function
def perceptron(weights, confusionMatrix, startIndex, learningRate):
	# Gets globals needed for calculation
	global BATCH_SIZE, MULTIPLIER, data

	dIndex = startIndex

	# Runs the current perceptron for BATCH_SIZE rows from startIndex
	for x in range(0, BATCH_SIZE):
		# Get data row and inserts the bias at front
		row  = data[dIndex][:dw-1]
		row.insert(0, -1)

		# Target output
		y = int(data[dIndex][dw - 1])

		output = calculateOutput(weights, row)
		err = errCal(y, output)
		deri = sigmoidDerivaive(output)

		# Calculates confusion matrix
		confusionMatrix = confusionMatrixUpdate(output, confusionMatrix, y)

		# Updates weights
		for j in range(0, len(weights)):
			weights[j] += learningRate * err * deri * float(row[j])

		dIndex += 1
		# Checks if all data has been complete
		if dIndex > len(data) - 1:
			weights.append(confusionMatrix)
			break

	# Appends errors to the weights
	weights.append(confusionMatrix)
	return weights

# Checks input for correct length
if len(sys.argv) != 5 or sys.argv[0] == "help":
	print("Usage: <File name> <Learning rate a> <Batch size N> <Multiplier y>")
	sys.exit(0)

data = open_csv(sys.argv[1])

learningRate = float(sys.argv[2])
BATCH_SIZE = int(sys.argv[3])
MULTIPLIER = float(sys.argv[4])
print("Learning Rate =", learningRate)
print("Data length =", len(data) - 1)
print("Batch Size =", BATCH_SIZE)
print("Multiplier =", MULTIPLIER)

# Perceptron start index in the data
startIndex = 1

# confusionMatrix = [tp, tn, fp, fn]
confusionMatrix = [0] * 4

# Data row len
dw = len(data[0])
weights = [0.0] * (dw)

# Runs the perceptrons while there is still unused data
while startIndex < len(data) - 1:

	# Runs the 3 versions of the perceptrons, collecting weights and errors as return values...
	# ...where [:] passes by value not by reference
	w1 = perceptron(weights[:], confusionMatrix[:], startIndex, learningRate)
	w2 = perceptron(weights[:], confusionMatrix[:], startIndex, MULTIPLIER * learningRate)
	w3 = perceptron(weights[:], confusionMatrix[:], startIndex, (1 / MULTIPLIER) * learningRate)

	# Finds the amount of errors made by the perceptrons
	err1 = w1[len(w1) - 1][2] + w1[len(w1) - 1][3]
	err2 = w2[len(w2) - 1][2] + w2[len(w2) - 1][3]
	err3 = w3[len(w3) - 1][2] + w3[len(w3) - 1][3]

	# Finds the smallest error
	if err1 <= err2 and err1 <= err3:
		confusionMatrix = w1.pop()
		weights = w1
	elif err2 <= err3:
		learningRate = MULTIPLIER * learningRate
		confusionMatrix = w2.pop()
		weights = w2
	else:
		learningRate = (1 / MULTIPLIER) * learningRate
		confusionMatrix = w3.pop()
		weights = w3

	startIndex += BATCH_SIZE
	# print(learningRate)

# Funky pretty print stuff
print("\r", " " * 100, end="")
print("\r", end="")

# Legit weight print stuff
weights.pop()
printWeights(data[0], weights)

# Prints confusion matirx
printConfusionMatrix(confusionMatrix)
