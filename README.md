# PrusaSlicer-numberformater
Reformat all numbers in PrusaSlicers' GCode. 

Reformat from .2 to 0.2. This script will add zeros before the decimal point. 

See PrusaSlicer issue: https://github.com/prusa3d/PrusaSlicer/issues/6996

### Note
It will reformat _all_ numbers found in the gcode file.

![image](https://user-images.githubusercontent.com/10420187/148681885-d3729649-419c-42be-98b1-9b5a87cd4cb0.png)

_Left_ before and _right_ after the script has run.

## Installation
Add that script to the post processing section of PrusaSlicer.
Maybe so: 
"C:\Users\USERNAME\AppData\Local\Programs\Python\Python39\python.exe" "C:\dev\prusaslicer-numberformater.py";
