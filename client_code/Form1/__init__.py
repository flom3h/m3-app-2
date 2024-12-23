from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    state = anvil.server.call('get_login_state')
    if state is True:
      open_form('Form2')
    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    username = self.text_box_1.text
    password = self.text_box_2.text
    if self.check_box_1.checked:
      login_state = anvil.server.call('login_save', username, password)
    else:
      login_state = anvil.server.call('login_unsave',username, password)

    if "Fail" not in login_state:
      open_form('Form3', login_state = login_state, AccountState = anvil.server.call('get_accountNo',username,password) )
    else:
      alert("Wrong Username or Password")

    
  