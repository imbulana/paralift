import numpy as np
import pyvista as pv

# receive bb (singular)

# hough filter (only ellipses for now)

# transform to center

# find minimal peak path to center (origin) OR alternatively slice across the center

# slice across center and extrude

def slice_across_axis(shell, axis=[0, 1, 0]):
    spline = shell.slice(normal=axis)
    # recreate surface from spline
    # extruded = spline.extrude_rotate(resolution=100)
    return spline

# reflect path around origin

# fit sinusoidal to path (solve sys of eqns.) for symmetric surfaces
# or Taylor approx./interpolation for complex surfaces
def to_parametric():
    pass

def lift():
    pass