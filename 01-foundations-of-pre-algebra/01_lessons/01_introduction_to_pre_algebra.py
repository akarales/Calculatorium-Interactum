{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Introduction to Pre-Algebra\n",
    "\n",
    "Welcome to the first lesson in **Calculatorium Interactum: Foundations of Pre-Algebra**! In this lesson, we'll explore what pre-algebra is, why it's important, and some of the key concepts we'll be learning throughout this course."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import ipywidgets as widgets\n",
    "from IPython.display import display, HTML, clear_output\n",
    "from import_db_utils import update_progress, reset_progress, get_progress\n",
    "\n",
    "# Assume user_id 1 for now. In a real app, you'd get this from authentication.\n",
    "user_id = 1\n",
    "course_name = \"Foundations of Pre-Algebra\"\n",
    "lesson_name = \"Introduction to Pre-Algebra\"\n",
    "\n",
    "# Initialize score\n",
    "score = 0\n",
    "total_questions = 3\n",
    "\n",
    "print(\"Module 'db_utils' imported successfully.\")\n",
    "\n",
    "def get_existing_progress():\n",
    "    progress_df = get_progress(user_id)\n",
    "    if not progress_df.empty:\n",
    "        lesson_progress = progress_df[(progress_df['course'] == course_name) & (progress_df['lesson'] == lesson_name)]\n",
    "        if not lesson_progress.empty:\n",
    "            return lesson_progress.iloc[0]['score'], lesson_progress.iloc[0]['completed']\n",
    "    return None, None\n",
    "\n",
    "existing_score, existing_completed = get_existing_progress()\n",
    "if existing_score is not None:\n",
    "    print(f\"You have already completed this lesson with a score of {existing_score}%.\")\n",
    "    retake = input(\"Would you like to retake the lesson? (yes/no): \").lower().strip()\n",
    "    if retake != 'yes':\n",
    "        print(\"Exiting the lesson. You can run this notebook again if you change your mind.\")\n",
    "        import sys\n",
    "        sys.exit()\n",
    "    else:\n",
    "        reset_progress(user_id, courses=[course_name], lessons=[lesson_name])\n",
    "        print(\"Progress reset. Starting the lesson from the beginning.\")\n",
    "\n",
    "print(\"Let's begin the lesson!\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## What is Pre-Algebra?\n",
    "\n",
    "Pre-algebra is the bridge between basic arithmetic and algebra. It introduces fundamental concepts that prepare you for more advanced mathematical thinking. In pre-algebra, we start to use symbols to represent unknown quantities and learn how to manipulate these symbols using the rules of arithmetic.\n",
    "\n",
    "Key areas we'll explore in pre-algebra include:\n",
    "1. Properties of numbers\n",
    "2. Order of operations\n",
    "3. Negative numbers\n",
    "4. Fractions, decimals, and percentages\n",
    "5. Basic equation solving\n",
    "6. Introduction to functions and graphs"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Why is Pre-Algebra Important?\n",
    "\n",
    "Pre-algebra is crucial because it lays the foundation for all future mathematical studies. It helps develop critical thinking and problem-solving skills that are valuable not just in mathematics, but in many areas of life and various career paths.\n",
    "\n",
    "Some specific reasons why pre-algebra is important:\n",
    "1. It introduces abstract thinking in mathematics.\n",
    "2. It prepares you for algebra and more advanced math courses.\n",
    "3. It improves logical reasoning skills.\n",
    "4. It has many real-world applications, from basic budgeting to more complex scientific and engineering problems."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Interactive Examples and Exercises\n",
    "\n",
    "Now, let's put these concepts into practice with some interactive exercises. Try your best to solve them, and remember, making mistakes is part of the learning process!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 1. Understanding Variables\n",
    "\n",
    "Let's start with a simple question about variables. Given the equation **2x + 3**, where **x = 5**, what is the value of the expression?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def check_variable_understanding(b):\n",
    "    global score\n",
    "    user_answer = variable_input.value\n",
    "    correct_answer = 2 * x_value + 3\n",
    "    if user_answer == correct_answer:\n",
    "        result_output.value = f\"<span style='color: green;'>Correct! When x = {x_value}, 2x + 3 = {correct_answer}.</span>\"\n",
    "        score += 1\n",
    "    else:\n",
    "        result_output.value = f\"<span style='color: red;'>Not quite. When x = {x_value}, 2x + 3 = {correct_answer}. Let's try again!</span>\"\n",
    "    clear_output(wait=True)\n",
    "    display(HTML(f\"<h3>If x = {x_value}, what is 2x + 3?</h3>\"))\n",
    "    display(variable_input, check_button, result_output)\n",
    "\n",
    "x_value = 5\n",
    "variable_input = widgets.IntText(description=\"Your answer:\")\n",
    "check_button = widgets.Button(description=\"Check\")\n",
    "check_button.on_click(check_variable_understanding)\n",
    "result_output = widgets.HTML()\n",
    "\n",
    "display(HTML(f\"<h3>If x = {x_value}, what is 2x + 3?</h3>\"))\n",
    "display(variable_input, check_button, result_output)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 2. Order of Operations\n",
    "\n",
    "The order of operations is a fundamental concept in mathematics. Let's test your understanding with this problem: What is the result of **2 + 3 * 4**?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def check_order_of_operations(b):\n",
    "    global score\n",
    "    user_answer = operation_input.value\n",
    "    correct_answer = 2 + 3 * 4\n",
    "    if user_answer == correct_answer:\n",
    "        operation_output.value = f\"<span style='color: green;'>Correct! 2 + 3 * 4 = {correct_answer}.</span>\"\n",
    "        score += 1\n",
    "    else:\n",
    "        operation_output.value = f\"<span style='color: red;'>Not quite. Remember the order of operations: 2 + 3 * 4 = 2 + 12 = {correct_answer}. Let's try again!</span>\"\n",
    "    clear_output(wait=True)\n",
    "    display(HTML(\"<h3>What is the result of 2 + 3 * 4?</h3>\"))\n",
    "    display(operation_input, operation_check_button, operation_output)\n",
    "\n",
    "operation_input = widgets.IntText(description=\"Your answer:\")\n",
    "operation_check_button = widgets.Button(description=\"Check\")\n",
    "operation_check_button.on_click(check_order_of_operations)\n",
    "operation_output = widgets.HTML()\n",
    "\n",
    "display(HTML(\"<h3>What is the result of 2 + 3 * 4?</h3>\"))\n",
    "display(operation_input, operation_check_button, operation_output)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 3. Fraction to Decimal Conversion\n",
    "\n",
    "Fractions and decimals are different ways of representing numbers. Convert the fraction **3/4** to a decimal."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def check_fraction_conversion(b):\n",
    "    global score\n",
    "    user_answer = fraction_input.value\n",
    "    correct_answer = round(3/4, 2)\n",
    "    if abs(user_answer - correct_answer) < 0.001:  # Allow for small rounding errors\n",
    "        fraction_output.value = f\"<span style='color: green;'>Correct! 3/4 as a decimal is {correct_answer}.</span>\"\n",
    "        score += 1\n",
    "    else:\n",
    "        fraction_output.value = f\"<span style='color: red;'>Not quite. 3/4 as a decimal is {correct_answer}. Let's try again!</span>\"\n",
    "    clear_output(wait=True)\n",
    "    display(HTML(\"<h3>Convert the fraction 3/4 to a decimal:</h3>\"))\n",
    "    display(fraction_input, fraction_check_button, fraction_output)\n",
    "\n",
    "fraction_input = widgets.FloatText(description=\"Your answer:\")\n",
    "fraction_check_button = widgets.Button(description=\"Check\")\n",
    "fraction_check_button.on_click(check_fraction_conversion)\n",
    "fraction_output = widgets.HTML()\n",
    "\n",
    "display(HTML(\"<h3>Convert the fraction 3/4 to a decimal:</h3>\"))\n",
    "display(fraction_input, fraction_check_button, fraction_output)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Conclusion\n",
    "\n",
    "In this introduction to pre-algebra, we've discussed what pre-algebra is, why it's important, and practiced some fundamental concepts including variables, order of operations, and fraction-to-decimal conversion.\n",
    "\n",
    "As we progress through this course, we'll delve deeper into these concepts and build a strong foundation for your future mathematical journey. Remember, mathematics is a skill that improves with practice, so don't hesitate to revisit these exercises and explore further!\n",
    "\n",
    "In our next lesson, we'll explore the properties of numbers in more detail. See you then!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Calculate final score\n",
    "final_score = (score / total_questions) * 100\n",
    "\n",
    "print(f\"Lesson completed! Your score: {final_score}%\")\n",
    "\n",
    "def save_progress(b):\n",
    "    try:\n",
    "        update_progress(user_id, course_name, lesson_name, final_score, 1)\n",
    "        save_output.value = \"<span style='color: green;'>Your progress has been saved to the database.</span>\"\n",
    "    except Exception as e:\n",
    "        save_output.value = f\"<span style='color: red;'>An error occurred while saving progress: {str(e)}</span>\"\n",
    "    \n",
    "    clear_output(wait=True)\n",
    "    display(HTML(f\"<h3>Your score: {final_score}%</h3>\"))\n",
    "    display(save_button, save_output)\n",
    "    display(HTML(\"<p>Would you like to retake the lesson to improve your score?</p>\"))\n",
    "    display(retake_button)\n",
    "\n",
    "def retake_lesson(b):\n",
    "    global score\n",
    "    score = 0\n",
    "    print(\"To retake the lesson, please run all cells in this notebook again.\")\n",
    "\n",
    "save_button = widgets.Button(description=\"Save Progress\")\n",
    "save_button.on_click(save_progress)\n",
    "save_output = widgets.HTML()\n",
    "\n",
    "retake_button = widgets.Button(description=\"Retake Lesson\")\n",
    "retake_button.on_click(retake_lesson)\n",
    "\n",
    "display(HTML(f\"<h3>Your score: {final_score}%</h3>\"))\n",
    "display(save_button, save_output)\n",
    "display(HTML(\"<p>Would you like to retake the lesson to improve your score?</p>\"))\n",
    "display(retake_button)"
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
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}