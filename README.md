# Calculatorium Interactum

## Overview

Calculatorium Interactum is a comprehensive, interactive mathematics learning series spanning from pre-algebra to advanced topics in calculus, linear algebra, and statistics. This project aims to provide a rich, engaging learning experience through a combination of traditional mathematical instruction and modern computational tools.

## Project Structure

The project consists of 10 courses, each with the following structure:

```
[course-name]/
├── 01_lessons/
│   └── lesson_template.ipynb
├── 02_quiz_book/
├── 03_reinforcement_workbook/
├── 04_interactive_visualizations/
│   └── dynamic_plots.py
├── 05_midterm_exam/
├── 06_final_exam/
├── 07_use_cases/
│   └── use_case_template.ipynb
└── rule_key.pdf
```

### Courses

1. Foundations of Pre-Algebra
2. Algebra Unveiled
3. Geometry Explored
4. Advanced Algebra and Precalculus
5. Trigonometry in Depth
6. Calculus I - Limits and Derivatives
7. Calculus II - Integrals and Applications
8. Calculus III - Multivariable Calculus
9. Linear Algebra Fundamentals
10. Probability and Statistics

## Key Features

- **Interactive Lessons**: Jupyter Notebooks are used for lessons, allowing for a mix of explanations, code, and interactive elements.
- **Adaptive Learning**: Each lesson includes an adaptive learning algorithm to adjust difficulty based on student performance.
- **Comprehensive Assessment**: Quiz books, midterm exams, and final exams are provided for each course.
- **Reinforcement Workbooks**: Additional practice materials to solidify understanding of concepts.
- **Interactive Visualizations**: Dynamic plots and diagrams to illustrate mathematical concepts.
- **Real-world Applications**: Use cases demonstrating practical applications of mathematical concepts.
- **Rule Keys**: PDF documents summarizing key rules and formulas for quick reference.

## Getting Started

1. Clone this repository:
   ```
   git clone https://github.com/your-username/Calculatorium-Interactum.git
   ```
2. Ensure you have Jupyter Notebook installed:
   ```
   pip install jupyter
   ```
3. Navigate to a course directory and open the lesson notebooks:
   ```
   cd Calculatorium-Interactum/01-foundations-of-pre-algebra/01_lessons
   jupyter notebook
   ```

## Development

To contribute to the development of Calculatorium Interactum:

1. Ensure you have Python and LaTeX installed on your system.
2. Install required Python libraries:
   ```
   pip install nbformat
   ```
3. Run the update script to generate or update the course structure:
   ```
   python update_course_structure.py
   ```

## Contributing

We welcome contributions to Calculatorium Interactum! Please read our [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on how to submit contributions.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any queries regarding Calculatorium Interactum, please contact [Your Name] at [your email or contact information].

