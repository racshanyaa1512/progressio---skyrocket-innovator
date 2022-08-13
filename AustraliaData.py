from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt
Australia= Tk()
Australia.geometry('1120x630')
Australia.title('Australia - Data Graph')

df = pd.read_csv('AustraliaDB.csv')
plt.hist(df.AverageTemperature)
plt.show()