from setuptools import setup

with open("Readme.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setup(
    name='friendlier-json',
    version='2.0a1',
    packages=['friendlier-json'],
    url='https://github.com/py-alpha-wolf/friendlier-json',
    license='MIT',
    author='Leo B.',
    author_email='bernerdoodle@outlook.de',
    description='Friendlier Json simplifies your handling of a Json for storing data enormously.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6"

)
