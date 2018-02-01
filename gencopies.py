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


# Get file paths for listing_txt and base_pdf
def get_filepaths():
	base = wdir + base_pdf
	listing = wdir + listing_txt
	return base, listing


# Get path to destination folder
def get_dest_path():
	return wdir + dest


# Generates copies of the specified PDF with names in array
def generate_copies(file_names):
	for name in file_names:
		dest = copy_dest + '\\' + name + '.pdf'
		shutil.copy(base_pdf, dest)


# Generates documents given TEXT FILE with file name listing
def generate_documents():
	names = open(listing_txt, mode='r', encoding='utf-8').read().splitlines()
	for name in names:
		dest = copy_dest + '\\' + name + '.pdf'
		shutil.copy(base_pdf, dest)


# Main Module
if __name__ == "__main__":
	print('Generating copies...')
	generate_documents()
	print('Complete')