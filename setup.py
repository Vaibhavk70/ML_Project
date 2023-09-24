from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT="-e ."
def get_requirements(file_path:str)->List[str]:
    ''''
    this function will return the list of requirements
    Reads the entire file at the specified file path. The function returns all the text in the file as a string, if
    the file is empty it will return an empty string ("").
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("/n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements


setup(
name='ML_Project',
version='0.0.1',
author='Vaibhav',
author_email='vaibhavkharat10@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)