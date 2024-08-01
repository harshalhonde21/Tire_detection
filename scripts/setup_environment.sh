#!/bin/bash

# Create a virtual environment in the project root directory
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
