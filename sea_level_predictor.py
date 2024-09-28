import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('https://docs.google.com/spreadsheets/d/1ltcVfh_sMG8CBbLG7hBE9Nr1lASNoIeGlBTXjjINk_Y/export?format=csv')
    years_extended1 = np.arange(1880, 2051, 1)
    years_extended2 = np.arange(2000, 2051, 1)
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
  
    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    
    # Create first line of best fit
    res = linregress(x, y)
    line = [res.slope*x + res.intercept for x in years_extended1]
    ax.plot(years_extended1, line, color = 'r')
    ax.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
   
    # Create second line of best fit
    res1 = linregress(x[120:], y[120:])
    line = [res1.slope*x + res1.intercept for x in years_extended2]
    ax.plot(years_extended2, line, color = 'g')
  
    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.xlim(1850, 2075)
   
    # Save plot and return data for testing (DO NOT MODIFY)
    fig.savefig('sea_level_plot.png')
    return plt.gca()
  
draw_plot()
plt.show()