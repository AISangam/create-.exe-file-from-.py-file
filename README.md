# create-.exe-file-from-.py-file  

![exe](https://user-images.githubusercontent.com/35392729/52805258-35679600-30ac-11e9-8614-151d234fda6c.png)  

This code is focusssed on creating the exe file from the python file using the cx_Freeze library.  

## Why exe is needed.  

There may be case when some one needs the python code in the form of executable file for some reason. It may be possible that some one has made an app using python programming language and wants to launch its .exe version also. In all such cases, conversion from.py to .exe becomes important.

## How to create the exe file  

### To create the exe file please execute the below steps:
<ul>
  <li>Step 1: You have the python installed in your system. I am writing these steps with respect to windows. So please visit https://www.python.org/downloads/ to download the version of the python you want and install it. During installation, please install it in the custom location in c drive as well as please donot forget to add it to the path. Have a look at the screenshot.  

![creating_exe_step1](https://user-images.githubusercontent.com/35392729/52865166-f8f67180-3161-11e9-874c-71a8dfdb2ecf.png) </li>

<li> Step 2: Install cx_freeze  by using the blow command.
  
  ```
  pip3 install cx_Freeze
  ```
  Execute the above command at <strong>C:\Python3.x\Scripts</strong> location in command prompt where x denotes the version of python which you have downloaded.</li>
  
  <li> Install all the dependencies that you need to run your python script by using pip in the location C:\Python3.x\Scripts by exectuing the command in the command prompt.
  
  ```
  pip3 install -r requirement.txt
  ```
  Please see the requirement.txt for this project in this repository.

    
