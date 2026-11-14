# OOP Data Processing Lab

## 1. Lab Overview

This lab focuses on Object-Oriented Programming (OOP) in Python by organizing data processing operations into reusable classes.

The program loads city and country data from CSV files and stores them in a database. It supports filtering, aggregating, searching, and joining tables using a common key.

The main objective is to understand how multiple tables can be managed and combined using OOP concepts.

## 2. Project Structure

```text
data-processing-lab/
│
├── README.md
├── Cities.csv
├── Countries.csv
└── data_processing.py
```

- `README.md`: Project documentation.
- `Cities.csv`: Dataset containing city information.
- `Countries.csv`: Dataset containing country information.
- `data_processing.py`: Python program containing the data loader, database, and table classes.

## 3. Design Overview

### DataLoader Class

The `DataLoader` class handles loading CSV data files.

**Attributes:**
- `base_path`: The directory used to locate CSV files.

**Methods:**
- `__init__(base_path=None)`: Initializes the data loader with a base directory.
- `load_csv(filename)`: Reads a CSV file and returns its contents as a list of dictionaries.

### DB Class

The `DB` class manages multiple tables in a database.

**Attributes:**
- `tables`: A dictionary used to store tables by their names.

**Methods:**
- `__init__()`: Initializes an empty database.
- `insert(table)`: Inserts a table into the database.
- `search(name)`: Searches for and returns a table by its name.

### Table Class

The `Table` class stores table data and provides data processing operations.

**Attributes:**
- `table_name`: The name of the table.
- `table`: A list of dictionaries containing the table data.

**Methods:**
- `__init__(table_name, table)`: Initializes a table with its name and data.
- `__str__()`: Returns the table name and its data as a string.
- `filter(condition)`: Returns a new table containing rows that satisfy the given condition.
- `aggregate(aggregation_function, aggregation_key)`: Extracts values from a specified column and applies an aggregation function.
- `join(other_table, key)`: Joins two tables using a common key and returns a new table containing the combined data.

## 4. How to Test and Run

### Requirements

- Python 3
- `Cities.csv`
- `Countries.csv`

### Run the Program

1. Open the project folder in Visual Studio Code.
2. Open the terminal.
3. Run the following command:

```bash
python data_processing.py
```

### Expected Operations

The program demonstrates the following operations:

1. Display all cities in Italy.
2. Calculate the average temperature of cities in Italy.
3. Display all non-EU countries.
4. Count the number of countries that have a coastline.
5. Join the cities and countries tables using the `country` key.
6. Display cities with temperatures below 5.0 in non-EU countries.
7. Find the minimum and maximum temperatures for cities in EU countries without coastlines.