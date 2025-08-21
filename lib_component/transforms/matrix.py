import numpy as np, math

def translation(tx, ty):
    return np.array([[1, 0, tx],
                     [0, 1, ty],
                     [0, 0, 1]])

def scaling(s):
    return np.array([[s, 0, 0],
                     [0, s, 0],
                     [0, 0, 1]])

def rotation(angle_deg):
    rad = math.radians(angle_deg)
    c, s = math.cos(rad), math.sin(rad)
    return np.array([[c, -s, 0],
                     [s,  c, 0],
                     [0,  0, 1]])
