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
def get_query_params(url):
  query = url.split('?')[-1] if '?' in url else ''
  query = urllib.parse.parse_qs(query)
  return query
  
@anvil.server.callable
def get_data_accountno(accountno):
  conn = sqlite3.connect(data_files["database.db"])
  cursor = conn.cursor()
  querybalance = f"SELECT balance FROM Balances WHERE AccountNo = {accountno}"
  queryusername = f"SELECT username FROM Users WHERE AccountNo = {accountno}"
  
  try:
   return list(cursor.execute(querybalance)) + list(cursor.execute(queryusername))
  except:
    return ""
