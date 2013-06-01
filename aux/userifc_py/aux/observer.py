# -*- coding: utf-8 -*-
'''Observer module (for Observer pattern)

'''

from __future__ import (absolute_import, division, print_function,
  unicode_literals)

import sys, os, logging
#from future.builtins import (ascii, filter, hex, map, oct, zip, str)

__all__ = ['Observer']


#MODULE_LOGGER = logging.getLogger(__name__)

class Observer(object):
  '''Description:: '''

  def __init__(self):
    '''Construct object'''

    #self.logger = logging.getLogger(__name__ + '.' + self.__class__.__name__)
    self._data = None

  def __eq__(self, other):
    return (isinstance(other, self.__class__) and
      self.__dict__ == other.__dict__)

  def __ne__(self, other):
    return not self.__eq__(other)

# __hash__ = None
  def __hash__(self):
    return hash(self.data) ^ hash(self.data)

  def __str__(self):
    return '{0}{{data: {1}}}'.format(self.__class__.__name__, self.data)

  def __repr__(self):
    return "{0}(data={1})".format(__name__ + '.' + self.__class__.__name__,
      self.data)

  @property
  def data(self):
    return self._data

  def update(self, data):
    self._data = data


#def lib_main(argv=None):
#  from userifc_py.aux import subject, observer
#
#  subj = subject.Subject()
#  obs = observer.Observer()
#
#  subj.attachObserver(obs)
#  subj.notifyObservers('To be set -- HELP.')
#  print('obs.data:', obs.data)
#  return 0
#
#if '__main__' == __name__:
#  sys.exit(lib_main(sys.argv[1:]))
