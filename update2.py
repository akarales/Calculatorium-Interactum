import json
import os
import nbformat as nbf

# Define the correct order of subdirectories for each course
ordered_subdirs = [
    '01_lessons',
    '02_quiz_book',
    '03_reinforcement_workbook',
    '04_interactive_visualizations',
    '05_midterm_exam',
    '06_final_exam',
    '07_use_cases'
]

# Read the JSON file
with open('Calculatorium_interactum_courses.json', 'r') as f:
    data = json.load(f)

def create_lesson_template(course_name):
    nb = nbf.v4.new_notebook()
    
    nb['cells'] = [
        nbf.v4.new_markdown_cell(f"# Lesson Template for {course_name}"),
        nbf.v4.new_markdown_cell("## Lesson Content"),
        nbf.v4.new_code_cell("# Your lesson code here"),
        nbf.v4.new_markdown_cell("## Interactive Components"),
        nbf.v4.new_code_cell("# Code for interactive elements"),
        nbf.v4.new_markdown_cell("## Adaptive Learning Algorithm"),
        nbf.v4.new_code_cell(
            "# Placeholder for adaptive learning algorithm\n"
            "def adjust_difficulty(student_performance):\n"
            "    # Implement adaptive learning logic here\n"
            "    pass\n"
            "\n"
            "# Example usage:\n"
            "# current_difficulty = adjust_difficulty(previous_performance)"
        ),
        nbf.v4.new_markdown_cell("## Assessment"),
        nbf.v4.new_code_cell("# Assessment code here")
    ]
    
    return nb

def create_use_case_template(course_name):
    nb = nbf.v4.new_notebook()
    
    nb['cells'] = [
        nbf.v4.new_markdown_cell(f"# Use Case Template for {course_name}"),
        nbf.v4.new_markdown_cell("## Project Description"),
        nbf.v4.new_markdown_cell("Describe the real-world problem or scenario this project addresses."),
        nbf.v4.new_markdown_cell("## Concepts Applied"),
        nbf.v4.new_markdown_cell("List the key concepts from the course that are applied in this project."),
        nbf.v4.new_markdown_cell("## Implementation"),
        nbf.v4.new_code_cell("# Your implementation code here"),
        nbf.v4.new_markdown_cell("## Results and Analysis"),
        nbf.v4.new_markdown_cell("Discuss the results and their implications in the real-world context."),
        nbf.v4.new_markdown_cell("## Further Exploration"),
        nbf.v4.new_markdown_cell("Suggest ways to extend or modify this project for additional learning.")
    ]
    
    return nb

# Create directories and subdirectories
for course in data['courses']:
    # Create main course directory
    os.makedirs(course['directory'], exist_ok=True)
    print(f"Created main directory: {course['directory']}")
    
    # Create subdirectories in the specified order
    for subdir in ordered_subdirs:
        full_path = os.path.join(course['directory'], subdir)
        os.makedirs(full_path, exist_ok=True)
        print(f"  Created subdirectory: {full_path}")
    
    # Create Rule Key file as a text file
    rule_key_path = os.path.join(course['directory'], 'rule_key.txt')
    with open(rule_key_path, 'w') as rule_key:
        rule_key.write(f"Rule Key for {course['name']}\n\n")
        rule_key.write("List of functions and rules for this course:\n")
        rule_key.write("1. \n2. \n3. \n")  # Placeholder for actual rules
    print(f"  Created Rule Key: {rule_key_path}")

    # Create lesson template with adaptive learning algorithm
    template_nb = create_lesson_template(course['name'])
    template_path = os.path.join(course['directory'], '01_lessons', 'lesson_template.ipynb')
    with open(template_path, 'w') as f:
        nbf.write(template_nb, f)
    print(f"  Created lesson template with adaptive learning: {template_path}")

    # Create use case template
    use_case_nb = create_use_case_template(course['name'])
    use_case_path = os.path.join(course['directory'], '07_use_cases', 'use_case_template.ipynb')
    with open(use_case_path, 'w') as f:
        nbf.write(use_case_nb, f)
    print(f"  Created use case template: {use_case_path}")

    # Create placeholder for interactive visualizations
    viz_placeholder_path = os.path.join(course['directory'], '04_interactive_visualizations', 'dynamic_plots.py')
    with open(viz_placeholder_path, 'w') as viz_file:
        viz_file.write("# Placeholder for interactive visualizations\n")
        viz_file.write("# This will contain code for dynamic, interactive plots and diagrams\n")
    print(f"  Created visualization placeholder: {viz_placeholder_path}")

print("Course structure creation complete with numbered subdirectories!")