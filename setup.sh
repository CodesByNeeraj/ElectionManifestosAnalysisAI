#!/bin/bash

# Create the virtual environment
python3 -m venv myenv

# Activate the virtual environment
source myenv/bin/activate

# Install dependencies from requirements.txt
pip install -r requirements.txt

# Run the setup_db script to create the Chroma vector database
python setup_db.py

echo "Environment setup complete and vector DB initialized!"
