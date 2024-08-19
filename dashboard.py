{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Calculatorium Interactum Dashboard\n",
    "\n",
    "Welcome to your personal dashboard for tracking your progress through the Calculatorium Interactum course. Here you can view your scores, completed lessons, and reset your progress if needed."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "from db_utils import get_progress, reset_progress, get_courses_and_lessons\n",
    "from ipywidgets import widgets\n",
    "from IPython.display import display, clear_output\n",
    "\n",
    "# Assume user_id 1 for now. In a real app, you'd get this from authentication.\n",
    "user_id = 1"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Your Progress"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def plot_progress():\n",
    "    progress = get_progress(user_id)\n",
    "    if progress.empty:\n",
    "        print(\"No progress data available. Complete some lessons to see your progress!\")\n",
    "        return\n",
    "    \n",
    "    plt.figure(figsize=(15, 8))\n",
    "    sns.barplot(x='lesson', y='score', hue='course', data=progress)\n",
    "    plt.title('Course and Lesson Scores')\n",
    "    plt.ylim(0, 100)\n",
    "    plt.xticks(rotation=45, ha='right')\n",
    "    plt.legend(title='Course', bbox_to_anchor=(1.05, 1), loc='upper left')\n",
    "    plt.tight_layout()\n",
    "    plt.show()\n",
    "\n",
    "    completed = progress['completed'].sum()\n",
    "    total = len(progress)\n",
    "    print(f\"Completed lessons: {completed}/{total}\")\n",
    "\n",
    "plot_progress()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Reset Progress\n",
    "\n",
    "If you want to start over or reset your progress for specific courses or lessons, you can do so here. Be careful, as this action cannot be undone!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def on_reset_click(b):\n",
    "    selected_courses = [course for course, checkbox in course_checkboxes.items() if checkbox.value]\n",
    "    selected_lessons = [lesson for lesson, checkbox in lesson_checkboxes.items() if checkbox.value]\n",
    "    \n",
    "    if selected_courses or selected_lessons:\n",
    "        reset_progress(user_id, courses=selected_courses, lessons=selected_lessons)\n",
    "        reset_message = []\n",
    "        if selected_courses:\n",
    "            reset_message.append(f\"Courses: {', '.join(selected_courses)}\")\n",
    "        if selected_lessons:\n",
    "            reset_message.append(f\"Lessons: {', '.join(selected_lessons)}\")\n",
    "        print(f\"Progress reset for {' and '.join(reset_message)}\")\n",
    "    else:\n",
    "        reset_progress(user_id)\n",
    "        print(\"All progress reset.\")\n",
    "    \n",
    "    clear_output(wait=True)\n",
    "    plot_progress()\n",
    "    display_reset_options()\n",
    "\n",
    "def display_reset_options():\n",
    "    global course_checkboxes, lesson_checkboxes\n",
    "    course_checkboxes = {}\n",
    "    lesson_checkboxes = {}\n",
    "    courses_lessons = get_courses_and_lessons(user_id)\n",
    "    \n",
    "    if not courses_lessons:\n",
    "        print(\"No courses or lessons available. Complete some lessons to see reset options.\")\n",
    "        return\n",
    "    \n",
    "    print(\"Select courses or lessons to reset (leave all unchecked to reset all):\")\n",
    "    \n",
    "    for course, lessons in courses_lessons.items():\n",
    "        course_checkbox = widgets.Checkbox(value=False, description=f\"Course: {course}\")\n",
    "        course_checkboxes[course] = course_checkbox\n",
    "        display(course_checkbox)\n",
    "        \n",
    "        for lesson in lessons:\n",
    "            lesson_checkbox = widgets.Checkbox(value=False, description=f\"  Lesson: {lesson}\")\n",
    "            lesson_checkboxes[lesson] = lesson_checkbox\n",
    "            display(lesson_checkbox)\n",
    "    \n",
    "    reset_button = widgets.Button(description=\"Reset Selected Progress\")\n",
    "    reset_button.on_click(on_reset_click)\n",
    "    display(reset_button)\n",
    "\n",
    "display_reset_options()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Next Steps\n",
    "\n",
    "Based on your current progress, here are some suggested next steps:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def suggest_next_steps():\n",
    "    progress = get_progress(user_id)\n",
    "    if progress.empty:\n",
    "        print(\"1. Start with the first lesson in 'Foundations of Pre-Algebra'.\")\n",
    "        return\n",
    "    \n",
    "    # Find lessons with scores below 80%\n",
    "    review_lessons = progress[progress['score'] < 80]\n",
    "    if not review_lessons.empty:\n",
    "        print(\"1. Review these lessons where your score is below 80%:\")\n",
    "        for _, lesson in review_lessons.iterrows():\n",
    "            print(f\"   - {lesson['course']}: {lesson['lesson']} (Score: {lesson['score']}%)\")\n",
    "    \n",
    "    # Suggest the next incomplete lesson\n",
    "    incomplete_lessons = progress[progress['completed'] == 0]\n",
    "    if not incomplete_lessons.empty:\n",
    "        next_lesson = incomplete_lessons.iloc[0]\n",
    "        print(f\"2. Continue with the next lesson: {next_lesson['course']} - {next_lesson['lesson']}\")\n",
    "    else:\n",
    "        print(\"2. Great job! You've completed all available lessons.\")\n",
    "    \n",
    "    print(\"3. Remember, consistent practice is key to mastering mathematics. Keep up the great work!\")\n",
    "\n",
    "suggest_next_steps()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}