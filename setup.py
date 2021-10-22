from setuptools import setup, find_packages
import codecs
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

VERSION = '1.0.2'


# Setting up
setup(
    name="treesp",
    version=VERSION,
    author="Sidharth Parekh",
    author_email="sidharthparekh1@gmail.com",
    description="trees",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'preorder', 'postorder', 'inorder', 'trees'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)