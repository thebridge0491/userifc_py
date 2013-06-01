# -*- coding: utf-8 -*-
'''Subject module (for Observer pattern)

'''

from __future__ import (absolute_import, division, print_function,
  unicode_literals)

import sys, os, logging, inspect
#from future.builtins import (ascii, filter, hex, map, oct, zip, str)

__all__ = ['Subject']


#MODULE_LOGGER = logging.getLogger(__name__)

class Subject(object):
  '''Description:: '''

  def __init__(self):
    '''Construct object'''

    self.logger = logging.getLogger(__name__ + '.' + self.__class__.__name__)
    self._observers = set()

  def __eq__(self, other):
    return (isinstance(other, self.__class__) and
      self.__dict__ == other.__dict__)

  def __ne__(self, other):
    return not self.__eq__(other)

#  __hash__ = None
  def __hash__(self):
    return hash(self.__class__.__name__)

  def __str__(self):
    return '{0}'.format(self.__class__.__name__)

  def __repr__(self):
    return "{0}".format(__name__ + '.' + self.__class__.__name__)

  def attachObserver(self, obs):
    self._observers.add(obs)

  def detachObserver(self, obs):
    self._observers.discard(obs)

  def notifyObservers(self, arg):
    for obs in self._observers:
      obs.update(arg if arg is not None else '')


def lib_main(argv=None):
  from userifc_py.aux import subject, observer

  subj = subject.Subject()
  obs = observer.Observer()

  subj.attachObserver(obs)
  subj.notifyObservers('To be set -- HELP.')
  print('obs.data:', obs.data)
  return 0

if '__main__' == __name__:
  sys.exit(lib_main(sys.argv[1:]))
