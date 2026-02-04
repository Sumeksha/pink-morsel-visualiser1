#!/bin/bash
set -e

# Create or activate venv
if [ -d "venv" ]; then
    source venv/Scripts/activate
else
    python -m venv venv
    source venv/Scripts/activate
fi

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Run tests
pytest test_app.py

if [ $? -eq 0 ]; then
    echo "All tests passed!"
    exit 0
else
    echo "Some tests failed."
    exit 1
fi
