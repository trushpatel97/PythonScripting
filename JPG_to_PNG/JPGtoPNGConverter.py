import sys
import os
from PIL import Image
#grab first and second argument from cmd
ImageArg= sys.argv[1]
OutputFolder = sys.argv[2]
#Check if new/exists, if not create
if not os.path.exists(OutputFolder):
	os.makedirs(OutputFolder)

for filename in os.listdir(ImageArg):
	img = Image.open(f'{ImageArg}{filename}')#its {ImageArg} because we are assuming the user will type the slash /
	clean_name = os.path.splitext(filename)[0]
	img.save(f'{OutputFolder}{clean_name}.png','png')
	#img.save(f'{ImageArg}{clean_name}.png','png')
	#print('all done!')
#loop through pictures,



#convert images to png


#save to the new folder