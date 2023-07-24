from setuptools import setup,find_packages
from typing import List

HYPEN_E_DOT ='-e .'

def find_requirements(file_path:str)->List[str]:
    '''This Function returns the list of requirements for the project'''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[i.replace("\n","") for i in requirements]
        #This list comprehension replaces the \n that comes after every line automatically with a white space in the requirements.txt file

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            #The -e . is not a package for installation. So, it is removed here.
    return requirements



setup(
    Name = "End To End Ml Project",
    version = '0.0.1',
    author = "Pranjal",
    author_email= "Pranzalkhadka1@gmaial.com",
    packages = find_packages(),
    install_requires = find_requirements('requirements.txt')
)