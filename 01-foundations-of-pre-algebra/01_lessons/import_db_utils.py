import sys
import os

# Get the absolute path of the current file
current_dir = os.path.dirname(os.path.abspath(__file__))

# Go up two levels to reach the root directory
root_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))

# Add the root directory to sys.path if it's not already there
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

# Now we can import all necessary functions from db_utils
from db_utils import update_progress, get_progress, reset_progress, get_courses_and_lessons

# You can add any other imports from db_utils here if needed