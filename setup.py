from setuptools import setup
from setuptools import find_packages


VERSION = '2023.12.10'


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
    
setup(
    name='SuperSimpleConfig',  # package name
    version=VERSION,  # package version
    description='Reads user configuration files that written in an extremely simple way',  # package description
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/shengj1ang/SuperSimpleConfig',
    packages=find_packages(),
    zip_safe=False,
)