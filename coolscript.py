import os
import arcpy
from arcpy import env

env.workspace = r"C:\Users\pratik.pathak\lpthw\homework\2020-03-02"
# print (os.getcwd())
input1_in = "input1.shp"
input2_in = "input2.shp"
clipped_out = "clipped.shp"
unioned_out = "unioned.shp"
xy_tolerance =""

arcpy.Clip_analysis (input1_in, input2_in, clipped_out, xy_tolerance)
arcpy.Union_analysis ([input1_in, input2_in], unioned_out,"ONLY_FID")
