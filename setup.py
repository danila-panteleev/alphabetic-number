import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="alphabetic-number",
    version="0.0.1",
    author="danila-panteleev",
    author_email="pont131995@gmail.com",
    description="Convert number to alphabetical from",
    long_description=long_description,
    url="https://github.com/arocketman/git-and-pip",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)