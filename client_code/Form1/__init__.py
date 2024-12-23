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
    if anvil.server.call('check_login_status'):
      open_form('Form2')
    else:
      set_url_hash()

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    username = self.text_box_1.text
    password = self.text_box_2.text
    login_state = anvil.server.call("login", password, username, self.check_box_1.checked)
    if not login_state[1]:
      alert(login_state[0], title="Login Failed")
    else:
      res = anvil.server.call('getAccno', username, password)
      if res is not None:
        set_url_hash(f'?AccountNo={res}')
      open_form('Form2')
      
      
      

    
