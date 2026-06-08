# Data Analyzer and Transformer Program

A menu-driven Python application that allows users to input, analyze, filter, and sort numerical data. This project demonstrates the use of core Python concepts such as recursion, lambda functions, built-in functions, sorting, and menu-driven programming.

# Features

## 1. Input Data
- Accepts numerical values from the user.
- Stores the data in a list for further processing.

## 2. Display Data Summary
Displays:
- Total number of elements
- Minimum value
- Maximum value
- Sum of all values
- Average value

## 3. Calculate Factorial (Recursion)
- Calculates the factorial of a user-entered number.
- Uses a recursive function implementation.

## 4. Filter Data by Threshold (Lambda Function)
- Accepts a threshold value from the user.
- Filters and displays values greater than or equal to the threshold using a lambda function.

## 5. Sort Data
Provides:
- Ascending order sorting
- Descending order sorting

## 6. Display Dataset Statistics
Displays:
- Minimum value
- Maximum value
- Sum of values
- Average value

## 7. Exit Program
- Terminates the application safely.

---

## Concepts Used

- Python Lists
- Built-in Functions
- Recursion
- Lambda Functions
- Filter Function
- Sorting
- Match-Case Statements
- Loops
- Conditional Statements
- User Input Handling

---

## Project Structure

```text
Data-Analyzer-and-Transformer/
│
├── data_analyzer.py
├── README.md
```

---

## Sample Run

```text
Welcome to the Data Analyzer and Transformer Program

Main Menu
1. Input Data
2. Display Data Summary (Built-in Function)
3. Calculate Factorial (Recursion)
4. Filter Data by Threshold (Lambda Function)
5. Sort Data
6. Display Dataset Statistics (Return Multiple Values)
7. Exit Program

Please Enter your Choice: 1

Enter data for a 1D array:
10
20
30
40
50
60
70

Data has been stored successfully!
```

## Data Summary Output

```text
Data Summary:
- Total elements: 7
- Minimum Value: 10
- Maximum Value: 70
- Sum of all values: 280
- Average value: 40.0
```

## Filter Data Output

```text
Enter the threshold value to filter out data above this value: 50

Filtered Data:
[50, 60, 70]
```

## Sorting Output

```text
Choose sorting option:
1. Ascending
2. Descending

Sorted Data in Ascending Order:
[10, 20, 30, 40, 50, 60, 70]
```

---

## How to Run

1. Clone the repository:

```bash
  git clone <repository-url>
```

2. Navigate to the project directory:

```bash
  cd Data-Analyzer-and-Transformer
```

3. Run the Python file:

```bash
  python data_analyzer.py
```

---

## Learning Objectives

This project was developed to practice:

- Data manipulation using lists
- Recursive programming techniques
- Functional programming with lambda expressions
- Sorting operations
- Menu-driven application design
- Basic statistical analysis in Python

---

## Author

Rishit Rajput

Python Mini Project