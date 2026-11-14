# OOP Data Processing Lab

## 1. Lab Overview

This lab focuses on converting procedural data processing code into an Object-Oriented Programming (OOP) style using Python.

The program loads city data from a CSV file and provides operations to filter and aggregate the data using classes and methods.

The main goal is to organize the code into reusable classes, making the data processing program easier to understand and maintain.

## 2. Project Structure

```text
data-processing-lab/
│
├── README.md
├── Cities.csv
└── data_processing.py
```

- `README.md`: Project documentation.
- `Cities.csv`: Dataset containing city information.
- `data_processing.py`: Python code for loading, filtering, and aggregating city data.

## 3. Design Overview

### DataLoader Class

The `DataLoader` class handles loading CSV data files.

**Attributes:**
- `base_path`: The directory used to locate CSV files.

**Methods:**
- `__init__(base_path=None)`: Initializes the data loader with a base directory. If no path is provided, it uses the directory containing the Python file.
- `load_csv(filename)`: Reads a CSV file and returns its contents as a list of dictionaries.

### Table Class

The `Table` class stores table data and provides operations for filtering and aggregating data.

**Attributes:**
- `name`: The name of the table.
- `table`: A list of dictionaries containing the table data.

**Methods:**
- `__init__(name, table)`: Initializes a table with its name and data.
- `filter(condition)`: Returns a new Table containing only rows that satisfy the given condition.
- `aggregate(aggregation_function, aggregation_key)`: Extracts values from the specified column and applies the given aggregation function.

## 4. How to Test and Run

### Requirements

- Python 3
- `Cities.csv` dataset

### Run the Program

1. Open the project folder in Visual Studio Code.
2. Open the terminal.
3. Run the following command:

```bash
python data_processing.py
```

### Expected Operations

The program demonstrates the following operations:

1. Calculate the average temperature of all cities.
2. Filter and display all cities in Germany.
3. Filter and display cities in Spain with temperatures above 12°C.
4. Count the number of unique countries.
5. Calculate the average temperature of cities in Germany.
6. Find the maximum temperature among cities in Italy.