from setuptools import find_packages,setup
from typing import List

def get_requirments()->List[str]:
    """
    This function will return list of requirments
    "-e ." is refering to this setup .py file 
    
    """
    requirment_lst:List[str]=[]
    try:
        with open ('requirments.txt','r') as file:
            #This will read line from requirments from requirments.txt file

            lines=file.readlines()

            #process each line

            for line in lines:
                requirment=line.strip()
                ## ignore empty lines and -e.

                if requirment and requirment!='-e .':
                    requirment_lst.append(requirment)

    except FileNotFoundError:
        print("README.txt File not found !")

    return requirment_lst

setup(

    name="NetworkSecurity",
    version="0.0.1",
    author="Dhananjay",
    author_email="dhananjaymane2125@gmail.com",
    packages=find_packages(),
    install_requires=get_requirments()
)


    
