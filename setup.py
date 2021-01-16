# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdata-abdi", # the name that you will install via pip
    version="1.0",
    author="Abdrehim Nuru",
    author_email="shifaabdrehim80@email.com",
    description="My first trial of testing a package",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/abdishifa234/lambdata-abdi",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)