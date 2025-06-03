import os
import sys

# Print current directory and files for debugging
print("Current directory:", os.getcwd())
print("Files in directory:", os.listdir())

# Try to run the main.py file
try:
    exec(open('main.py').read())
except Exception as e:
    print(f"Error running main.py: {e}")
