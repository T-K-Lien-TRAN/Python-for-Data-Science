# ft_package

A simple Python package developed for the 42 School
Python for Data Science Piscine.

## Description

This package provides a function to count the number
of occurrences of an element in a list.

## Installation

# 1. Go to your project directory
cd /home/thitran/Documents/Lien/Python_for_Data_Science/Python-0-Starting/ex09

# 2. Test the local package
python3 usage.py

# 3. Install the build tool
python3 -m pip install build

# 4. Build the package
python3 -m build

# 5. Check the distribution files
ls dist/

# 6. Install the package

The subject requires both installation methods to work.
Method A: Install the .whl file

        python3 -m pip install ./dist/ft_package-0.0.1-py3-none-any.whl

        You should see a success message similar to:
        Successfully installed ft_package-0.0.1

Method B: Install the .tar.gz file
        To verify the second method, uninstall and reinstall:
        python3 -m pip uninstall ft_package

        Then:
        python3 -m pip install ./dist/ft_package-0.0.1.tar.gz

# 7. Verify the installed package
python3 -m pip list
python3 -m pip show -v ft_package

# 8. Test from another directory
cd /tmp

python3 -c 'from ft_package import count_in_list; print(count_in_list(["toto", "tata", "toto"], "toto"))'

## Usage

```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto")) # output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu")) # output: 0