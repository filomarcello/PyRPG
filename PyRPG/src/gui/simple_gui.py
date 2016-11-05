""" created 04/11/2016
author: marcello
version: 0.1
"""

import tkinter as tk

from environment.map import Map


class Gui(tk.Frame):
    """Base class for GUI."""

    def __init__(self, map: Map, master=None):

        tk.Frame.__init__(self, master)
        self._map = map
        self._map_area = tk.Canvas(self, bg='white')

        self._show_map()

        self.grid()

    def _show_map(self):
        pass

class CharGui(Gui):
    """Shows alphanumeric tiles on screen."""

    def __init__(self, map: Map, step: int, master=None):
        self._step = step
        super().__init__(map, master)


    def _show_map(self):
        """Draws a grid of self._step x self._step tiles."""

        c = self._map.view_all()
        for x in range(len(c)):
            for y in range(len(c[x])):
                self._map_area.create_text(x * self._step, y * self._step,
                                           justify=tk.CENTER,
                                           text=c[x][y], anchor=tk.NW)

        self._map_area.pack()


