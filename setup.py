from setuptools import setup, find_packages
from typing import List
from os import path
E_dot="-e ."

def get_requirements(file_path: str) -> List[str]:
    """
    This function will return a list of requirements
    """
    requirements=[]

    with open(file_path, "r") as file:
        requirements = file.readlines()
        requirements=[req.strip() for req in requirements if req.strip()]
        if E_dot in requirements:
            requirements.remove(E_dot)
    return requirements



setup(
    name="ml_project",
    version="0.1.0",
    author="MMM",
    author_email="mannamodanmohan@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(path.join("requirement.txt")),

)