import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.files
from anvil.files import data_files
import anvil.server
import sqlite3
import urllib.parse

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#


@anvil.server.callable
def login_save(username, password):
    con = sqlite3.connect(data_files["database.db"])
    cur = con.cursor()
    query = "SELECT username, isAdmin FROM Users WHERE username = ? AND password = ?"
    cur.execute(query, (username, password))
    result = cur.fetchone()
    con.close()
    if result == None:
      return f"Login Fail: {query}"
    else:
      anvil.server.session["login"] = True
      return f"Login Sucsess {query}"

@anvil.server.callable
def login_unsave(username,password):
  con = sqlite3.connect(data_files["database.db"])
  cur = con.cursor()
  print(username)
  query = f"SELECT username, isAdmin FROM Users WHERE username = '{username}' AND password = '{password}'"
  cur.execute(query)
  reslut = cur.fetchone()
  con.close()
  if reslut == None:
    anvil.server.session["login"] = False
    return f"Login Fail: {query}, {reslut}"
  else:
    anvil.server.session["login"] = True
    return f"Login Sucsess {query}"

@anvil.server.callable
def get_accountNo(username, password):
  con = sqlite3.connect(data_files["database.db"])
  cur = con.cursor()
  print(username)
  query = "SELECT AccountNo FROM Users WHERE username = ? AND password = ?"
  cur.execute(query, (username, password))
  reslut = cur.fetchone()
  if reslut == None:
    return [False , ' ']
  else:
    return [True, reslut]
  con.close()


@anvil.server.callable
def get_login_state():
  if "login" not in anvil.server.session:
    anvil.server.session["login"] = False
    
  return anvil.server.session["login"]

@anvil.server.callable
def login_accNo(url):
    con = sqlite3.connect(data_files["database.db"])
    cur = con.cursor()
    url = get_accountNumber_from_query(url)
    if url is None:
        return "AccountNo Not passed"
    
    query_balance = f"SELECT balance FROM Balances WHERE AccountNo = {url}"
    query_user = f"SELECT username FROM Users WHERE AccountNo = {url}"
    
    try:
        balance = cur.execute(query_balance).fetchall()
        user = cur.execute(query_user).fetchall()
        
    except Exception as e:
        return f"User not found.<br>{query_user}<br>{query_balance}<br>{e}"
    # formatting start
    user = [u[0] for u in user if isinstance(u, tuple)]
    balance = [b[0] for b in balance if isinstance(b, tuple)]
    user = user[0] if len(user) == 1 else user
    balance = balance[0] if len(balance) == 1 else balance
    # formatting end
    if user:
        return f"Welcome {user}! Your balance is {balance}."
    else:
        return f"User not found.<br>{query_user}<br>{query_balance}"



def get_accountNumber_from_query(url):
  query_string = url.split('?')[-1] if '?' in url else ''
  if query_string :
    query_params = urllib.parse.parse_qs(query_string)
    if "AccountNo" in query_params:
      return query_params["AccountNo"][0]
  return None

@anvil.server.callable
def del_session():
  anvil.server.session["login"] = False
  
@anvil.server.callable
def current_state():
  return anvil.server.session["login"]
  