import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 

sampling_rate = 200 # should be 200 Hz from README1.txt
df=pd.read_csv("center_sternum.txt",sep=None,engine='python')
df['time_s'] = np.arange(0,df.shape[0])/100 # let's construct the time axis, with each sampling separated by a 100th of a second (because sampling rate is 100 Hz)
df=df.set_index('time_s')

acc=df.loc[0:20][['AccX','AccY','AccZ']].values
print(acc.shape)
print(df.columns)

ax= plt.subplot(projection='3d')
ax.scatter(acc[:,0],acc[:,1],acc[:,2],c=df.loc[0:20].index)
plt.show()

ax = plt.subplot()
df.plot(y=['AccX','AccY','AccZ'],ax=ax)
plt.show()