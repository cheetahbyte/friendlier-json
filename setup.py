from setuptools import setup
import setuptools

with open('README.md', 'r') as fh:
    long = fh.read()

setup(
    name='friendlier json',
    version='0.0.1.1',
    author='Leo Breuer',
    autor_email='admin@bernerdev.de',
    description='A small package that turns a .json into a database !',
    long_description=long,
    long_description_content_type='text/markdown',
    url='https://github.com/py-alpha-woelfchen/friendlier-json',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',

)
