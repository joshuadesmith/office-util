# gencopies.py
# Written by Josh Smith
# Creates copies of a pdf file

import shutil, os

wdir = 'C:\\Users\\joshua\\Desktop\\'
fnl = 'filelisting.txt'
ftbc = 'base.pdf'
dest = 'Quigley\\'


# Get file paths for fnl and ftbc
def get_filepaths():
	base = wdir + ftbc
	listing = wdir + fnl
	return base, listing


# Get path to destination folder
def get_dest_path():
	return wdir + dest


# Generates copies of the specified PDF with names in array
def generate_copies(file_to_copy, file_names):
	dest_path = get_dest_path()
	for name in file_names:
		dest = dest_path + name.strip() + '.pdf'
		shutil.copy(file_to_copy, dest)


# Generates documents given TEXT FILE with file name listing
def generate_documents(base_file, text_file):
	names = open(text_file, mode='r', encoding='utf-8').readlines()
	generate_copies(base_file, names)


# Main Module
if __name__ == "__main__":
	print('Generating copies of base.pdf')
	base, listing = get_filepaths()
	generate_documents(base, listing)
	print('Process complete')