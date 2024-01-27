import json
import matplotlib.pyplot as plt
import numpy as np
"""
How to use the friction dataset, plotting hysteresis curves for a 
characterization and a wind profile.

Author: Daniel Coble
"""

test_name = "DuzceDBE"

with open("%s.json"%test_name) as f:
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
plt.xlabel("velocity (in/s)")
plt.title("Force-velocity of characterization data")
plt.tight_layout()


plt.figure(figsize=(6, 4))
plt.plot(t, F_act1/1000,label="actuator 1")
plt.plot(t, F_act2/1000,label="actuator 2")
plt.legend()
plt.ylabel("force (kip)")
plt.xlabel("time (s)")
plt.title("Actuator force-time of characterization data")
plt.tight_layout()


plt.figure(figsize=(6, 4))
plt.plot(t, -F,label="damping force")
plt.plot(t, F_act1/1000,label="actuator 1")
plt.plot(t, F_act2/1000,label="actuator 2")
plt.legend()
plt.ylabel("force (kip)")
plt.xlabel("time (s)")
plt.title("Force-time of characterization data")
plt.tight_layout()



















