# -*- coding: utf-8 -*-
'''Curses interface Hello-View module (for Model-View-Controller)

'''

from __future__ import (absolute_import, division, print_function,
  unicode_literals)

import sys, os, logging, inspect, enum, atexit
#from future.builtins import (ascii, filter, hex, map, oct, zip, str)

from intro_py import util
from userifc_py.aux import observer

import curses, curses.panel

__all__ = ['curses', 'HelloView', 'Keys']


Keys = {    # usage: Keys['KEY_ENTER']
  'KEY_ENTER': ord('E') - 64,  # Ctrl+E -- Enter (Curses.KEY_ENTER)
  'KEY_ESC': ord('X') - 64,    # Ctrl+X -- Exit  (Curses.KEY_EXIT)
  'KEY_RUN': ord('R') - 64     # Ctrl+R -- Run   (???)
  }

#MODULE_LOGGER = logging.getLogger(__name__)

class HelloView(observer.Observer):
  '''Description:: '''

  def __init__(self, screen=curses.initscr()):
    '''Construct object'''

    observer.Observer.__init__(self)
    #super(HelloView, self).__init__()
    atexit.register(self.cleanup)

    #self.logger = logging.getLogger(__name__ + '.' + self.__class__.__name__)
    self.stdscr, self.panels = screen, {}
    self.setup()
    #self.stdscr.clear()
    orig_hgt, orig_wid = self.stdscr.getmaxyx()
    
    self.panels['output'] = curses.panel.new_panel(
      curses.newwin(orig_hgt - 5, orig_wid - 2, 1, 1))
    self.panels['input'] = curses.panel.new_panel(
      curses.newwin(3, orig_wid // 2, 7, 20))
    self.panels['commands'] = curses.panel.new_panel(
      curses.newwin(4, orig_wid - 2, orig_hgt - 5, 1))

    #self.stdscr.addstr(0, (orig_wid - len(__name__) - 2) // 2, __name__,
    #  curses.A_REVERSE)
    self.stdscr.addstr(__name__.ljust(orig_wid - 32), curses.A_REVERSE)
    
    for _, pan in self.panels.items():
      pan.window().clear()
      pan.window().border()
    self.panels['commands'].window().addch(1, 1, Keys['KEY_RUN'],
      curses.A_STANDOUT)
    self.panels['commands'].window().addstr(' Run'.ljust(11))
    self.panels['commands'].window().addch(Keys['KEY_ENTER'],
      curses.A_STANDOUT)
    self.panels['commands'].window().addstr(' Enter Name'.ljust(11))
    self.panels['commands'].window().addch(2, 1, Keys['KEY_ESC'], 
      curses.A_STANDOUT)
    self.panels['commands'].window().addstr(' Exit'.ljust(11))
    #self.stdscr.refresh()

  def setup(self):
    #self.stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    self.stdscr.keypad(True)
    #return stdscr

  def cleanup(self):
    curses.nocbreak()
    self.stdscr.keypad(False)
    curses.echo()
    curses.endwin()    

  def update(self, data):
    self._data = data
    cur_y, _ = self.panels['output'].window().getyx()
    self.panels['output'].window().addstr(cur_y+1, 1, self.data)
