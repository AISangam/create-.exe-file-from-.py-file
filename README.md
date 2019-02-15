# create-.exe-file-from-.py-file  

![exe](https://user-images.githubusercontent.com/35392729/52805258-35679600-30ac-11e9-8614-151d234fda6c.png)  

This code is focusssed on creating the exe file from the python file using the cx_Freeze library.  

## Why exe is needed.  

There may be case when some one needs the python code in the form of executable file for some reason. It may be possible that some one has made an app using python programming language and wants to launch its .exe version also. In all such cases, conversion from.py to .exe becomes important.

## How to create the exe file  

### To create the exe file please execute the below steps:
<ul>
  <li><strong>Step 1</strong>: You have the python installed in your system. I am writing these steps with respect to windows. So please visit https://www.python.org/downloads/ to download the version of the python you want and install it. During installation, please install it in the custom location in c drive as well as please donot forget to add it to the path. Have a look at the screenshot.  

![creating_exe_step1](https://user-images.githubusercontent.com/35392729/52865166-f8f67180-3161-11e9-874c-71a8dfdb2ecf.png) </li>

<li><strong>Step 2</strong>: Install cx_freeze  by using the below command.
  
  ```
  pip3 install cx_Freeze
  ```
  Execute the above command at <strong>C:\Python3.x\Scripts</strong> location in command prompt where x denotes the version of python which you have downloaded.</li>
  
<li><strong>Step 3</strong>: Install all the dependencies that you need to run your python script by using pip in the location C:\Python3.x\Scripts by exectuing the command in the command prompt.
  
  ```
  pip3 install -r requirement.txt
  ```
  Please see the requirement.txt for this project in this repository.</li>
  
<li><strong>Step 4</strong>:Please create a file called setup.py and you have another file which is having your code. Please excetute the below commands in file setup.py
  
  ```
  import sys
from cx_Freeze import setup, Executable

# <added>
import os.path
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
print(PYTHON_INSTALL_DIR)
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')
# </added>
build_exe_options = {'packages': ['numpy','pandas','tkinter'],"include_files": [os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
         ]}

setup(
    name = "reading_file_pandas",
    version = "0.1",
    description = "reading_file_pandas",
    options = {"build_exe": build_exe_options},
    executables =[Executable('reading_file_pandas.py')] # this is the name of the file which is having your code
    )
 ```
 </li>
 <li><strong>Step 5</strong>: Please run the below command to create the exe file.
  
  ```
  py -2 setup.py build
  or
  py -3 setup.py build
  ```
  
  Please remember that both the setup.py as well as file having your code must be in the same path/directory.
  </li>
  </ul>

    
