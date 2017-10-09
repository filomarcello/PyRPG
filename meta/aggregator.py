""" 
created: 09/10/2017
author: marcello
version: 1.0
"""
from collections import Iterable


class Aggregator:
    """Contains properties, i.e. key-value couples."""

    def __init__(self, props: Iterable = {}):
        """If props IS_A dict, its keys-values are the propertirs.
        Properties names are taken from tuple or list, with values = None."""

        if isinstance(props, dict):
            self.props = props
        elif isinstance(props, list) or isinstance(props, tuple):
            self.props = dict(zip(props, (None,) * len(props)))

    def __getitem__(self, prop: str):
        return self.props.get(prop)

    def __setitem__(self, prop: str, value):
        self.props[prop] = value

    @property
    def properties(self):
        return self.props




