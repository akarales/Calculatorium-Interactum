import json
import os

with open('Calculatorium_interactum_courses.json', 'r') as f:
    data = json.load(f)

for course in data['courses']:
    os.makedirs(course['directory'], exist_ok=True)
    print(f"Created directory: {course['directory']}")