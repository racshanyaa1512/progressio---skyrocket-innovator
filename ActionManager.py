from tkinter import *
from functools import partial

ActionManager = Tk()
ActionManager.geometry('1120x630')
ActionManager.title('EnvirAware - Action Page')

def movetoCountryWiseSearchPage():
  import CountryWiseSearch
def movetoDisplayDatabase():
  import SituationFinder
CountryWiseSearch = Button(ActionManager, text="Search with Country ", command=movetoCountryWiseSearchPage).grid(row=40, column=8)
SituationFinder = Button(ActionManager, text="Display the Database", command=movetoDisplayDatabase).grid(row=40, column=9)