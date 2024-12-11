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

def get_user(username, passwort):
  conn = sqlite3.connect(data_files["database.db"])
  cursor =  conn.cursor()
  try:
      res = cursor.execute(f"SELECT username FROM Users WHERE username = '{username}' AND password = '{passwort}'")
      result = cursor.fetchone()
      if result:
        res = "Login successful"
        anvil.server.session["login"] = True
      else:
        raise ValueError("Empty Data")
  except Exception:
      res = f"Login not successful: \n SELECT username FROM Users WHERE username = '{username}' AND password = '{passwort}'"
  return res

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