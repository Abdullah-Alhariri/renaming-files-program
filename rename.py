from alive_progress import alive_bar
import shutil
import json
import time 
import sys
import os  

# 0) Getting command arguments 
if len(sys.argv) != 3:
    print("Usage: python rename.py <from folder> <new folder>")
    sys.exit(1)

fromFolder =  sys.argv[1]
toFolder = sys.argv[2]
dirPath = os.path.dirname(os.path.realpath(__file__))

# 1) Checking if there are files in fromFolder
for dirpath, dirnames, files in os.walk(f"{dirPath}/{fromFolder}"): 
    if not files: 
        print(f'No files found in "{fromFolder}" folder')
        sys.exit(1)

# 2) Checking if files folder exist else make them 
if not os.path.isdir(f"{dirPath}/{fromFolder}"):
    print(f'"{fromFolder}" folder not found')
    sys.exit(1)

# 2) removing toFolder folder if exist
if os.path.isdir(f"{dirPath}/{toFolder}"):
    shutil.rmtree(f"{dirPath}/{toFolder}") # removes "new" with all its contents 

# 3) Making toFolder folder
os.mkdir(f"{dirPath}/{toFolder}")

# 4) Saving every file in toFolder folder   
def getOptions(block): 
    info = open('options.json')
    result =  json.load(info)[block]
    return result

def formatFilename(fileName):
    charOptions = getOptions('charOptions')
    case = getOptions('case')

    for key, value in charOptions.items():
        fileName = fileName.replace(key, value)

    match case:
        case 'lower': 
            fileName = fileName.lower()
        case 'upper': 
            fileName = fileName.upper()
        case 'title': 
            fileName = fileName.title() 
        case 'capitalize': 
            fileName = fileName.capitalize()
            
    return fileName

for dir_path, dirnames, files in os.walk(f"{dirPath}/{fromFolder}"): 
    with alive_bar(len(files), dual_line=True, title='renaming') as bar:
        for index, file in enumerate(files):
            shutil.copy2(f'{dirPath}/{fromFolder}/{file}', f'{dirPath}/{toFolder}/{formatFilename(file)}')
            bar.text = f'-> renaming file: {file}, still {len(files) - index}/{len(files)} files to go'
            time.sleep(.2)
            bar()

print('Done! ???')
