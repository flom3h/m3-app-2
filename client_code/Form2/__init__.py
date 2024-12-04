from ._anvil_designer import Form2Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Form2(Form2Template):
  def __init__(self, status, pare, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.label_1.text = status
    self.label_2.text = pare
    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    open_form('Form1')

