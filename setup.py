from setuptools import setup,find_packages
from typing import List

#Declaring variables for setup function
PROJECT_NAME="housing-predictor"
VERSION="0.0.1"
AUTHOR="Harsh Tidke"
DESCRIPTION="This is first Machine Learning project"
REQUIRMENTS_FILE_NAME="requirements.txt"


### Description: this function is going to return list of requiremts mentioned in the requirements.txt file
### Return : This function is going to return a list which contains names of libraries mentioned in requirements.txt file 
def get_requirments_list()->List[str]: 
    with open(REQUIRMENTS_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")


setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=find_packages(),
install_requires=get_requirments_list()
)