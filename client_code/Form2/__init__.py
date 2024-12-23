from ._anvil_designer import Form2Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Form2(Form2Template):
  
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.url = anvil.js.window.location.href
    self.accNo = anvil.server.call('getQuery',self.url)
    if (self.accNo == None):
      self.label_1.text = "Login Successful but AccountNo was not passed."
    else:
      res = anvil.server.call('getUsrId', self.accNo)
      self.label_1.text = res
    
    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    anvil.server.call('resetSession')
    open_form('Form1')

  