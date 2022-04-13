""" Flow analysis using Q+MONI data from ISOVER """
from turtle import color
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

# #reading data flow
# raw_data1 = pd.read_csv("Total flow_2021_09_04_00_00-2022_04_04_23_59.csv")
# print(raw_data1)
# raw_data1.to_csv('IsoverDataTotalFlow.csv', header=False, index=False)
# #reading data power
# raw_data = pd.read_csv("Total power_2021_09_04_00_00-2022_04_04_23_59.csv")
# print(raw_data)
# raw_data.to_csv('IsoverDataTotalPower.csv', header=False, index=False)

#flow
raw_dataflow = pd.read_csv("IsoverDataTotalFlow.csv", index_col=False)
dataflow = raw_dataflow['Date;Total flow (#1+#6+...+#15) / m3/min'].str.split(';', expand=True)
#power
raw_datapower = pd.read_csv("IsoverDataTotalPower.csv", index_col=False)
datapower = raw_datapower['Date;Total power / kW'].str.split(';', expand=True)
#merge
dataraw = dataflow.merge(datapower, on=0)


def estimate_coef(x, y):
    # number of observations/points
    n = np.size(x)
 
    # mean of x and y vector
    m_x = np.mean(x)
    m_y = np.mean(y)
 
    # calculating cross-deviation and deviation about x
    SS_xy = np.sum(y*x) - n*m_y*m_x
    SS_xx = np.sum(x*x) - n*m_x*m_x
 
    # calculating regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1*m_x
 
    return (b_0, b_1)
 
def plot_regression_line(x, y, b):
    # plotting the actual points as scatter plot
    plt.scatter(x, y, color = "m",
               marker = "o", s = 30)
 
    # predicted response vector
    y_pred = b[0] + b[1]*x
 
    # plotting the regression line
    plt.plot(x, y_pred, color = "g")
 
    # putting labels
    plt.xlabel('x')
    plt.ylabel('y')
 
    # function to show plot
    plt.show()
 
def main():
    # observations / data
    x_list =  list(map(float, dataraw["1_x"].values))
    x = np.array(x_list)
    print(x)
    y_list = list(map(float, dataraw["1_y"].values))   
    y = np.array(y_list)
    print(y)
 
    # estimating coefficients
    b = estimate_coef(x, y)
    print("Estimated coefficients:\nb_0 = {}  \
          \nb_1 = {}".format(b[0], b[1]))
 
    # plotting regression line
    plot_regression_line(x, y, b)
 
if __name__ == "__main__":
    main()
