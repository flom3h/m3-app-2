from ._anvil_designer import Form3Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Form3(Form3Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    print(properties.get('login_state'))
    # Any code you write here will run before the form opens.
    AccountState = properties.get("AccountState")
    accNo = AccountState[1]
    accState = AccountState[0]
    self.accountNo_set(accNo,accState)
    state = self.accountNo_check(accNo)
    self.rich_text_1.content= f"{properties.get('login_state')}"
    self.rich_text_2.content= state

  def button_1_click(self, **event_args):
    anvil.server.call('del_session')
    open_form('Form1')
   
    

  def accountNo_set(self, accNo, accState):
    if accState:
      set_url_hash(f'#AccountNo={accNo[0]}')
    else:
      pass
      
  def accountNo_check(self, accNo):
    print(get_url_hash(), f'AccountNo={accNo}')
    if get_url_hash() == f'AccountNo={accNo[0]}':
      return "YOU OWN THE DATABASE!"

    return "AccountNo NOT PASSED"
    
      