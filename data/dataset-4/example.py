import json
import matplotlib.pyplot as plt
import numpy as np
"""
How to use the friction dataset, plotting hysteresis curves and 
time-series data for a semi-active test profile.

Author: Parker Huggins
"""

test_name = "harmonic0.015forward"

with open("%s.json"%test_name) as f:
    semiactive_data = json.load(f)['data']
    f.close()

data = np.array(semiactive_data)
t = data[:,0] # time (s)
x = data[:,1] # MTS actuator displacement (in)
F = data[:,2] # friction force (kip)
v = data[:,3] # velocity (in/s)
x_act1 = data[:,4] # first actuator position (in)
x_act2 = data[:,5] # second actuator position (in)
F_act1 = data[:,6] # first actuator force (lb)
F_act2 = data[:,7] # second actuator force (lb)

# plot hysteresis loops
plt.figure(figsize=(6, 4))
plt.plot(x, F)
plt.ylabel("force (kip)")
plt.xlabel("displacement (in)")
plt.title("Force-displacement of semi-active data")
plt.tight_layout()

plt.figure(figsize=(6, 4))
plt.plot(v, F)
plt.ylabel("force (kip)")
plt.xlabel("velocity (in/s)")
plt.title("Force-velocity of semi-active data")
plt.tight_layout()

# plot actuator positions
plt.figure(figsize=(6, 4))
plt.plot(t,x_act1,label="actuator 1")
plt.plot(t,x_act2,label="actuator 2")
plt.legend()
plt.ylabel("position (in)")
plt.xlabel("time (s)")
plt.title("Actuator positions of semi-active data")

# plot friction and actuator forces
plt.figure(figsize=(6, 4))
plt.plot(t,F,label="damping force")
plt.plot(t,F_act1/1000,label="actuator 1")
plt.plot(t,F_act2/1000,label="actuator 2")
plt.legend()
plt.ylabel("friction force (kip)")
plt.xlabel("time (s)")
plt.title("Force-time of semi-active data")
