from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt
Afghanistan= Tk()
Afghanistan.geometry('1120x630')
Afghanistan.title('Afghanistan - Data Graph')

df = pd.read_csv('AfghanistanDB.csv')
plt.hist(df.AverageTemperature)
plt.show()



