#!/bin/sh

#Installation Python, pip and tk
sudo apt-get install python
sudo apt-get install python-pip
sudo apt-get install python-tk

#Uprgade pip before installation
sudo pip install --upgrade pip

#Installation required libs
sudo python -m pip install -U pip setuptools
sudo python -m pip install matplotlib
sudo pip install Pillow
sudo pip install reportlab
