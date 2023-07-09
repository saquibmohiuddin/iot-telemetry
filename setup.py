from setuptools import setup, find_packages



def get_requirements(file_path:str = 'requirements.txt')-> list:
    """Reads requirements.txt and returns list of requirements"""
    with open(file_path) as f:
        requirements = f.read().splitlines()
        requirements = [requirement for requirement in requirements if not requirement.startswith('-e')]
        return requirements


    
VERSION = '0.1.0'
AUTHOR = 'Saquib Mohiuddin Siddiqui'

setup(
    name='iot-sensor',
    version=VERSION,
    author=AUTHOR,
    author_email='saquib.mohiuddin@hotmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)
    
    