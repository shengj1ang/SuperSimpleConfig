from setuptools import setup
from setuptools import find_packages


VERSION = '2023.12.13'


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
    entry_points={
        'console_scripts': [
            'supersimpleconfig=SuperSimpleConfig:main',
        ],
    },
    zip_safe=False,
)