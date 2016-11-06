""" created 05/11/2016
author: marcello
version: 0.1
"""

import tkinter as tk
from PIL import Image
from environment.map import Map
from environment.tile import Tile
from gui.simple_gui import BMPGui


t1 = Tile(view=Image.open(r'C:\Users\marcello\progetti\PyRPG\PyRPG\res\img\water.jpeg'))
t2 = Tile(view=Image.open(r'C:\Users\marcello\progetti\PyRPG\PyRPG\res\img\grass.jpeg'))
m1 = Map(tiles=[[t1, t2, t1], [t2, t1, t2], [t1, t2, t1]])

bmp_gui = BMPGui(map=m1)

bmp_gui.mainloop()