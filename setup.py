from setuptools import find_packages,setup
from typing import List

E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_object:
        requirements=file_object.readlines()
        requirements = [req.replace("\n","")for req in requirements]
        if E_DOT in requirements:
            requirements.remove(E_DOT)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Tsifeherana',
    author_email='razamimiranto@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)