# KUBIOS Import & Export for Python

This Python package enables easy exportation of NN/RR interval series or signals to KUBIOS HRV friendly files and structured formats and to import HRV analysis results from KUBIOS HRV report files in .txt format.

The exported signals are stored in the Type 1 format as presented on page 14 and 15 of the [KUBIOS User Guide](https://www.kubios.com/downloads/Kubios_HRV_Users_Guide.pdf).

## How to Use this Package

#### export_nni()
Use the ``export_nni()``` function to export a series of NN/RR interval or ECG signal data to a KUBIOS readable file format.
```python
import numpy as np
from kubios import export_nni

# Load NNI series
nni = np.load('SampleSeries.npy')

# Export NNI series
export_nni(nni)
```

Use the ```output_path``` variable to specify the file path where to store the exported file and ```output_file``` to specify the file name. Use only the ```output_file``` if you want to set the absolute file path in a single string. If no value for the ```output_file``` is provided, a file name (incl. time stamp) will automatically be generated.

```python
import numpy as np
from kubios import export_nni

# Load NNI series
nni = np.load('SampleSeries.npy')

# Export NNI series with specific file name
export_nni(nni, output_file='export.txt)

# Export NNI series to specific path & specific file name
export_nni(nni, output_path='/my/favorite/path/', output_file='export.txt')

# Export NNI series to specific path with automatic file name generation
export_nni(nni, output_path='/my/favorite/path/')
```

#### import_report()
Use the ```import_report()``` function to read a KUBIOS HRV report files in .txt format. The results will be returned in a Python dictionary.
```python
from kubios import import_report

# Import HRV results from KUBIOS report
results = import_report('SampleReport.txt')

# Get SDNN value
results['sdnn']
```

## Dependencies
- [numpy](http://www.numpy.org)

## Context of this Work
This package is under development within the scope of my master thesis _"Development of an Open-Source Python Toolbox for Heart Rate Variability (HRV)"_ at the [University of Applied Sciences Hamburg, Germany (Faculty Life Sciences, Department of Biomedical Engineering)](https://www.haw-hamburg.de/fakultaeten-und-departments/ls/studium-und-lehre/master-studiengaenge/mbme.html) and [PLUX wireless biosignals, S.A.](http://www.plux.info), Lisbon, Portugal.

## Disclaimer
This package is not part of the official KUBIOS software.

This program is distributed in the hope it will be useful and provided to you "as is", but WITHOUT ANY WARRANTY, without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. This program is NOT intended for medical diagnosis. We expressly disclaim any liability whatsoever for any direct, indirect, consequential, incidental or special damages, including, without limitation, lost revenues, lost profits, losses resulting from business interruption or loss of data, regardless of the form of action or legal theory under which the liability may be asserted, even if advised of the possibility of such damages.
