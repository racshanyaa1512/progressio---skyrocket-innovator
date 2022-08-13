from tkinter import *
import pandas as pd
from functools import partial

CountryWiseSearch = Tk()
CountryWiseSearch.geometry('1120x630')
CountryWiseSearch.title('EnvirAware Country Wise Search')

def movetoAfghanistanPage():
    import AfghanistanData
def movetoAngolaPage():
    import AngolaData
def movetoAustraliaPage():
    import AustraliaData
def movetoBangladeshPage():
    import BangladeshData
def movetoBrazilPage():
    import BrazilData
def movetoBurmaPage():
    import BurmaData

Afghanistan = Button(CountryWiseSearch, text="Afghanistan", command=movetoAfghanistanPage).grid(row=40, column=20)
Angola = Button(CountryWiseSearch, text="Angola", command=movetoAngolaPage).grid(row=41, column=20)
Australia = Button(CountryWiseSearch, text="Australia", command=movetoAustraliaPage).grid(row=43, column=20)
Bangladesh = Button(CountryWiseSearch, text="Bangladesh", command=movetoBangladeshPage).grid(row=44, column=20)
Brazil = Button(CountryWiseSearch, text="Brazil", command=movetoBrazilPage).grid(row=45, column=20)
Burma = Button(CountryWiseSearch, text="Burma", command=movetoBurmaPage).grid(row=46, column=20)






