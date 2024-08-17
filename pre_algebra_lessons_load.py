import json
import os
import nbformat as nbf

# ... [previous parts of the script remain the same] ...

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

# ... [keep the previous functions and main loop] ...

# Inside the main loop, add this block for the Foundations of Pre-Algebra course
if course['name'] == "Foundations of Pre-Algebra":
    lessons_dir = os.path.join(course['directory'], '01_lessons')
    for lesson in pre_algebra_lessons:
        lesson_nb = nbf.v4.new_notebook()
        lesson_nb['cells'] = [nbf.v4.new_markdown_cell(f"# {lesson.replace('_', ' ').title()}\n\nLesson content goes here.")]
        lesson_path = os.path.join(lessons_dir, f"{lesson}.ipynb")
        with open(lesson_path, 'w') as f:
            nbf.write(lesson_nb, f)
        print(f"  Created lesson notebook: {lesson_path}")

# ... [rest of the script remains the same] ...