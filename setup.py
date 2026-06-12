from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT='-e .' 

def get_requirements(file_path:str)->List[str]: ## List[str]says that the function will return a list of strings
    ''' this function will return a list '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readline()
        requirements=[req.replace('\n','') for req in requirements] ## to remove the \n

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT) ## We are removing it because it will automatically trigger so we do not want it inside our setup.py

    return requirements

setup(
    name='EndToEnd_ML_Project',
    version='0.0.1',
    author='Udeani',
    author_email='udeaniizu04@gmail.com',
    packages=find_packages(), ## This will search through the folders to find which ones have __init__.py. The folder will be treated as a package. Then it will build it and you will be able to import it anywhere you want
    install_requires= get_requirements('requirements.txt')## rather than putting in a list like this ['pandas','numpy','seaborn'], ecause we can have hundresds of packages

)