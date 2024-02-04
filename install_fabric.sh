#!/bin/bash

# Install pip3
sudo apt-get update
sudo apt-get install -y python3-pip

# Install required dependencies
sudo apt-get install -y libffi-dev libssl-dev build-essential

# Install required Python packages with specific versions
pip3 install --upgrade pip
pip3 install pyparsing appdirs setuptools==40.1.0 cryptography==2.8 bcrypt==3.1.7 PyNaCl==1.3.0

# Install Fabric3 with a specific version
pip3 install Fabric3==1.14.post1
