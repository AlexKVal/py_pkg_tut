import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "example-pkg-alexkval",
    version = "0.0.2",
    author = "AleKVal",
    author_email = "alexkval@gmail.com",
    description = "An example package",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://packaging.python.org/tutorials/packaging-projects/",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
