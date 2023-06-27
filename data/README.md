# Data

## [Dataset 1](dataset-1)
* Dataset added July 22, 2022, from testing at Lehigh. 
* Access each dataset by loading the .json file for each test. Data is stored in a matrix with columns time (s), displacement (in), friction force (kip), velocity (in/s), actuatator force 1 (lb), actuator force 2 (lb). 
* See `example.py` in the directory for how to load tests.

## [Dataset 2](dataset-2)
* Dataset from tests done in April 2023.
* Access each dataset by loading the .json file for each test. Data is stored in a matrix with columns time (s), displacement (in), friction force (kip), velocity (in/s), actuatator force 1 (lb), actuator force 2 (lb).
### Characterization tests
* For characterization tests: sinusoidal signal varied in amplitude: (0.5 in, 1 inch, 1.5 inch), frequency: (0.1 Hz, 0.25 Hz, 0.5 Hz, 1 Hz, 2 Hz) and band tension (0 lb, 30 lb, 36 lb).
* Five tests excluded because of limitation of test setup: (1.5 in, 2 Hz, 0 lb), (1 in, 2 Hz, 30 lb), (1.5 in, 2 Hz, 30 lb), (1 in, 2 Hz, 36 lb), (1.5 in, 2 Hz, 36 lb).
* Seven tests (0.5 in, 0.1 Hz, 0 lb), (0.5 in, 0.25 Hz, 0 lb), (0.5 in, 0.5 Hz, 0 lb), (0.5 in, 1 Hz, 0 lb), (0.5 in, 2 Hz, 0 lb), (1 in, 0.1 Hz, 0 lb), (1 in, 0.25 Hz, 0 lb) appear to have an issue with incorrect measurement of band tension.
### Earthquake predefined displacements
* Six tests of the device under 36 lb band tension were performed from three earthquake displacements run with DBE and MCE scale factors.
* The displacement data was taken from hybrid simulation tests of the BRFD installed a two-story reinforced concrete building, but these tests are predefined displacements.

|Earthquake ID|Scale Factor (DBE level)|Earthquake Name|Year|Station Name|Magnitude|Mechanism|
|-------------|------------------------|---------------|----|------------|---------|---------|
|1|1.4199|Kocaeli Turkey|1999|Yarimca|7.51|strike slip|
|2|0.5076|Duzce Turkey|1999|Bolu|7.14|strike slip|
|3|1.0787|Imperial Valley-06|1979|El Centro Array #7|6.53|strike slip|

|Earthquake ID|Scale Factor (MCE level)|Earthquake Name|Year|Station Name|Magnitude|Mechanism|
|-------------|------------------------|---------------|----|------------|---------|---------|
|1|2.12985|Kocaeli Turkey|1999|Yarimca|7.51|strike slip|
|2|0.7614|Duzce Turkey|1999|Bolu|7.14|strike slip|
|3|1.61805|Imperial Valley-06|1979|El Centro Array #7|6.53|strike slip|

## [Dataset 3](dataset-3)
* Tests done in April 2023
* Characterization tests identical to Dataset 2 but only with 30 lb band tension.
* Six earthquake tests identical to Dataset 2 but with 30 lb band tension.
