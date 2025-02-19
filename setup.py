from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'

from typing import List

def get_requirements(file_path: str) -> List[str]:
    """
    This function reads a text file containing a list of Python package requirements and returns them as a list of strings.

    Parameters:
    file_path (str): The path to the text file containing the requirements.

    Returns:
    List[str]: A list of Python package requirements read from the file.

    Note:
    - The function removes any newline characters ('\\n') from each requirement.
    - If the file contains the special requirement '-e .' (HYPEN_E_DOT), it is removed from the list.
    """
    requirements = []

    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements



setup(
name = 'Flight_Price_Predictions',
version='0.0.1',
author="Grish Kumar Gupta",
author_email="gupta.grish03@gmail.com",
packages=find_packages(),
install_requires = get_requirements('requirements.txt')
)