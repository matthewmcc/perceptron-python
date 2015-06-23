from __future__ import print_function

import sys, math

from perceptronMod import *
from csvparse import *

global EPOCHS, LEARNING_RATE, confusionMatrix
EPOCHS = 1

# Perceptron function
def perceptron(data):
	# Gets globals needed for calculation
	global EPOCHS, LEARNING_RATE, confusionMatrix

	# Data row len
	dw = len(data[0])
	weights = [0.0] * (dw)

	for i in range(0, EPOCHS):
		print("\rIteration ->", i + 1, end="")
		sys.stdout.flush()
		for dl in range(1, len(data)):
			# Get data row and inserts the bias at front
			row  = data[dl][:dw - 1]

			row.insert(0, "-1")

			# Target output
			y = int(data[dl][dw - 1])

			output = calculateOutput(weights, row)
			err = errCal(y, output)
			deri = sigmoidDerivaive(output)

			# Calculates confusion matrix
			confusionMatrix = confusionMatrixUpdate(output, confusionMatrix, y)

			# Updates weights
			for j in range(0, len(weights)):
				weights[j] += LEARNING_RATE * err * deri * float(row[j])

	return weights

# Checks input for correct length
if len(sys.argv) != 3 or sys.argv[0] == "help":
	print("Usage: <File name> <Learning rate a>")
	sys.exit(0)

data = open_csv(sys.argv[1])

LEARNING_RATE = float(sys.argv[2])
print("Learning Rate =", LEARNING_RATE)
print("Data length =", len(data) - 1)
print("Iterations =", EPOCHS)

# confusionMatrix = [tp, tn, fp, fn]
confusionMatrix = [0] * 4

# Runs the perceptron
weights = perceptron(data)

# Funky pretty print stuff
print("\r", " " * 100, end="")
print("\r", end="")

# Legit weight print stuff
printWeights(data[0], weights)

# Prints confusion matirx
printConfusionMatrix(confusionMatrix)