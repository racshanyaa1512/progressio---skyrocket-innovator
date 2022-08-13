from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt
Angola= Tk()
Angola.geometry('1120x630')
Angola.title('Angola - Data Graph')

df = pd.read_csv('AngolaDB.csv')
plt.hist(df.AverageTemperature)
plt.show()