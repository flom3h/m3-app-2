from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.
    state = anvil.server.call('get_login_state')
    if state is True:
      open_form('Form2')


  def button_1_click(self, **event_args):
    username = self.text_box_1.text
    passwort = self.text_box_2.text
    Form2 = open_form('Form2')
    Form2.label_1.text =  anvil.server.call("get_user",username, passwort)

  def check_box_1_change(self, **event_args):
    
    pass

    