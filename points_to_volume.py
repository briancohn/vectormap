# This file was *autogenerated* from the file /Users/Olive/Documents/dev/bbdl/cat_model/sohn_data/points_to_volume.sage.
from sage.all_cmdline import *   # import sage library
_sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_10 = Integer(10)
import csv
import sys

# filepath = sys.argv[1]

# a = csv.reader(open(filepath))

poly_3d_space = Polyhedron(vertices = [ [_sage_const_1 ,_sage_const_0 ,_sage_const_0 ],
									[_sage_const_0 ,_sage_const_1 ,_sage_const_0 ], 
									[_sage_const_0 ,_sage_const_1 ,_sage_const_0 ]])
vol = poly_3d_space.volume()
print(vol)
sys.sleep(_sage_const_10 )
