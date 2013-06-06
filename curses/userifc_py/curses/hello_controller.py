# -*- coding: utf-8 -*-
'''Curses interface Hello-Controller module (for Model-View-Controller)

'''

from __future__ import (absolute_import, division, print_function,
  unicode_literals)

import sys, os, logging, inspect
#from future.builtins import (ascii, filter, hex, map, oct, zip, str)

from userifc_py.curses.hello_model import HelloModel
from userifc_py.curses.hello_view import curses, HelloView, Keys

__all__ = ['curses', 'HelloController', 'userifc_version', 'run']


#MODULE_LOGGER = logging.getLogger(__name__)

def userifc_version():
  import platform

  #return '(Python {0}) Curses {1}'.format(platform.python_version(),
  #  curses.version.decode('utf-8'))
  return '(Python {0}) Ncurses {1}.{2}.{3}'.format(platform.python_version(),
    curses.ncurses_version.major, curses.ncurses_version.minor,
    curses.ncurses_version.patch)

class HelloController(object):
  '''Description:: '''

  def __init__(self, greetpath, pkg_or_mod=__name__, rsrc_path=None):
    '''Construct object'''

    #super(HelloController, self).__init__(greetpath, pkg_or_mod, rsrc_path)

    self.logger = logging.getLogger(__name__ + '.' + self.__class__.__name__)
    self._model = HelloModel(greetpath, pkg_or_mod, rsrc_path)
    self._view1 = HelloView()
    #self._view2 = HelloView()

    self.model.attachObserver(self.view1) # view[1 .. N]
    #self.view1.stdscr.refresh()

  @property
  def model(self):
    return self._model

  #@model.setter
  #def model(self, newmodel):
  #  self._model = newmodel

  @property
  def view1(self):
    return self._view1

  #@view1.setter
  #def view1(self, newview):
  #  self._view1 = newview
  
  def step_virtualscr(self):
    isRunning = True
    self.view1.panels['input'].window().clear()
    self.view1.panels['input'].window().border()
    self.view1.panels['input'].hide()
    ch = self.view1.panels['commands'].window().getch()
    
    if Keys['KEY_ENTER'] == ch:
      self.on_key_enter()
    elif Keys['KEY_ESC'] == ch:
      isRunning = False
    elif Keys['KEY_RUN'] != ch:
      self.on_key_unmapped(ch)
    
    for _, pan in self.view1.panels.items():
      pan.window().noutrefresh()
    return isRunning
  
  def run(self):
    curses.noecho()
    self.view1.stdscr.refresh()
    
    while self.step_virtualscr():
      #curses.panel.update_panels()
      curses.doupdate()

  def on_key_unmapped(self, ch):
    '''Callback for unmapped key'''
    
    self.view1.panels['input'].window().addstr(1, 1, 
      'Error! Un-mapped key: {0}. Retrying.'.format(
      curses.unctrl(ch).decode('utf-8')))
    self.view1.panels['input'].window().refresh()
    curses.flash()
    curses.napms(2000)
  
  def on_key_enter(self):
    '''Callback for Keys.KEY_ENTER'''
    
    self.view1.panels['input'].top()
    curses.echo()
    data = self.view1.panels['input'].window().getstr(1, 1).decode('utf-8')
    cur_y, _ = self.view1.panels['output'].window().getyx()
    max_y, _ = self.view1.panels['output'].window().getmaxyx()
    if (max_y - 3) < cur_y:
      self.view1.panels['output'].window().clear()
      self.view1.panels['output'].window().border()
    cur_y, _ = self.view1.panels['output'].window().getyx()
    self.model.notifyObservers(data)
    curses.noecho()
