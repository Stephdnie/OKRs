import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

""" # reading compressor real
raw_data1 = pd.read_csv("Compressor real power_2021_09_13_00_00-2022_04_13_23_59.csv")
print(raw_data1)
raw_data1.to_csv('IsoverCompressorRealPower.csv', header=False, index=False)

# reading data flow
raw_data = pd.read_csv("Total flow_2021_09_13_00_00-2022_04_13_23_59.csv")
print(raw_data)
raw_data.to_csv('IsoverTotalFlow.csv', header=False, index=False) """

""" # reading compressor real
raw_data1 = pd.read_csv("Compressor real power_2021_10_01_00_00-2021_10_15_00_00.csv")
raw_data1.to_csv('xrayIsoverCompressorRealPower.csv', header=False, index=False)

# reading data flow
raw_data = pd.read_csv("Total flow_2021_10_01_00_00-2021_10_15_00_00.csv")
raw_data.to_csv('xrayIsoverTotalFlow.csv', header=False, index=False) """

""" # reading compressor real
raw_data1 = pd.read_csv("Result_3.csv")
print(raw_data1)
raw_data1.to_csv('xrayIsoverCompressorRealPower.csv', header=False, index=False)
print(raw_data1)

# reading data flow
raw_data = pd.read_csv("Total_decimal.csv")
raw_data.to_csv('xrayIsoverTotalFlow.csv', header=False, index=False)
print(raw_data)
 """

power = pd.read_csv("xrayIsoverCompressorRealPower.csv", header=None, index_col=False)
#power = raw_power['Date;Real power sum Compressor 71 ZR355 / kW;Real power sum Compressor 72 ZR355 / kW;Real power sum Compressor 73 ZR400 VSD / kW;Real power sum Compressor 74 ZR132 VSD FF / kW'].str.split(';', expand=True)
print(power[0])
unloaded = power[power < 1]
print(unloaded)
loaded = power[power >= 1]
print(loaded)
powerkomp1 = power[0]
powerkomp1loaded = powerkomp1[powerkomp1 >= 88.75]
powerkomp2 = power[1]
powerkomp2loaded = powerkomp2[powerkomp2 >= 88.75]
powerkomp3 = power[2]
powerkomp3loaded = powerkomp3[powerkomp3 >= 98]
powerkomp4 = power[3]
powerkomp4loaded = powerkomp4[powerkomp4 >= 28.25]

# Plotting both the curves simultaneously
plt.plot(powerkomp2, color='r', label='totalPower')
plt.plot(powerkomp2loaded, color='g', label='loadedPower')
  
# Naming the x-axis, y-axis and the whole graph
plt.xlabel("Time")
plt.ylabel("Power")
plt.title("Total power and loaded power - Kompressor 72")
  
# Adding legend, which helps us recognize the curve according to it's color
plt.legend()
  
# To load the display window
plt.show()

# Initialise the subplot function using number of rows and columns
figure, axis = plt.subplots(2, 2)

axis[0, 0].plot(powerkomp1, color = 'r', linestyle = 'dashed',
         marker = 'o', label= 'totalPower')
axis[0, 0].plot(powerkomp1loaded, color = 'g', linestyle = 'dashed',
         marker = 'o', label = 'loadedPower')
axis[0, 0].set_title("Kompressor 71")
axis[0, 0].set_xlabel("Time")
axis[0, 0].set_ylabel("Power")

axis[0, 1].plot(powerkomp2, color = 'r', linestyle = 'dashed',
         marker = 'o', label= 'totalPower')
axis[0, 1].plot(powerkomp2loaded, color = 'g', linestyle = 'dashed',
         marker = 'o', label = 'loadedPower')
axis[0, 1].set_title("Kompressor 72")
axis[0, 1].set_xlabel("Time")
axis[0, 1].set_ylabel("Power")


axis[1, 0].plot(powerkomp3, color = 'r', linestyle = 'dashed',
         marker = 'o', label= 'totalPower')
axis[1, 0].set_title("Kompressor 73")
axis[1, 0].set_xlabel("Time")
axis[1, 0].set_ylabel("Power")

axis[1, 1].plot(powerkomp4, color = 'r', linestyle = 'dashed',
         marker = 'o', label= 'totalPower')
axis[1, 1].set_title("Kompressor 74")
axis[1, 1].set_xlabel("Time")
axis[1, 1].set_ylabel("Power")


plt.show()
plt.legend()




fig, axes = plt.subplots(nrows=2, sharex=True)
axes[0].plot(unloaded, 'bo')
axes[1].plot(loaded, 'ro')
plt.show()

# power[0].plot()
# plt.show()
#komp71_list = list(map(float, power[1].values))   
#komp72_list = list(map(float, power[2].values))   
#komp73_list = list(map(float, power[3].values))   
#komp74_list = list(map(float, power[4].values))   
#y = np.array(y_list)
#np.size(power)

# raw_power = pd.read_csv("xrayIsoverCompressorRealPower.csv", index_col=False)
# power = raw_power['Date;Real power sum Compressor 71 ZR355 / kW;Real power sum Compressor 72 ZR355 / kW;Real power sum Compressor 73 ZR400 VSD / kW;Real power sum Compressor 74 ZR132 VSD FF / kW'].str.split(';', expand=True)
# print(power)
# komp71_list = list(map(float, power[1].values))   
# komp72_list = list(map(float, power[2].values))   
# komp73_list = list(map(float, power[3].values))   
# komp74_list = list(map(float, power[4].values))   
# #y = np.array(y_list)
# #np.size(power)

# raw_flow = pd.read_csv("xrayIsoverTotalFlow.csv", index_col=False)
# flow = raw_flow['Date;Total flow (#1+#6+...+#15) / m3/min'].str.split(';', expand=True)
# print(flow)
# x_list =  list(map(float, flow[1].values))
# x = np.array(x_list)
# print(x)

