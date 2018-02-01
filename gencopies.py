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

wdir = os.path.dirname(os.path.realpath(__name__))
listing_txt = os.path.realpath('filelisting.txt')
base_pdf = os.path.realpath('base.pdf')
copy_dest = os.path.realpath('copies')


# Generates documents given TEXT FILE with file name listing
def generate_copies():
	names = open(listing_txt, mode='r', encoding='utf-8').read().splitlines()
	for name in names:
		dest = copy_dest + '\\' + name + '.pdf'
		shutil.copy(base_pdf, dest)


# Main Module
if __name__ == "__main__":
	print('Generating copies...')
	generate_copies()
	print('Complete')