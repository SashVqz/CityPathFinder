#!/bin/bash

VENV_DIR=".venv"
echo "Creating the virtual environment in the $VENV_DIR folder..."
python3 -m venv $VENV_DIR

echo "Activating the virtual environment..."
source $VENV_DIR/bin/activate

echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt

echo "Virtual environment set up and dependencies installed!"
