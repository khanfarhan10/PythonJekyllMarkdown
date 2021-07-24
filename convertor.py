"""
python convertor.py
Converts Jupyter Notebooks to Markdown for Jekyll
Make sure you have jupyter installed and or ipython configured early
"""
import os
import re

INPUT_FOLDER = os.path.join(os.getcwd(),"Sample_Notebooks")

NOTEBOOK_CONVERTOR = True # True
IMAGE_PATH_FIXER = True
replaceImgCaption = True
PrependPath = "/assets/images/"
removeSpaces = True
debug = False
ignoreDone = False



lst = os.listdir(INPUT_FOLDER)


if NOTEBOOK_CONVERTOR:
    for each in lst:
        run_nb = False
        # os.system('ls -l')
        if each.endswith(".ipynb"):
            FilePath  = os.path.join(INPUT_FOLDER ,each)
            # ExecutionCommand  = f"ipython nbconvert --to markdown {FilePath}"
            if ignoreDone:
                md_path = each.replace(".ipynb",".md")
                if not os.path.exists(md_path):
                    run_nb = True
            else:
                run_nb = True
            if run_nb:
                ExecutionCommand  = f"jupyter nbconvert --to markdown {FilePath}"
                os.system(ExecutionCommand)
       
""" 
################### FIX THE PATHS TO IMAGES

![png](Custom-Colour-Splash-Effect-Improved_files/Custom-Colour-Splash-Effect-Improved_40_1.png)
Convert these to "/assets/images/Arduino_1.jpg"
"""

if IMAGE_PATH_FIXER and not ignoreDone:
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
                    new_data_path = os.path.join(PrependPath,data_path)
                    new_img_line = f"![{data_caption}]({new_data_path})"
                    new_data.append(new_img_line)
                else:
                    if removeSpaces :
                        if not (e=="\n" or e=="" or e.strip()==''):
                            new_data.append(e)
                    else:
                        new_data.append(e)
            NewFilePath  = os.path.join(INPUT_FOLDER ,str("Fixed_")+ each)
                    
            if debug==True:
                for d in new_data:
                    print(d)
            with open(NewFilePath, 'w') as f:
                for i in new_data:
                    f.write('%s'%i)
	

print("Finished Processing!")


