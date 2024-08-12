import json
import os

# Define the correct subdirectories for each course
subdirs = ['lessons', 'quiz_book', 'reinforcement_workbook', 'midterm_exam', 'final_exam']

# Read the JSON file
with open('Calculatorium_interactum_courses.json', 'r') as f:
    data = json.load(f)

# Create directories and subdirectories
for course in data['courses']:
    # Create main course directory
    os.makedirs(course['directory'], exist_ok=True)
    print(f"Created main directory: {course['directory']}")
    
    # Create subdirectories
    for subdir in subdirs:
        full_path = os.path.join(course['directory'], subdir)
        os.makedirs(full_path, exist_ok=True)
        print(f"  Created subdirectory: {full_path}")
    
    # Create Rule Key file
    rule_key_path = os.path.join(course['directory'], 'rule_key.ipynb')
    with open(rule_key_path, 'w') as rule_key:
        rule_key.write('{"cells": [], "metadata": {}, "nbformat": 4, "nbformat_minor": 5}')
    print(f"  Created Rule Key: {rule_key_path}")

    # Create placeholder files in each subdirectory
    for subdir in subdirs:
        placeholder_path = os.path.join(course['directory'], subdir, '.gitkeep')
        with open(placeholder_path, 'w') as placeholder:
            pass  # Create an empty file
        print(f"  Created placeholder: {placeholder_path}")

print("Course structure creation complete!")