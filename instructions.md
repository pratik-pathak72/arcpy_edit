# LPTHW Homework for 2020-03-02
A simple `arcpy`-based utility to run the Clip, Union, and Erase tools.

## Requirements
The script should accept four input arguments:
    1. The name of the geoprocessing tool to run (`clip`, `union`, or `erase`)
    2. Paths to two input shapefiles
    3. Path to an output shapefile

It should work something like this:
```
> C:\Python27\ArcGIS10.4\python.exe coolscript.py clip input1.shp input2.shp clipped.shp
Clipping "input1.shp" with "input2.shp" to create "clipped.shp"...
Done.

> C:\Python27\ArcGIS10.4\python.exe coolscript.py union input1.shp input2.shp unioned.shp
Unioning "input1.shp" with "input2.shp" to create "unioned.shp"...
Done.
```
Where:
    * `C:\Python27\ArcGIS10.4\python.exe` is the path to the ArcGIS Desktop Python
    * `coolscript.py` is your incredible script
    * `clip` is just a string that your script will check to decide whether to run Clip, Union, or Erase
    * `input.shp` is the path to the first input file
    * `clip_area.shp` is the path to the second input file
    * `output.shp` is where the output will be stored

## Notes
* Read the manual! Check the documentation online to figure out exactly what you need to do to run the Clip, Union, and Erase tools in Python.
* Use functions!
* Sometimes `arcpy` lets you use relative paths like `mydata\input1.shp`, instead of absolute paths like `C:\blah\mydata\input1.shp`. Sometimes it doesn't. This is weird. You might need to use the `os.path.abspath` function to get the full path to a file. Look it up!
