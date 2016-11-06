""" created 05/11/2016
author: marcello
version: 0.1
"""

from environment.map import Map
from environment.tile import Tile
from gui.simple_gui import CharGui


t1 = Tile(view='1')
t2 = Tile(view='2')
m1 = Map(tiles=[[t1, t2, t1], [t2, t1, t2], [t1, t2, t1]])

txt_gui = CharGui(map=m1, step=30)
txt_gui.mainloop()
