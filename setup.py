from setuptools import find_packages, setup
from typing import List

HYPHEN_E_D = "-e ."


def get_requirements(file_path: str) -> List[str]:
    """This function will return the list of requirements."""
    requirements = []

    with open(file_path, "r") as f:
        requirements = [line.strip() for line in f]

    if HYPHEN_E_D in requirements:
        requirements.remove(HYPHEN_E_D)

    return requirements


setup(
    name="mlproject",
    version="0.1.0",
    author="DIVYANG PANDEY",
    author_email="divyangpandeynitcalicut77@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)