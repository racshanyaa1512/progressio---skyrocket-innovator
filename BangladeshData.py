from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt
Bangladesh= Tk()
Bangladesh.geometry('1120x630')
Bangladesh.title('Bangladesh - Data Graph')

df = pd.read_csv('BangladeshDB.csv')
plt.hist(df.AverageTemperature)
plt.show()