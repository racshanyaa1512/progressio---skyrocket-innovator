from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt
Burma= Tk()
Burma.geometry('1120x630')
Burma.title('Burma - Data Graph')

df = pd.read_csv('BurmaDB.csv')
plt.hist(df.AverageTemperature)
plt.show()