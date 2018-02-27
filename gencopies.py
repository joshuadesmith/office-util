# gencopies.py
# Written by Josh Smith
# Creates copies of a pdf file
#   1. Move PDF to be copied into the same directory as this file
#   2. Rename the PDF 'base.pdf'
#   3. List the desired file names for the copies in a file named filelisting.txt
#   4. run python gencopies.py
# 
# NOTE: ONLY TESTED ON WINDOWS OS

import shutil, os, argparse

listing_txt = os.path.realpath('filelisting.txt')
base_pdf = os.path.realpath('base.pdf')
copy_dest = os.path.realpath('copies')


# Generates documents given TEXT FILE with file name listing
def generate_copies(filename):
	file = os.path.realpath(filename)
	names = open(listing_txt, mode='r', encoding='utf-8').read().splitlines()
	for name in names:
		dest = copy_dest + '\\' + name
		shutil.copy(file, dest)


# Generates n duplicates of a file
def generate_dupes(filename, n):
	file = os.path.realpath(filename)
	for i in range(n):
		dest = copy_dest + '\\' + str(i) + '-' + filename
		shutil.copy(file, dest)


# Checks whether copy destination folder is empty
def check_dest_empty(dir):
	contents = os.listdir(dir)
	if contents:
		print("WARNING: copies directory already contains files:")
		for f in contents:
			print(' - ', f)
		ans = input("Would you like to continue? (Y/N): ")
		return ans.lower() == 'y'
	else:
		return True


# Check whether file to be copied exists


# Check whether or not the required files are in the working directory
def check_resources(filename, n):
	wdir = os.path.dirname(os.path.realpath(__name__))
	bp = wdir + filename
	fl = wdir + '\\filelisting.txt'
	cp = wdir + '\\copies'
	clear = True

	if not os.path.exists(bp):
		print("ERROR: ", filename, " not found")
		clear = False

	if not os.path.exists(cp):
		print("ERROR: copies directory not found")
		clear = False
	else:
		clear = check_dest_empty(cp)

	if n > 0:
		if not os.path.exists(fl):
			print("ERROR: filelisting.txt not found")
			clear = False

	return clear


# Main Module
if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Generate copies supa fast! By default, \'base.pdf\' is copied with names specified in \'filelisting.txt\'.')

	parser.add_argument('--filename', 
						help='specify a file to be copied', 
						action='store', 
						dest='filename', 
						default='base.pdf')

	parser.add_argument('--dupe', 
						help="duplicate the file N times and disregard \'filelisting.txt\'", 
						action="store", 
						dest="n", 
						type=int, 
						default=0)

	args = parser.parse_args()
	print(vars(args))
	if check_resources(args.filename, args.n):
		print('Generating copies...')
		#generate_copies()
		print('Complete')
	else:
		print("Exiting")