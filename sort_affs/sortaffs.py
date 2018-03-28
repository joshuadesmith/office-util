import shutil, os


dict_txt = os.path.realpath('dict.txt')
sort_dir = os.path.realpath('sortdir')


# Generates a dictionary that contains folders that correspond to trust names
def generate_dict():
	ext_dict = {}
	for line in open(dict_txt, mode='r', encoding='utf-8').read().splitlines():
		tokens = line.split(':')
		ext_dict[tokens[0]] = tokens[1]
	return ext_dict


# Gets the destination path to be used by shutil.copy
def get_destination_filepath(ext_dict, filename):
	trust = filename.split(' - ')[1].split()[0]
	if trust in ext_dict:
		return sort_dir + '\\' + ext_dict[trust] + '\\' + filename


# Gets file paths of all files to be sorted
def get_files_to_sort():


# Main Module
if __name__ == "__main__":
	# Start here
	ext_dict = generate_dict()
