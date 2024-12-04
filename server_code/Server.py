import anvil.files
from anvil.files import data_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import sqlite3

@anvil.server.callable
def get_user(username, password):
    conn = sqlite3.connect(data_files["SQL_Injection_database.db"])
    cursor = conn.cursor()
    try:
        query = f"SELECT username FROM Users WHERE username = '{username}' AND password = '{password}'"
        res = cursor.execute(query)
        rows = cursor.fetchall()  # Fetch all matching rows
        if rows:  # Check if any rows were returned
            return True, query  # Return success and the query
        else:
            return False, query  # Return failure and the query
    except Exception as e:
        return False, str(e)  # Handle exceptions gracefully

@anvil.server.callable
def get_all_users(username, password):
    conn = sqlite3.connect(data_files["SQL_Injection_database.db"])
    cursor = conn.cursor()
    try:
        query = f"SELECT username, balance FROM Users WHERE {account_condition}"
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows  # Return the query results as a list of tuples
    except Exception as e:
        return str(e)  # Return error message for debugging
    finally:
        conn.close()  # Close the database connection

