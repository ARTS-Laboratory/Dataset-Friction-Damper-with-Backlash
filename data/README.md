# Data

## [Dataset 1](dataset-1)
* Dataset added July 22, 2022, from testing at Lehigh. 
* Access each dataset by loading the .json file for each test. Data is stored in a matrix with columns time (s), displacement (in), friction force (kip), velocity (in/s), actuatator force 1 (lb), actuator force 2 (lb). 
* See `example.py` in the directory for how to load tests.

## [Dataset 2](dataset-2)
* Dataset from tests done in April 2023.
* Access each dataset by loading the .json file for each test. Data is stored in a matrix with columns time (s), displacement (in), friction force (kip), velocity (in/s), actuatator force 1 (lb), actuator force 2 (lb). 
* For characterization tests: sinusoidal signal varied in amplitude: (0.5 in, 1 inch, 1.5 inch), frequency: (0.1 Hz, 0.25 Hz, 0.5 Hz, 1 Hz, 2 Hz) and band tension (0 lb, 30 lb, 36 lb).
* Five tests excluded because of limitation of test setup: (1.5 in, 2 Hz, 0 lb), (1 in, 2 Hz, 30 lb), (1.5 in, 2 Hz, 30 lb), (1 in, 2 Hz, 36 lb), (1.5 in, 2 Hz, 36 lb).
