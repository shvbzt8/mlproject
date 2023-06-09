from setuptools import find_packages, setup
from typing import List


HYPHEN_E_DOT = '-e .'
def get_requirements(path) -> List[str]:
    '''
    this func will return the list of requirements'''
    requiremetns = []
    with open(path) as file_obj:
        requirements = file_obj.readlines()
        [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Shivam',
    author_email='sb1kaka@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'))
