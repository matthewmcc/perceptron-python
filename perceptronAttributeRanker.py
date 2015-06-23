from __future__ import print_function

import sys, math

from perceptronMod import *
from csvparse import *

global EPOCHS, LEARNING_RATE, itemCount

# Minimum of 2 epochs required
EPOCHS = 1
itemCount = 1

# Perceptron funciton
def perceptron(data):
	# Data row len
	dw = len(data[0])
 
 	# Gets globals needed for calculation
	global LEARNING_RATE, EPOCHS, itemCount

	weights = [0.0] * (dw)
	absWeights = []
	row = []

	for i in range(0, EPOCHS):
		print("\rIteration ->", i + 1, end="")
		sys.stdout.flush()
		for dl in range(1, len(data)):
			# Get data row and inserts the bias at front
			row = data[dl][:dw-1]
			row.insert(0, -1)

			# Target output
			y = int(data[dl][dw - 1])

			output = calculateOutput(weights, row)
			err = errCal(y, output)
			deri = sigmoidDerivaive(output)

			# Updates weights
			for j in range(0, len(weights)):
				weights[j] += LEARNING_RATE * err * deri * float(row[j])

		# Adds new iteration of weights to absWeights
	 	if i == 0:
	 		absWeights = map(abs, weights)
	 		for z in range(0, len(weights)):
	 			absWeights[z] = [absWeights[z]]
	 	else:
	 		absW = map(abs, weights)
	 		for i in range(0, len(weights)):
	 			absWeights[i].append(absW[i])

	# Gets list with averages of all weights
	avgList = listAvg(absWeights)
	lm = max(avgList)

	# Finds index of highest weight
	ri = avgList.index(lm)

	printHighestAttribute(itemCount, data[0][ri], len(data[0]) - 2)

	itemCount += 1

	# Removes highest weighted column from list
	for row in data:
		del row[ri]

	# Halts if complete
	isComplete(len(data[0]))

	# Halts if only zeros remain
	return onlyZeroRemaing(avgList, data)

# Checks input for correct length
if len(sys.argv) != 3 or sys.argv[0] == "help":
	print("Usage: <File name> <Learning rate a>")
	sys.exit(0)

data = open_csv(sys.argv[1])

LEARNING_RATE = float(sys.argv[2])
print("Learning Rate =", LEARNING_RATE, "Perceptron Iterations")
print("Data length =", len(data) - 1)

# Runs perceptron until usefull data reaches zero
while True:
	data = perceptron(data)
