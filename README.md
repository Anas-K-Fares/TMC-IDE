# TMC-IDE

1) About:

This project was started to enable remote access and control of Test and Measurement (TMC) devices. The commands are sent over a low-level TCP network within the   local network. The commands get sent to a Linux based interface which reroutes the commands to a connected Test and Measurment device by leveraging the USBTMC       driver that comes packaged with Linux. All sections of this project were written in Python. 

The files are split in the following way. A server folder contains all the code necessary to host a server that handles the USBTMC communication. This code can only run on a Linux operating system to make use of the USBTMC driver that comes packaged with Linux. A Raspberry Pi can handle that job. The other two folders, Linux and Windows, contain the client applications that are used by the user to make contact with the server. Each folder contains a Command Line application, an IDE, and a Matlab script. All client applications serve the same purpose of controlling TMC devices but in different enviroments. The client applications can be run on Windows or Linux.

2) Installation:

  * Server Install:
  
  The requirements for the server installation are a version of Python 3 and an installation of the pyudev library.
  
  Run this pip command in a Terminal to install pyudev if an installation of Python 3 is present.
  
  >$ pip3 install pyudev
  
  On a clean install of Raspberry Pi OS (Desktop included), python comes prepackaged. Installing a newer version of Python might cause issues with using the pip       command so it is recommended that you don't
  
  * Linux and Windows:
  
  For both Linux and Windows client applications, a version of Python 3 is required and the following libraries are needed: PILLOW, matplotlib, and Numpy.
  
  To install the libraries on a linux system run:
  
  >$ pip3 install PILLOW
  
  >$ pip3 install matplotlib
  
  >$ pip3 install pyudev
  
  To install on Windows run the following in CMD:
  >\> py -m pip install PILLOW
  
  >\> py -m pip install matplotlib
  
  >\> py -m pip install pyudev
  
  Now you're all set to test the setup.
  
  3) Testing:
  
  On your server, run the following files by using the Terminal:
  
  >$ python3 rulesSetup.py
  
  >$ python3 Network_server.py
  
  On the client side run run this file for the console version, under the Console Variant folder: ($ for linux, > for windows)
  
  >$ python3 Network_client.py
  
  >\> py -3 Network_client.py
  
  Run this file to start TMC IDE, under the IDE folder: ($ for linux, > for windows)
  
  >$ python3 IDE_main.py
  
  >\> py -3 IDE_main.py
  
  Run this script through Matlab for the Matlab version, under the Matlab Variant folder: (under respective operating system folder)
  
  > Example_graph.m
  
  4) Console Syntax:
  
  lstmc is used to show all the TMC devices connected to the server to allow for multi-device control.
  >\>\>\> lstmc

  Once the device name is known, ruinning a command must be in the following format: device::command. For example:
  >\>\>\> usbtmc1::*IDN?
  
  A new command was added to the list of standard TMC commands which facilitates acquiring data points from an oscilliscope: iwav:data?. Using the standard         wav:data? on its own will not give you all of the data showing in the display. iwav:data? was crated to solve that issue.
  >\>\>\> usbtmc1::iwav:data?
  
  5) Common problems:
  
  * rulesSetup.py must be running while plugging or removing TMC devices, otherwise the list of devices connected will not be displayed correctly. If that happens just delete the file, devList, that gets created on the server side and make sure that rulesSetup.py is ruinning when plugging any TMC devices. 
  
  * Running an unknown command through the Console application (or the others) will unfortunately hang the network connection and Network_server.py has to be re-run.
  
  * If when running Network_server.py, error "OSError: [Errno 98] Address already in use" shows up. Close all instances of this file and try again after a short    period of time.
  
  
