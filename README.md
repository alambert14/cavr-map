ASCII-MAP - Generate Shapes in a Grid of Numbers
================================================
This script allows the user to add shapes to a topographic map that is output as an ascii grid. Shape locations are defined in an input file and a grid of numbers is output in another file.

TODO: DECIDE WHAT UNITS THE X AND Y ARE IN!!!!!!!!!!!! Also if we are ned or enu

Usage
=====
`shape_array.py` is (currently) the entry point for the script. Calling it will load the file `input.txt` and output the ascii grid to `output.asc`. The flags `--input` and `--output` allow you to define the names of the input and output files respectively.


Input
=====
The script assumes an input file is supplied. The input file contains information about the shapes that the user wants to add to the map. Each line of the file defines a different shape. There are a finite number of primitive shapes. As of now, only the rectangle, ellipse, and circle will be implemented. The selection will hopefully be expanded to include at least rectangular prisms and sphere, and spherical objects.

Disclaimer
----------
The coordinate system of the ascii map relative to the world map is currently
undefined. As of now, the best solution is to find the `lat0` and `lon0`
defined in `vlbv sim_lowlevel.launch` and use these as `yllcenter` and
`xllcenter` (note that this may be reverse of what is logical). There is no
guarantee of the ascii image's rotation relative to any world system. Right
now, it just gives enough precision to have *something* show up in rviz.

Input Explanation
-----------------
Rotation is input as degrees.

The the "rect" command will graph a rectangle. In order to easily allow for specifying a rectangle that has some arbitrary rotation about the z axis, the shape is specified with the x and y coordinates of its center, the length and width of the rectangle, and the number of degrees through which the shape is rotated in the clockwise direction. The depth of the object also needs to be specified. To be clear, length and width (lx and ly) apply in the x and y direction, before rotation is applied. Then, the resulting object is rotated by the specified amount.

The rectangle object descriptor has the form:

rect(x, y, lx, ly, rot, depth)

The rectangular prism will be specified similarly:
rect3d(x, y, z, lx, ly, lz, rot, depth)

Note that as of now the rectangular prism can only be rotated about the z axis.

An ellipse is specified by the coordinates of its center point, and the length of its two axes. It can also be rotated. An ellipse is specified as:
ellipse(x, y, lx, ly, rot, depth) where dx is the length of the axis in the x direction and dy is the length of the axis in the y direction. 

Finally, a spheroid is specified as:
ellipse3d(x, y, z, lx, ly, lz, rot, depth)

At this point, as with the 3d rectangle, only rotation around the z axis is supported. It's not clear exactly how the ellipse3d and to some extent the rect3d will be useful, but they will be included for robustness.


"square" and "circle" and their 3d counterparts "square3D" and "circle3D" will be provided for convenience. These require 1 fewer argument and are just wrappers for the above objects. square is called as square(x, y, l, rot, depth), where l is the side length. The same logic applies for the other three special objects.


The input file has a header used to give useful information about what the shapes represent. It also must specify the size of the grid to be used. The shape definitions are placed after the `<BEGIN SHAPES>` tag and before the `<END SHAPES>` tag. Comments can be added to the body with the "#" sign. An example input file follows:

```

This is the header. The header describes why these shapes are here.
Or other useful information
Like Dates
Or Notes

ncol	20
nrows	20
xllcenter	-121.8787
yllcenter	36.6043
cellsize	0.00001
nodata_value	-9999

<BEGIN SHAPES>

rect(10, 10, 5, 10, 0) # This is a rectangle centered at 10, 10 with x direction 5 units, y direction 10 units.

ellipse(20, 20, 5, 15, 45) # Ellipse with rotation 



<END SHAPES>

```



Output
======

The script will read in the text file containing the shapes described and output an ascii map of the location. The output file WILL HAVE A HEADER THAT MATCHES THE MAP_PRIOR HEADER. i.e. it is readable with read_prior


Sample Output
-------------
```
ncol	18
nrows	10 
xllcenter	-121.8787 
yllcenter	36.6043
cellsize	0.00001
nodata_value	-9999
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 5 5 5 5 0 0 0 0 0 0 0 0 0 0 0 0
0 5 5 5 5 0 0 0 0 1 1 1 1 1 0 0 0
0 5 5 5 5 0 0 0 0 1 1 1 1 1 0 0 0
0 5 5 5 5 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0


```



Workflow notes:

1. Input file opened
2. Parse header for data necessary to initialize array
3. Parse the rest of the file for shape objects. Store these as a list of objects. (i.e. our text definitions get instantiated as geometry objects from another library, and we keep a list of these objects)
4. We we feed the objects through a transform function. This is only because we have not nailed down the input and output reference frames, and there *might* be a difference. Therefore, we feed the objects through a "transform_object" function that can just be the identity function right now.
5. Load the objects into the array. This is tricky and subtle
6. Write the array - This is pretty easy

