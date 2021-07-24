"""
python convertor.py
Converts Jupyter Notebooks to Markdown for Jekyll
Make sure you have jupyter installed and or ipython configured early
"""
import os
import re
INPUT_FOLDER = os.path.join(os.getcwd(),"Sample_Notebooks")
IMAGE_PATH_FIXER = False
NOTEBOOK_CONVERTOR = True # True
replaceImgCaption = True
PrependPath = "/assets/images/"



lst = os.listdir(INPUT_FOLDER)

if NOTEBOOK_CONVERTOR:
    for each in lst:
        # os.system('ls -l')
        if each.endswith(".ipynb"):
            FilePath  = os.path.join(INPUT_FOLDER ,each)
            # ExecutionCommand  = f"ipython nbconvert --to markdown {FilePath}"
            ExecutionCommand  = f"jupyter nbconvert --to markdown {FilePath}"
            os.system(ExecutionCommand)
       
""" 
################### FIX THE PATHS TO IMAGES

![png](Custom-Colour-Splash-Effect-Improved_files/Custom-Colour-Splash-Effect-Improved_40_1.png)
Convert these to "/assets/images/Arduino_1.jpg"
"""

if IMAGE_PATH_FIXER:
    print("Shifting Notebook Image Paths : Prepending Paths to",PrependPath)
    for each in lst:
        # os.system('ls -l')
        if each.endswith(".md"):
            FilePath  = os.path.join(INPUT_FOLDER ,each)
            # ExecutionCommand  = f"ipython nbconvert --to markdown {FilePath}"
            
            with open(FilePath, 'r') as f:
                data = f.readlines()
            ImageMarkdownRegex = r"\!\[(\S+)\]\((\S+)\)"
            
            new_data = []
            for e in data:
                dataMatch = re.findall(ImageMarkdownRegex,e)
                if not dataMatch==[]:
                    print(dataMatch)
                    data_caption, data_path = dataMatch[0]
                    basepath = os.path.basename(data_path)
                    if replaceImgCaption:
                        data_caption = basepath
                    new_data_path = os.path.join(PrependPath,basepath)
                    new_img_line = f"![{data_caption}]({new_data_path})"
                    new_data.append(new_img_line)
                else:
                    new_data.append(e)
            with open(FilePath, 'w') as f:
                for i in new_data:
                    f.write('%s\n'%i)
	

print("Finished Processing!")


