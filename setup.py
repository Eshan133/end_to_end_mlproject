from typing import List
from setuptools import find_packages, setup

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements] #when reading line, python will also read \n in a new line, removing that

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT) #when reading line, python will also read `-e .` in a new line, removing that


setup(
    name= 'end_to_end_mlproject',
    version='0.0.1',
    author='Ishan',
    author_email='ishan.maharjan5@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)

