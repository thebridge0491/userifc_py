# -*- coding: utf-8 -*-
'''Person module.

'''

from __future__ import (absolute_import, division, print_function,
    unicode_literals)

import logging, inspect
#from future.builtins import (ascii, filter, hex, map, oct, zip, object)

__all__ = ['Person']


# MODULE_LOGGER = logging.getLogger(__name__)

class Person(object):

    def __init__(self, name = 'World', age = 0):
        self.logger = logging.getLogger(
            __name__ + '.' + self.__class__.__name__)
        self._name, self._age = name, age

    def __eq__(self, other):
        return (isinstance(other, self.__class__) and
            self.__dict__ == other.__dict__)

    def __ne__(self, other):
        return not self.__eq__(other)

    __hash__ = None
#    def __hash__(self):
#        return hash(self.name) ^ hash(self.age)

    def __str__(self):
        return '{0}\{\{name: {1}, age: {2}\}\}'.format(
            self.__class__.__name__, self.name, self.age)

    def __repr__(self):
        return "{0}(name='{1}', age={2})".format(
            __name__ + '.' + self.__class__.__name__, self.name, self.age)

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        func_name = inspect.stack()[0][3]
        self.logger.debug(func_name + '()')

        return self._age

    @name.setter
    def name(self, newname):
        self._name = newname

    @age.setter
    def age(self, newage):
        func_name = inspect.stack()[0][3]
        self.logger.debug(func_name + '()')

        self._age = newage
