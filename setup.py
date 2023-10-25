from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    """
    This function will return a list of requirements
    """
    requirements=[]
    with open('requirements.txt') as file_obj:
        requirements = file_obj.readlines()  # read a txt file add /n in every line break
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name="mlproject",
    version="0.0.1",
    author="Huy",
    author_email="huylearndata@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)