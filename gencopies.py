# gencopies.py
# Written by Josh Smith
# Creates copies of a pdf file
# 	1. Move PDF to be copied into the same directory as this file
#	2. Rename the PDF 'base.pdf'
#	3. List the desired file names for the copies in a file named filelisting.txt
#	4. run python gencopies.py
# 
# NOTE: ONLY TESTED ON WINDOWS OS

import shutil, os

listing_txt = os.path.realpath('filelisting.txt')
base_pdf = os.path.realpath('base.pdf')
copy_dest = os.path.realpath('copies')


# Generates documents given TEXT FILE with file name listing
def generate_copies():
	names = open(listing_txt, mode='r', encoding='utf-8').read().splitlines()
	for name in names:
		dest = copy_dest + '\\' + name
		shutil.copy(base_pdf, dest)


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


# Check whether or not the required files are in the working directory
def check_resources():
	wdir = os.path.dirname(os.path.realpath(__name__))
	bp = wdir + '\\base.pdf'
	fl = wdir + '\\filelisting.txt'
	cp = wdir + '\\copies'
	clear = True
	if not os.path.exists(bp):
		print("ERROR: base.pdf not found")
		clear = False
	if not os.path.exists(fl):
		print("ERROR: filelisting.txt not found")
		clear = False
	if not os.path.exists(cp):
		print("ERROR: copies directory not found")
		clear = False
	else:
		clear = check_dest_empty(cp)
	return clear


# Main Module
if __name__ == "__main__":
	if check_resources():
		print('Generating copies...')
		generate_copies()
		print('Complete')
	else:
		print("Exiting")