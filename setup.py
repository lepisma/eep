#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("requirements.txt") as requirements_file:
    requirements = requirements_file.read().splitlines()

install_requires = [x.strip() for x in requirements if "git+" not in x]
dependency_links = [x.strip().replace("git+", "")
                    for x in requirements if "git+" in x]

setup(
    name="eep",
    version="0.1.0",
    description="Emacs style, point based string search-replace library for python",
    long_description=readme,
    author="Abhinav Tushar",
    author_email="abhinav.tushar.vs@gmail.com",
    url=
    "https://github.com/lepisma/eep",
    include_package_data=True,
    install_requires=install_requires,
    license="MIT",
    keywords="",
    dependency_links=dependency_links,
    packages=find_packages(exclude=["docs", "tests*"]))
