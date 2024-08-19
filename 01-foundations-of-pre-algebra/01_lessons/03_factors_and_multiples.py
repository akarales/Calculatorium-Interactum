{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Factors and Multiples\n",
    "\n",
    "Welcome to the third lesson in **Calculatorium Interactum: Foundations of Pre-Algebra**! In this lesson, we'll explore factors and multiples, two important concepts that help us understand the relationships between numbers. Let's dive in!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## What are Factors and Multiples?\n",
    "\n",
    "### Factors\n",
    "Factors are numbers that divide evenly into another number. For example, the factors of 12 are 1, 2, 3, 4, 6, and 12.\n",
    "\n",
    "### Multiples\n",
    "Multiples are the product of a number and an integer. For example, the multiples of 3 are 3, 6, 9, 12, 15, and so on.\n",
    "\n",
    "Understanding factors and multiples helps us solve many mathematical problems and is crucial for more advanced topics like fractions and algebra."
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
    "## Finding Factors\n",
    "\n",
    "Let's practice finding factors of a number. Remember, factors are numbers that divide evenly into another number with no remainder."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def check_factors(b):\n",
    "    global number\n",
    "    user_answer = [int(x.strip()) for x in factors_input.value.split(',')]\n",
    "    correct_factors = [i for i in range(1, number + 1) if number % i == 0]\n",
    "    if set(user_answer) == set(correct_factors):\n",
    "        factors_output.value = f\"<span style='color: green;'>Correct! The factors of {number} are {', '.join(map(str, correct_factors))}.</span>\"\n",
    "    else:\n",
    "        factors_output.value = f\"<span style='color: red;'>Not quite. The factors of {number} are {', '.join(map(str, correct_factors))}. Let's try again!</span>\"\n",
    "    number = random.randint(10, 50)\n",
    "    clear_output(wait=True)\n",
    "    display(HTML(f\"<h3>What are the factors of {number}?</h3>\"))\n",
    "    display(HTML(\"Enter the factors separated by commas (e.g., 1, 2, 3)\"))\n",
    "    display(factors_input, factors_check_button, factors_output)\n",
    "\n",
    "number = random.randint(10, 50)\n",
    "factors_input = widgets.Text(description=\"Factors:\")\n",
    "factors_check_button = widgets.Button(description=\"Check\")\n",
    "factors_check_button.on_click(check_factors)\n",
    "factors_output = widgets.HTML()\n",
    "\n",
    "display(HTML(f\"<h3>What are the factors of {number}?</h3>\"))\n",
    "display(HTML(\"Enter the factors separated by commas (e.g., 1, 2, 3)\"))\n",
    "display(factors_input, factors_check_button, factors_output)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Identifying Multiples\n",
    "\n",
    "Now, let's practice identifying multiples of a number. Remember, multiples are the product of a number and an integer."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def check_multiples(b):\n",
    "    global number\n",
    "    user_answer = [int(x.strip()) for x in multiples_input.value.split(',')]\n",
    "    correct_multiples = [number * i for i in range(1, 6)]\n",
    "    if user_answer == correct_multiples:\n",
    "        multiples_output.value = f\"<span style='color: green;'>Correct! The first five multiples of {number} are {', '.join(map(str, correct_multiples))}.</span>\"\n",
    "    else:\n",
    "        multiples_output.value = f\"<span style='color: red;'>Not quite. The first five multiples of {number} are {', '.join(map(str, correct_multiples))}. Let's try again!</span>\"\n",
    "    number = random.randint(2, 12)\n",
    "    clear_output(wait=True)\n",
    "    display(HTML(f\"<h3>What are the first five multiples of {number}?</h3>\"))\n",
    "    display(HTML(\"Enter the multiples separated by commas (e.g., 2, 4, 6, 8, 10)\"))\n",
    "    display(multiples_input, multiples_check_button, multiples_output)\n",
    "\n",
    "number = random.randint(2, 12)\n",
    "multiples_input = widgets.Text(description=\"Multiples:\")\n",
    "multiples_check_button = widgets.Button(description=\"Check\")\n",
    "multiples_check_button.on_click(check_multiples)\n",
    "multiples_output = widgets.HTML()\n",
    "\n",
    "display(HTML(f\"<h3>What are the first five multiples of {number}?</h3>\"))\n",
    "display(HTML(\"Enter the multiples separated by commas (e.g., 2, 4, 6, 8, 10)\"))\n",
    "display(multiples_input, multiples_check_button, multiples_output)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Prime and Composite Numbers\n",
    "\n",
    "Understanding factors leads us to two special types of numbers:\n",
    "\n",
    "1. **Prime numbers**: Numbers that have exactly two factors - 1 and themselves.\n",
    "2. **Composite numbers**: Numbers that have more than two factors.\n",
    "\n",
    "Let's practice identifying prime and composite numbers!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def is_prime(n):\n",
    "    if n < 2:\n",
    "        return False\n",
    "    for i in range(2, int(n**0.5) + 1):\n",
    "        if n % i == 0:\n",
    "            return False\n",
    "    return True\n",
    "\n",
    "def check_prime_composite(b):\n",
    "    global number\n",
    "    user_answer = prime_composite_input.value.lower()\n",
    "    correct_answer = \"prime\" if is_prime(number) else \"composite\"\n",
    "    if user_answer == correct_answer:\n",
    "        prime_composite_output.value = f\"<span style='color: green;'>Correct! {number} is a {correct_answer} number.</span>\"\n",
    "    else:\n",
    "        prime_composite_output.value = f\"<span style='color: red;'>Not quite. {number} is a {correct_answer} number. Let's try again!</span>\"\n",
    "    number = random.randint(2, 50)\n",
    "    clear_output(wait=True)\n",
    "    display(HTML(f\"<h3>Is {number} a prime or composite number?</h3>\"))\n",
    "    display(prime_composite_input, prime_composite_check_button, prime_composite_output)\n",
    "\n",
    "number = random.randint(2, 50)\n",
    "prime_composite_input = widgets.Text(description=\"Answer:\")\n",
    "prime_composite_check_button = widgets.Button(description=\"Check\")\n",
    "prime_composite_check_button.on_click(check_prime_composite)\n",
    "prime_composite_output = widgets.HTML()\n",
    "\n",
    "display(HTML(f\"<h3>Is {number} a prime or composite number?</h3>\"))\n",
    "display(prime_composite_input, prime_composite_check_button, prime_composite_output)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Conclusion\n",
    "\n",
    "In this lesson, we've explored factors and multiples, and introduced the concepts of prime and composite numbers. Understanding these relationships between numbers is crucial for many areas of mathematics, including fractions, algebra, and beyond.\n",
    "\n",
    "Remember to practice these concepts regularly. You can run these interactive exercises multiple times to reinforce your understanding.\n",
    "\n",
    "In our next lesson, we'll introduce fractions, building upon the concepts of factors and multiples that we've learned here. See you then!"
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