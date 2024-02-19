from setuptools import find_packages, setup
from typing import List

HYPHEN = '-e .'

def get_requirements_list(filename:str) -> List[list]:
    """
    This function will return the list of requirements
    """
    requirements = []
    with open(filename) as f:
        requirements = f.readlines()
        requirements = [r.replace("\n","") for r in requirements] 

    if HYPHEN in requirements:
        requirements.remove(HYPHEN)
    
    return requirements




setup(
    name='NewmlProject',
    version='1.0.0',
    author='Kamal',
    author_email='bikram66871@gmail.com',
    description='Newml Project',
    packages=find_packages(),
    install_requires= get_requirements_list('requirements.txt')
)
