{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Whole Numbers and Operations\n",
    "\n",
    "Welcome to the second lesson in **Calculatorium Interactum: Foundations of Pre-Algebra**! In this lesson, we'll explore whole numbers and the fundamental operations we can perform with them. Let's dive into the building blocks of mathematics!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## What are Whole Numbers?\n",
    "\n",
    "Whole numbers are the counting numbers (1, 2, 3, ...) and zero. They are the foundation of our number system and are used in countless everyday situations.\n",
    "\n",
    "Key points about whole numbers:\n",
    "1. They are positive integers and zero\n",
    "2. They do not include fractions or decimals\n",
    "3. They extend infinitely in the positive direction"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Basic Operations with Whole Numbers\n",
    "\n",
    "There are four fundamental operations we can perform with whole numbers:\n",
    "1. Addition (+)\n",
    "2. Subtraction (-)\n",
    "3. Multiplication (×)\n",
    "4. Division (÷)\n",
    "\n",
    "Let's explore each of these operations with some interactive examples."
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
    "import random"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 1. Addition\n",
    "\n",
    "Addition is the process of combining two or more numbers to get a sum. Let's practice with a simple addition problem."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def check_addition(b):\n",
    "    global num1, num2\n",
    "    user_answer = addition_input.value\n",
    "    correct_answer = num1 + num2\n",
    "    if user_answer == correct_answer:\n",
    "        addition_output.value = f\"<span style='color: green;'>Correct! {num1} + {num2} = {correct_answer}.</span>\"\n",
    "    else:\n",
    "        addition_output.value = f\"<span style='color: red;'>Not quite. {num1} + {num2} = {correct_answer}. Let's try again!</span>\"\n",
    "    num1, num2 = random.randint(1, 50), random.randint(1, 50)\n",
    "    clear_output(wait=True)\n",
    "    display(HTML(f\"<h3>What is {num1} + {num2}?</h3>\"))\n",
    "    display(addition_input, addition_check_button, addition_output)\n",
    "\n",
    "num1, num2 = random.randint(1, 50), random.randint(1, 50)\n",
    "addition_input = widgets.IntText(description=\"Your answer:\")\n",
    "addition_check_button = widgets.Button(description=\"Check\")\n",
    "addition_check_button.on_click(check_addition)\n",
    "addition_output = widgets.HTML()\n",
    "\n",
    "display(HTML(f\"<h3>What is {num1} + {num2}?</h3>\"))\n",
    "display(addition_input, addition_check_button, addition_output)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 2. Subtraction\n",
    "\n",
    "Subtraction is the process of taking one number away from another. Let's practice with a subtraction problem."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def check_subtraction(b):\n",
    "    global num1, num2\n",
    "    user_answer = subtraction_input.value\n",
    "    correct_answer = num1 - num2\n",
    "    if user_answer == correct_answer:\n",
    "        subtraction_output.value = f\"<span style='color: green;'>Correct! {num1} - {num2} = {correct_answer}.</span>\"\n",
    "    else:\n",
    "        subtraction_output.value = f\"<span style='color: red;'>Not quite. {num1} - {num2} = {correct_answer}. Let's try again!</span>\"\n",
    "    num1, num2 = random.randint(10, 100), random.randint(1, 50)\n",
    "    clear_output(wait=True)\n",
    "    display(HTML(f\"<h3>What is {num1} - {num2}?</h3>\"))\n",
    "    display(subtraction_input, subtraction_check_button, subtraction_output)\n",
    "\n",
    "num1, num2 = random.randint(10, 100), random.randint(1, 50)\n",
    "subtraction_input = widgets.IntText(description=\"Your answer:\")\n",
    "subtraction_check_button = widgets.Button(description=\"Check\")\n",
    "subtraction_check_button.on_click(check_subtraction)\n",
    "subtraction_output = widgets.HTML()\n",
    "\n",
    "display(HTML(f\"<h3>What is {num1} - {num2}?</h3>\"))\n",
    "display(subtraction_input, subtraction_check_button, subtraction_output)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 3. Multiplication\n",
    "\n",
    "Multiplication is a shorthand way of expressing repeated addition. Let's practice with a multiplication problem."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def check_multiplication(b):\n",
    "    global num1, num2\n",
    "    user_answer = multiplication_input.value\n",
    "    correct_answer = num1 * num2\n",
    "    if user_answer == correct_answer:\n",
    "        multiplication_output.value = f\"<span style='color: green;'>Correct! {num1} × {num2} = {correct_answer}.</span>\"\n",
    "    else:\n",
    "        multiplication_output.value = f\"<span style='color: red;'>Not quite. {num1} × {num2} = {correct_answer}. Let's try again!</span>\"\n",
    "    num1, num2 = random.randint(2, 12), random.randint(2, 12)\n",
    "    clear_output(wait=True)\n",
    "    display(HTML(f\"<h3>What is {num1} × {num2}?</h3>\"))\n",
    "    display(multiplication_input, multiplication_check_button, multiplication_output)\n",
    "\n",
    "num1, num2 = random.randint(2, 12), random.randint(2, 12)\n",
    "multiplication_input = widgets.IntText(description=\"Your answer:\")\n",
    "multiplication_check_button = widgets.Button(description=\"Check\")\n",
    "multiplication_check_button.on_click(check_multiplication)\n",
    "multiplication_output = widgets.HTML()\n",
    "\n",
    "display(HTML(f\"<h3>What is {num1} × {num2}?</h3>\"))\n",
    "display(multiplication_input, multiplication_check_button, multiplication_output)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 4. Division\n",
    "\n",
    "Division is the process of splitting a number into equal parts. Let's practice with a division problem."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def check_division(b):\n",
    "    global num1, num2\n",
    "    user_answer = division_input.value\n",
    "    correct_answer = num1 // num2\n",
    "    if user_answer == correct_answer:\n",
    "        division_output.value = f\"<span style='color: green;'>Correct! {num1} ÷ {num2} = {correct_answer}.</span>\"\n",
    "    else:\n",
    "        division_output.value = f\"<span style='color: red;'>Not quite. {num1} ÷ {num2} = {correct_answer}. Let's try again!</span>\"\n",
    "    num2 = random.randint(2, 12)\n",
    "    num1 = num2 * random.randint(2, 12)\n",
    "    clear_output(wait=True)\n",
    "    display(HTML(f\"<h3>What is {num1} ÷ {num2}?</h3>\"))\n",
    "    display(division_input, division_check_button, division_output)\n",
    "\n",
    "num2 = random.randint(2, 12)\n",
    "num1 = num2 * random.randint(2, 12)\n",
    "division_input = widgets.IntText(description=\"Your answer:\")\n",
    "division_check_button = widgets.Button(description=\"Check\")\n",
    "division_check_button.on_click(check_division)\n",
    "division_output = widgets.HTML()\n",
    "\n",
    "display(HTML(f\"<h3>What is {num1} ÷ {num2}?</h3>\"))\n",
    "display(division_input, division_check_button, division_output)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Conclusion\n",
    "\n",
    "In this lesson, we've explored whole numbers and the four basic operations: addition, subtraction, multiplication, and division. These fundamental concepts form the basis of all mathematics and are crucial for your journey in pre-algebra.\n",
    "\n",
    "Remember, practice makes perfect! Feel free to run these interactive exercises multiple times to reinforce your understanding.\n",
    "\n",
    "In our next lesson, we'll delve into factors and multiples, building upon the concepts we've learned here. See you then!"
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