# SQL Query Converter
=====================

## Overview
-----------

This script converts SQL queries that use f-strings into queries using % formatting and tuples. This helps prevent SQL injection vulnerabilities by ensuring that user input is properly sanitized.

## Features
------------

- **F-String Cleaning**: Removes f-string syntax from input queries.
- **Placeholder Extraction**: Identifies placeholders in the query using regular expressions.
- **Placeholder Replacement**: Replaces placeholders with '%s' for safe parameter passing.
- **Tuple Creation**: Generates a tuple string for the placeholders.

## Usage
-----

1. **Run the Script**: Execute the Python script.
2. **Input Query**: Paste a non-parametrized SQL query using f-strings.
3. **Output**: The script will output the parametrized query with a tuple for placeholders.

## Requirements
------------

- Python 3.x
- `re` module (part of the Python Standard Library)

## Example Output
----------------

The script will output a modified SQL query that is safer against SQL injection attacks.

## Code Structure
----------------

The script uses a modular approach with functions for each step of the conversion process.

## Contributing
------------

Contributions are welcome! Feel free to suggest improvements or enhancements.


