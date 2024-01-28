from setuptools import setup
 




PROJECT_NAME = "housing-predictor"
VERSION = "0.0.1"
AUTHOR = "Himanshu Kumar Chaturvedi"
DESCRIPTION = "This is My First Project with full setup"
PACKAGES = ["housing"]
REQUIREMENTS_FILE_NAME= "requirements.txt"

def get_requirements_list():
        """
        this function will return list of reuirements mention in requirements.txt file

        return this function is going to return a list which contain name of library mention in requirements.txt
        """
        with open(REQUIREMENTS_FILE_NAME) as requirement_file:
            return requirement_file.readlines()

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=PACKAGES,
    install_requires=get_requirements_list()

)