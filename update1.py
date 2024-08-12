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
    
    # Remove old Jupyter notebook rule key if it exists
    old_rule_key_path = os.path.join(course['directory'], 'rule_key.ipynb')
    if os.path.exists(old_rule_key_path):
        os.remove(old_rule_key_path)
        print(f"  Removed old Rule Key notebook: {old_rule_key_path}")

    # Create Rule Key file as a text file
    rule_key_path = os.path.join(course['directory'], 'rule_key.txt')
    with open(rule_key_path, 'w') as rule_key:
        rule_key.write(f"Rule Key for {course['name']}\n\n")
        rule_key.write("List of functions and rules for this course:\n")
        rule_key.write("1. \n2. \n3. \n")  # Placeholder for actual rules
    print(f"  Created Rule Key: {rule_key_path}")

    # Create placeholder files in each subdirectory
    for subdir in subdirs:
        placeholder_path = os.path.join(course['directory'], subdir, '.gitkeep')
        with open(placeholder_path, 'w') as placeholder:
            pass  # Create an empty file
        print(f"  Created placeholder: {placeholder_path}")

print("Course structure creation complete!")