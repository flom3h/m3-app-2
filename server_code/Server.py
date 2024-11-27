import anvil.files
from anvil.files import data_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import sqlite3

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#

@anvil.server.callable
def get_user(username, password):
  conn =  con = sqlite3.connect(data_files["SQL_Injection_database.db"])
  cursor = conn.cursor()
  try:
    res = list(cursor.execute(f"SELECT username FROM Users WHERE username = '{username}' AND password = '{password}'"))
    if res:
      return True, f"SELECT username FROM Users WHERE username = '{username}' AND password = '{password}'"
    else:
      return False, f"SELECT username FROM Users WHERE username = '{username}' AND password = '{password}'"
  except:
    print("Login Failed")
    