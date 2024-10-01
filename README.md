# 42_school_Piscine_Python_for_Datascience


# Python Requirements

    install:  

    pip:
        $ sudo apt update
        $ sudo apt install python3-pip

    virtualenv:
        $ python3 -m venv venv
            This will create the .venv directory if it doesn’t exist, and also create directories inside it containing a copy of the Python interpreter and various supporting files.

        run:  
            $ source venv/bin/activate  
        run:  
            $ deactivate  


# ft_package

A sample test package  

## Package Structure

### Scripts

    A python file which is run like python "myscript.py"  

### Package

    A directory full of python code to be imported

### Subpackage

    A smaller package inside a package

### Module

    A python file inside a package which stores the package code  

### Library

    Either a package, or a collection of packages

### Package diretory tree

    my_package/
        |-- simple_module.py
        |-- __init.py__

    * directory my_package - is a python package
    * file simple_module.py - contains all the package code
    * file __init__.py - marks this directory as a python package

### Documentation

    Helps users use your code  
    Document each:  
    * function
    * class
    * class method  

    Can be access by:
        $ help(package_name.function_name) 
    
#### Documentation Style

![Documentation Style](./package_doc.png)
![Package, subpackage and module documentation](./package_subpackage_module_.png)

    Command:  
        $ pyment -w -o numpydoc <function.py>  
            * -w -> overwrite file  
            * -o numpydoc -> output in NumPy style

## Step by step

    1 - Create a folder with the ackage name  

    2 - Create the following files inside this folder:  
        * init.py  
        * setup.py  
        * README.md  
        * LICENCE.txt  

### init.py file

    Importe the functions inside, so it is possible to access the functions just importing the package:  
        * import ft_package
    If the function is not in the file:
        * from ft_package import <function>

### setup.py


### Wheel (Binary distribution)

    Binary version of the code ready for publication.  Contein everything that python package managment nedds to know to install the package.

## Installation
  
    $ pip install wheel
    Into the package folder:  
        * wheel
            $ python setup.py bdist_wheel



you can install the package using pip  


# Pandas

    Install:  
        $ pip install pandas  

    Pandas funciona com data frames(Tabelas)  

## Main Functions

    * dataframe = pd.DataFrame()