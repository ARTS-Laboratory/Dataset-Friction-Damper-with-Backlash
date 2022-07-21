import json
import matplotlib.pyplot as plt
import numpy as np
"""
How to use the friction dataset, plotting hysteresis curves for the 
characterization data and wind profiles

Author: Daniel Coble
"""
with open("./data/characterization_dataset.json") as f:
    characterization_data = json.load(f)
    f.close()

print(characterization_data['dt'])

test_name = "0.05Hz20lbtension"
data = np.array(characterization_data[test_name])
t = data[:,0] # time (s)
x = data[:,1] # displacement (in)
F = data[:,2] # friction force (kip)
v = data[:,3] # velocity (in/s)
F_act1 = data[:,4] # first actuator force (lb)
F_act2 = data[:,5] # second actuator force (lb)

# plot hysteresis loops
plt.figure(figsize=(6, 4))
plt.plot(x, F)
plt.ylabel("force (kip)")
plt.xlabel("displacement (in)")
plt.title("Force-displacement of characterization data")
plt.tight_layout()

plt.figure(figsize=(6, 4))
plt.plot(v, F)
plt.ylabel("force (kip)")
plt.xlabel("velocity (in)")
plt.title("Force-velocity of characterization data")
plt.tight_layout()

# doing the same thing with the wind profiles

with open("./data/wind_profiles.json") as f:
    wind_profile_data = json.load(f)
    f.close()

print(wind_profile_data['sampling freq'])

test_name = "test1"
data = np.array(wind_profile_data[test_name])
t = data[:,0] # time (s)
x = data[:,1] # displacement (in)
F = data[:,2] # friction force (kip)
v = data[:,3] # velocity (in/s)
F_act1 = data[:,4] # first actuator force (lb)
F_act2 = data[:,5] # second actuator force (lb)

# plot hysteresis loops
plt.figure(figsize=(6, 4))
plt.plot(x, F)
plt.ylabel("force (kip)")
plt.xlabel("displacement (in)")
plt.title("Force-displacement of wind loading")
plt.tight_layout()

plt.figure(figsize=(6, 4))
plt.plot(v, F)
plt.ylabel("force (kip)")
plt.xlabel("velocity (in)")
plt.title("Force-velocity of wind loading")
plt.tight_layout()