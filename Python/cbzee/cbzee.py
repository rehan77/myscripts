# importing required modules 
import os 
from zipfile import ZipFile

def get_all_file_paths(directory): 

	# initializing empty file paths list 
	file_paths = [] 

	# crawling through directory and subdirectories 
	for root, directories, files in os.walk(directory): 
		for filename in files: 
			# join the two strings in order to form the full filepath. 
			filepath = os.path.join(root, filename) 
			file_paths.append(filepath) 

	# returning all file paths 
	return file_paths		 

def main():

	#Path to the folder of which subfolders/files needs to be individually zipped
    root_dir = os.curdir
    print(root_dir)
    #Listing all the subfolders/files inside the root_dir
    for dir in os.listdir(root_dir):
        #Getting full subfolderpath along with subfoldername of current subfolder
        directory = os.path.join(root_dir, dir)

        #Calling function to get all file paths in the current subfolder
        file_paths = get_all_file_paths(directory) 

        print('Zipping "' + dir + '"...')

        # writing files to a zipfile and storing them in the root_dir itself
        with ZipFile(directory + '.cbz','w', allowZip64=True) as zip: 
            # writing each file one by one 
            for file in file_paths: 
                zip.write(file, os.path.basename(file)) 

        print('"' + dir + '" zipped successfully!')		 

if __name__ == "__main__": 
	main() 