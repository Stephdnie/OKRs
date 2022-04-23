import matplotlib.pyplot as plt
import pandas as pd

power = pd.read_csv("xrayIsoverCompressorRealPower.csv", header=None, index_col=False)
unloaded = power[power[0:1] < 88.75]
loaded = power[power[0:1] >= 88.75]

flow = pd.read_csv("xrayIsoverTotalFlow.csv", header=None, index_col=False)

