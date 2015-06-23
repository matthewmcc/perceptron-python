import zipfile, csv, StringIO, sys

# Reads csv file to a list, do you even lambda
csvRead = lambda f: list(csv.reader(f))

# Reads in the data from a file
def open_csv(filename):
	try:
		# Checks if data is in a .zip file
		if filename.endswith(".zip"):
			print(filename[:len(filename) - 4])

			zip_file = zipfile.ZipFile(filename)

			# Only opens the first file found in the zip archive, if this isn't a...
			# ...csv your going to have an error time
			f = zip_file.open(zip_file.namelist()[0], 'rU')

			return csvRead(f)
		else:
			with open(filename, 'rb') as f:
				return csvRead(f)
			

	# Error catch for file not found
	except IOError as (errno, strerror):
		print "I/O error({0}): {1}".format(errno, strerror), ":", filename
		sys.exit(0)


