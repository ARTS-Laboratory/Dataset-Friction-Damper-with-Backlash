# Dataset-Friction-Damper-with-Backlash

This dataset comes from tests of the banded rotary friction device (BRFD), which exhibits hysteritic and backlash effects. 
<p align="center">
<img src="images/friction damper.jpg" alt="Front view of banded rotary friction device" width="400"/> <br> 
</p>

Characterization datasets were performed by moving the damper under a sinusoidal displacement such as shown below. The wind profile tests were performed in a hybrid test where displacment from a simulated structure under wind diplacement was fed into the damper. This test was performed in real-time so that reactions from the damper were captured and used in the structure simulation.
<p align="center">
<img src="images/displacement-profile.png" alt="sinusoidal displacement profile" width="400"/> <br> 
</p>

<p align="center">
<img src="images/force-displacement.png" alt="displacement hysteresis loop from characterization test" width="400"/>
<img src="images/force-velocity.png" alt="velocity hysteresis loop from characterization test" width="400"/>
<br> 
</p>

Access each dataset by loading the .json file for each test. Data is stored in a matrix with columns time (s), displacement (in), friction force (kip), velocity (in/s), actuatator force 1 (lb), actuator force 2 (lb). See `example.py` for how to load tests.
