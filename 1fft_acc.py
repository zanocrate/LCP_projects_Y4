import numpy as np
import matplotlib.pyplot as plt 
from scipy import fft 
import pandas as pd

sampling_rate = 200 # should be 200 Hz from README1.txt
df=pd.read_csv("center_sternum.txt",sep=None,engine='python')
df['time_s'] = np.arange(0,df.shape[0])/100 # let's construct the time axis, with each sampling separated by a 100th of a second (because sampling rate is 100 Hz)
df=df.set_index('time_s')

# data for first time window
df1=df.loc[0:12][['AccX','AccY','AccZ','GyroX','GyroY','GyroZ','MagnX','MagnY','MagnZ']]
df1.plot(y=['AccX'])
plt.show()

accx=df1['AccX'].values
fft_accx=fft.fft(accx)

plt.plot(fft_accx)
plt.show()