# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="my-lambdata-ndow33", # the name that you will install via pip
    version="1.4",
    author="Nate Dow",
    author_email="ndow33@gmail.com",
    description="A short description",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    license="MIT",
    url="https://github.com/ndow33/lambdata-ndow33",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)