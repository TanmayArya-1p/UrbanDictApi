from setuptools import setup, find_packages
import os



VERSION = '0.1'
DESCRIPTION = 'Unofficial API for the popular website-Urban Dictionary.'
with open("README.md" , "r") as r:
    LONG = r.read()

# Setting up
setup(
    name="UrbanDictAPI",
    version=VERSION,
    author="TanmayArya1-p",
    author_email="<tanmayarya2018@gmail.com>",
    description=DESCRIPTION,
    url='https://github.com/TanmayArya-1p/UrbanDictAPI',
    long_description=LONG,
    long_description_content_type='text/markdown',
    install_requires=['beautifulsoup4','requests'],
    
    keywords=['python', 'api' , 'API' , 'web-scraping'],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
)