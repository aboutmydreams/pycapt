import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pycapt",
    version="1.0.16",
    author="aboutmydreams",
    author_email="aboutmydreams@163.com",
    description="a library that processes verification codes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aboutmydreams/pycapt",
    packages=setuptools.find_packages(),
    classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
)