import matplotlib.pyplot as plt
from astropy import units as u
from mw_plot import MWSkyMap
from astropy.coordinates import SkyCoord
import numpy as np



def find_coordinates(name):
    ra_dec = SkyCoord.from_name(name)
    galactic = ra_dec.galactic
    
    return galactic.l.deg, galactic.b.deg


#Task 0-2
def skymap(l,b, radius):
    mw1 = MWSkyMap(
    center=(l*u.deg,b*u.deg),
    radius=(radius, radius) * u.arcsec,
    background="Mellinger color optical survey"
)

    fig, ax = plt.subplots(figsize=(5, 5))

    mw1.transform(ax)

    mw1.savefig('galaxy.png')
    
    
    
#task 3
def plt2rgbarr(fig):
    """
    A function to transform a matplotlib to a 3d rgb np.array 

    Input
    -----
    fig: matplotlib.figure.Figure
        The plot that we want to encode.        

    Output
    ------
    np.array(ndim, ndim, 3): A 3d map of each pixel in a rgb encoding (the three dimensions are x, y, and rgb)
    
    """
    fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
    fig.canvas.draw()
    rgba_buf = fig.canvas.buffer_rgba()
    w, h = fig.canvas.get_width_height()
    rgba_arr = np.frombuffer(rgba_buf, dtype=np.uint8).reshape((h, w, 4))
    return rgba_arr[:, :, :3]