import anvil.files
from anvil.files import data_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import sqlite3
import urllib.parse

@anvil.server.callable
def get_login_state():
  if "login" not in anvil.server.session:
    anvil.server.session["login"] = False
  return anvil.server.session["login"]
@anvil.server.callable

@anvil.server.callable
def get_user(username, password):
    conn = sqlite3.connect(data_files["database.db"])
    cursor = conn.cursor()
    try:
        query = "SELECT username FROM Users WHERE username = ? AND password = ?"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()
        
        if result and result[0] == username:
            anvil.server.session["login"] = True
            return "Login successful"
        else:
            return "Invalid username or password."
    except Exception as e:
        return f"An error occurred: {str(e)}"


@anvil.server.callable
def get_query_params(url):
  query = url.split('?')[-1] if '?' in url else ''
  query = urllib.parse.parse_qs(query)
  return query
  
@anvil.server.callable
def get_data_accountno(accountno):
  conn = sqlite3.connect(data_files["database.db"])
  cursor = conn.cursor()
  queryacct = f"SELECT balance FROM Balances WHERE AccountNo = {accountno}"
  queryusr = f"SELECT username FROM Users WHERE AccountNo = {accountno}"
  
  try:
   return list(cursor.execute(queryacct)) + list(cursor.execute(queryusr))
  except:
    return ""

@anvil.server.callable
def logout():
  anvil.server.session["login"] = False