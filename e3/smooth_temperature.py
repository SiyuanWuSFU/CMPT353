import sys
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.nonparametric.smoothers_lowess import lowess
import numpy as np
from pykalman import KalmanFilter

filename1 = sys.argv[1]

cpu_data = pd.read_csv(filename1)

plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
cpu_data['timestamp']=cpu_data.timestamp.astype('datetime64[m]')
cpu_data['timestamp']=cpu_data.timestamp.values.astype(np.int64)

"""
plt.plot(cpu_data['timestamp'], cpu_data['cpu_percent'], 'b.', alpha=0.5)
plt.savefig('cpu_percent.png')
plt.plot(cpu_data['timestamp'], cpu_data['sys_load_1'], 'b.', alpha=0.5)
plt.savefig('sys_load_1.png')
plt.plot(cpu_data['timestamp'], cpu_data['fan_rpm'], 'b.', alpha=0.5)
plt.savefig('fan_rpm.png')
"""








plt.plot(cpu_data['timestamp'], cpu_data['temperature'], 'b.', alpha=0.5)
filtered = lowess(cpu_data['temperature'] ,cpu_data['timestamp'], frac = 0.05)
plt.plot(filtered[:,0],filtered[:,1], 'r-', linewidth = 3)
plt.legend(['Observation data','LOESS Smoothing'])


###############################################
kalman_data = cpu_data[['temperature', 'cpu_percent', 'sys_load_1', 'fan_rpm']]
#print(np.std(cpu_data['cpu_percent']))
initial_state = kalman_data.iloc[0]
o_covariance = np.diag([20, 50, 30, 200]) ** 2 # TODO: shouldn't be zero
t_covariance = np.diag([5, 5, 2, 20]) ** 2 # TODO: shouldn't be zero
transition = [[0.97, 0.5, 0.2, -0.001], [0.1, 0.4, 2.2, 0], [0,0, 0.95, 0], [0, 0, 0, 1]] # TODO: shouldn't (all) be zero

kf = KalmanFilter(initial_state_mean = initial_state,
                    initial_state_covariance = o_covariance,
                    observation_covariance = o_covariance,
                    transition_covariance = t_covariance,
                    transition_matrices = transition )
kalman_smoothed, _ = kf.smooth(kalman_data)
plt.subplot(1, 2, 2)
plt.plot(cpu_data['timestamp'], cpu_data['temperature'], 'b.', alpha=0.5)
plt.plot(cpu_data['timestamp'], kalman_smoothed[:, 0], 'g-',linewidth = 3)
plt.legend(['Observation data','Kalman Smoothing'])
#plt.show()
plt.savefig('cpu.svg') # for final submission
