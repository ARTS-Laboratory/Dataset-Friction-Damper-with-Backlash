import json
import matplotlib.pyplot as plt
import numpy as np
"""
How to use the friction dataset, plotting hysteresis curves for a 
characterization and a wind profile.

Author: Daniel Coble
"""

test_name = "0.05Hz20lbtension"

with open("./characterization datasets/%s.json"%test_name) as f:
    characterization_data = json.load(f)
    f.close()
print("keys: ")
for key in characterization_data.keys():
    print(key)

data = np.array(characterization_data["data"])
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

test_name = "test1"

with open("./wind profiles/%s.json"%test_name) as f:
    wind_profile_data = json.load(f)
    f.close()

data = np.array(wind_profile_data["data"])
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