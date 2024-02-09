from setuptools import find_packages,setup
from typing import List
#create a function 

#crearing a global constant 
Hypen_e_dot = '-e .'

def get_requirements(file_path:str)->List[str]:

## This function will return a list of requriements

    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        if Hypen_e_dot in requirements:
            requirements.remove(Hypen_e_dot)
    
    return requirements
    
#meta data for our porject 
setup(
name = 'machinelearning_project',
version = '0.0.1',
author = 'ahamedrefai',
author_email= 'refai.ahamed06@gmail.com',
packages= find_packages(),
install_requires = get_requirements('requirements.txt')
)