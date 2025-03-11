# Helper Script to Rewrite SQL Queries
# This script converts SQL queries using f-strings to those using % formatting and tuples,
# helping to avoid SQL injection vulnerabilities.

import re


def get_non_parametrized_query():
    """Gets a non-parametrized SQL query from user input."""
    return input("Paste a non-parametrized SQL query that uses f-strings: ")


def clean_f_string(sql_query):
    """
    Cleans the f-string syntax from the SQL query.

    :param sql_query: The SQL query to clean.
    :return: The cleaned SQL query.
    """
    sql_query = sql_query.replace("(f\"", "(\"")
    sql_query = sql_query.replace("\")", "\"")
    sql_query = sql_query.replace("'{", "{")
    sql_query = sql_query.replace("}'", "}")
    return sql_query


def extract_placeholders(sql_query):
    """
    Extracts placeholders from the SQL query using a regular expression.

    :param sql_query: The SQL query to extract placeholders from.
    :return: A list of placeholder names.
    """
    pattern = r"\{([^}]+)\}"
    return re.findall(pattern, sql_query)


def replace_placeholders(sql_query, placeholders):
    """
    Replaces placeholders in the SQL query with '%s'.

    :param sql_query: The SQL query to modify.
    :param placeholders: A list of placeholder names.
    :return: The modified SQL query.
    """
    for placeholder in placeholders:
        sql_query = sql_query.replace("{" + placeholder + "}", "%s")
    return sql_query


def create_params_tuple_str(placeholders):
    """
    Creates a string representation of a tuple for the placeholders.

    :param placeholders: A list of placeholder names.
    :return: A string representation of a tuple.
    """
    return "(" + ", ".join(placeholders) + ")"


def main():
    while True:
        sql_query = get_non_parametrized_query()
        sql_query = clean_f_string(sql_query)

        placeholders = extract_placeholders(sql_query)
        sql_query = replace_placeholders(sql_query, placeholders)

        params_tuple_str = create_params_tuple_str(placeholders)

        parametrized_query = sql_query + ", " + params_tuple_str
        print("\n", parametrized_query)

        decision = input("Do you want to continue? (y/n): ")
        if decision.strip().lower() == 'y':
            continue
        else:
            break


if __name__ == "__main__":
    main()
