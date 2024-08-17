import json
import os
import nbformat as nbf
import subprocess

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

def create_rule_key_tex(course_name):
    latex_content = f"""
\\documentclass{{article}}
\\usepackage{{amsmath}}
\\usepackage{{amssymb}}

\\title{{Rule Key for {course_name}}}
\\author{{Calculatorium Interactum}}

\\begin{{document}}

\\maketitle

\\section{{List of Functions and Rules}}

\\begin{{enumerate}}
    \\item [Rule 1] Description of rule 1
    \\item [Rule 2] Description of rule 2
    \\item [Rule 3] Description of rule 3
    % Add more rules as needed
\\end{{enumerate}}

\\end{{document}}
"""
    return latex_content

# List of lessons for Foundations of Pre-Algebra
pre_algebra_lessons = [
    "01_introduction_to_pre_algebra",
    "02_whole_numbers_and_operations",
    "03_factors_and_multiples",
    "04_fractions_introduction",
    "05_fraction_operations",
    "06_decimals_and_percents",
    "07_negative_numbers_and_integers",
    "08_order_of_operations",
    "09_exponents_and_square_roots",
    "10_algebraic_expressions",
    "11_equations_and_inequalities",
    "12_ratios_and_proportions",
    "13_basic_geometry_concepts",
    "14_perimeter_area_and_volume",
    "15_coordinate_plane",
    "16_basic_statistics_and_probability",
    "17_problem_solving_strategies",
    "18_math_in_real_life",
    "19_preparing_for_algebra",
    "20_course_review_and_next_steps"
]

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
    
    # Create Rule Key file as a LaTeX file
    rule_key_path = os.path.join(course['directory'], 'rule_key.tex')
    with open(rule_key_path, 'w') as rule_key:
        rule_key.write(create_rule_key_tex(course['name']))
    print(f"  Created Rule Key LaTeX file: {rule_key_path}")

    # Compile LaTeX to PDF
    try:
        subprocess.run(['pdflatex', '-output-directory', course['directory'], rule_key_path], 
                       check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"  Compiled Rule Key PDF: {os.path.splitext(rule_key_path)[0]}.pdf")
    except subprocess.CalledProcessError:
        print(f"  Failed to compile Rule Key PDF for {course['name']}")
    except FileNotFoundError:
        print(f"  pdflatex not found. Please install LaTeX to compile the Rule Key PDF.")

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

    # Create lesson notebooks for Foundations of Pre-Algebra
    if course['name'] == "Foundations of Pre-Algebra":
        lessons_dir = os.path.join(course['directory'], '01_lessons')
        for lesson in pre_algebra_lessons:
            lesson_nb = nbf.v4.new_notebook()
            lesson_nb['cells'] = [nbf.v4.new_markdown_cell(f"# {lesson.replace('_', ' ').title()}\n\nLesson content goes here.")]
            lesson_path = os.path.join(lessons_dir, f"{lesson}.ipynb")
            with open(lesson_path, 'w') as f:
                nbf.write(lesson_nb, f)
            print(f"  Created lesson notebook: {lesson_path}")

print("Course structure creation complete with numbered subdirectories, lessons, and LaTeX-generated rule keys!")