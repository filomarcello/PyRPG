""" created 09/12/2015
author: marcello
"""

import random as rnd

class Die:
    """Base class for dice rolling."""

    def __init__(self, code: str = None, casts: int = 1, faces: int = 1):
        """Create a die by 'dice codes' or specifying casts and faces.

        blah.
        """

        if code:
            self._casts, self._faces = self._dicedecoder(code)
            self._code = code
        else:
            self._casts = casts
            self._faces = faces
            self._code = str(casts) + 'd' + str(faces)

    def __str__(self):
        return "Die " + self._code


    def cast(self) -> int:

        self._sequence = [rnd.randint(1, self._faces)
                          for j in range(self._casts)]

        return sum(self._sequence)


    def _dicedecoder(self, code: str) -> (int, int):

        if 'd' in code:
            index_of_d = code.find('d')
        elif 'D' in code:
            index_of_d = code.find('D')

        casts = int(code[:index_of_d])
        faces = int(code[index_of_d + 1:])

        return casts, faces





