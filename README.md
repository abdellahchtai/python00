# Python 00 - Introduction to Python

<div align="center">

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
![42 Network](https://img.shields.io/badge/42-Network-000000.svg)

*A comprehensive introduction to Python programming as part of the 42 Network curriculum*

</div>

---

## 📋 Table of Contents

- [About](#about)
- [Learning Objectives](#learning-objectives)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Module Structure](#module-structure)
- [Exercises Overview](#exercises-overview)
- [Getting Started](#getting-started)
- [Testing](#testing)
- [Resources](#resources)
- [Author](#author)

---

## 🎯 About

**Python 00** is the foundational module in the 42 Network's Python curriculum. This module introduces students to the fundamental concepts of Python programming, including:

- Basic syntax and semantics
- Data types and variables
- Control structures (loops and conditionals)
- Functions and scope
- String manipulation
- List and dictionary operations
- File I/O operations
- Error handling basics

This repository contains exercises designed to build a strong foundation in Python programming through practical, hands-on challenges.

---

## 🎓 Learning Objectives

By completing this module, you will be able to:

- ✅ Understand Python's basic syntax and programming paradigms
- ✅ Work with fundamental data types (strings, integers, floats, booleans)
- ✅ Implement control flow using conditionals and loops
- ✅ Create and use functions effectively
- ✅ Manipulate strings and work with formatted output
- ✅ Handle collections (lists, tuples, dictionaries, sets)
- ✅ Read from and write to files
- ✅ Implement basic error handling
- ✅ Follow Python coding standards (PEP 8)
- ✅ Debug and test your code

---

## 📚 Prerequisites

Before starting this module, you should have:

- Basic understanding of programming concepts
- Familiarity with command-line interface
- A computer with a Unix-based operating system (Linux or macOS recommended)
- Curiosity and willingness to learn! 🚀

---

## 🔧 Installation

### Installing Python

#### On macOS:
```bash
# Using Homebrew
brew install python3

# Verify installation
python3 --version
```

#### On Linux (Ubuntu/Debian):
```bash
# Update package list
sudo apt update

# Install Python 3
sudo apt install python3 python3-pip

# Verify installation
python3 --version
```

### Setting Up the Project

```bash
# Clone this repository
git clone https://github.com/abdellahchtai/python00.git

# Navigate to the project directory
cd python00

# (Optional) Create a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

---

## 📂 Module Structure

```
python00/
│
├── ex00/           # First exercise
├── ex01/           # Second exercise
├── ex02/           # Third exercise
├── ex03/           # Fourth exercise
├── ex04/           # Fifth exercise
├── ex05/           # Sixth exercise
├── ex06/           # Seventh exercise
├── ex07/           # Eighth exercise
├── ex08/           # Ninth exercise
├── ex09/           # Tenth exercise
│
└── README.md       # This file
```

Each exercise folder typically contains:
- Python source files (`.py`)
- Instructions/subject file
- Test files (if applicable)

---

## 📝 Exercises Overview

The Python 00 module typically includes exercises covering:

### **Ex00**: Hello World & First Steps
- Introduction to Python syntax
- Print statements and basic output
- Running your first Python program

### **Ex01**: Variables and Data Types
- Understanding variables
- Working with different data types
- Type conversion and casting

### **Ex02**: String Manipulation
- String operations and methods
- Formatting strings
- String indexing and slicing

### **Ex03**: Conditionals
- If/elif/else statements
- Comparison operators
- Logical operators (and, or, not)

### **Ex04**: Loops
- For loops and while loops
- Loop control (break, continue)
- Iterating over sequences

### **Ex05**: Functions
- Defining functions
- Parameters and arguments
- Return values and scope

### **Ex06**: Lists and Tuples
- Creating and manipulating lists
- List methods and operations
- Understanding tuples and immutability

### **Ex07**: Dictionaries
- Dictionary creation and operations
- Key-value pairs
- Dictionary methods

### **Ex08**: File Operations
- Reading from files
- Writing to files
- File handling best practices

### **Ex09**: Error Handling
- Try/except blocks
- Handling exceptions
- Raising custom exceptions

*Note: Actual exercise content may vary. Refer to individual exercise folders for specific requirements.*

---

## 🚀 Getting Started

### Running a Python Program

```bash
# Navigate to an exercise directory
cd ex00

# Run a Python file
python3 your_script.py

# Or make it executable
chmod +x your_script.py
./your_script.py
```

### Coding Standards

Follow **PEP 8** - Python's official style guide:

- Use 4 spaces for indentation (not tabs)
- Maximum line length of 79 characters
- Use descriptive variable names
- Add docstrings to functions and modules
- Follow naming conventions:
  - `snake_case` for functions and variables
  - `UPPER_CASE` for constants
  - `PascalCase` for classes

### Example Code Structure

```python
#!/usr/bin/env python3
"""
Module docstring: Brief description of what this module does.
"""


def my_function(param1, param2):
    """
    Function docstring: Explain what the function does.
    
    Args:
        param1: Description of first parameter
        param2: Description of second parameter
    
    Returns:
        Description of return value
    """
    result = param1 + param2
    return result


if __name__ == "__main__":
    # Your main code here
    print(my_function(5, 3))
```

---

## 🧪 Testing

### Manual Testing

Test your code with various inputs:

```bash
python3 your_script.py
```

### Using Python's Built-in Tools

```bash
# Check syntax without running
python3 -m py_compile your_script.py

# Run with Python's debugger
python3 -m pdb your_script.py
```

### Code Quality Checks

```bash
# Install flake8 for style checking
pip3 install flake8

# Check your code
flake8 your_script.py

# Install pycodestyle (formerly pep8)
pip3 install pycodestyle

# Check PEP 8 compliance
pycodestyle your_script.py
```

---

## 📖 Resources

### Official Documentation
- [Python Official Documentation](https://docs.python.org/3/)
- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [Python Tutorial](https://docs.python.org/3/tutorial/)

### Learning Resources
- [Real Python](https://realpython.com/) - Comprehensive Python tutorials
- [Python for Beginners](https://www.python.org/about/gettingstarted/)
- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)
- [W3Schools Python Tutorial](https://www.w3schools.com/python/)

### Interactive Practice
- [Python Tutor](http://pythontutor.com/) - Visualize code execution
- [HackerRank Python](https://www.hackerrank.com/domains/python)
- [LeetCode](https://leetcode.com/)

### 42 Network Resources
- [42 Intra](https://intra.42.fr/)
- 42 Network Slack channels
- Peer collaboration and code reviews

---

## 👨‍💻 Author

**Abdellah Chtai**

- GitHub: [@abdellahchtai](https://github.com/abdellahchtai)

---

## 📄 License

This project is part of the 42 Network curriculum. Please refer to 42's policies regarding code sharing and academic integrity.

---

## 🤝 Contributing

While this is a personal learning project for the 42 Network curriculum, suggestions and feedback are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch
3. Submit a pull request with improvements

**Note**: If you're a 42 student, remember to follow the school's policies on collaboration and plagiarism.

---

## ⭐ Acknowledgments

- 42 Network for the excellent curriculum
- Fellow 42 students for collaboration and support
- The Python community for comprehensive documentation

---

<div align="center">

**Happy Coding! 🐍**

*"The only way to learn a new programming language is by writing programs in it." - Dennis Ritchie*

</div>
