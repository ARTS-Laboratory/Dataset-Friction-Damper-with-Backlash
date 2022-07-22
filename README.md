# Dataset-Friction-Damper-with-Backlash

This dataset comes from tests of the banded rotary friction device (BRFD), which exhibits hysteritic and backlash effects. 

## Device and Data
The BRFD is a semi active friction damper damper [1,2]. The device has heightened applicability compared to other damping
technologies due to its mechanical robustness,
technological simplicity, and high damping
performance.




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

### References

[1] Downey, A., Cao, L., Laflamme, S., Taylor, D., & Ricles, J. (2016). High capacity variable friction damper based on band brake technology. Engineering Structures, 113, 287-298.

[2] Stiles, M., & Subaihawi, S. L. Fabrication of a Semi-Active Controlled Friction Damper Device.

## Licensing and Citation

[![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg


Cite as:

@Misc{Coble2022DatasetFrictionDampery,   
  author = {Daniel Coble and Liang Cao and James Ricles and Austin Downey},   
  howpublished = {GitHub},  
  title  = {Dataset-Friction-Damper-with-Backlash},   
  year   = {2022},  
  groups = {{ARTS-L}ab},    
  url    = {https://github.com/ARTS-Laboratory/Dataset-Friction-Damper-with-Backlash},    
}
