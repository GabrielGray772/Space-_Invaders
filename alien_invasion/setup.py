from setuptools import setup, find_packages
from space_invaders import __version__

setup(
    name= "space_invaders",
    
    url="git@github.com:GabrielGray772/Space_Invaders.git",
    author= "GabrielGray772",
    author_email= "arcgabriel@gmail.com",
    
    install_requires = ["pygame>=2.5.0", "setuptools>=40.8.0"],
    entry_points ={
        "console_scripts": [ 
            "space_invaders=space_invaders:run_game"
        ]
    }
) 