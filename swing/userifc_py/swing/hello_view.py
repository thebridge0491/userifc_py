# -*- coding: utf-8 -*-
'''Swing interface (hand-coded) Hello-View module (for Model-View-Controller)

'''

from __future__ import (absolute_import, division, print_function,
  unicode_literals)

import sys, os, logging, inspect
#from future.builtins import (ascii, filter, hex, map, oct, zip, str)

from intro_py import util
from userifc_py.aux import observer

if 'java' not in sys.platform.lower():
    raise Exception('This package can only be used with Jython.')

from java.awt import GridLayout
from javax.swing import (JFrame, JPanel, JLabel, JButton, JTextArea, 
  JTextField, JDialog, BoxLayout)

__all__ = ['HelloView']


#MODULE_LOGGER = logging.getLogger(__name__)

class HelloView(observer.Observer):
  '''Description:: '''

  def __init__(self):
    '''Construct object'''

    observer.Observer.__init__(self)
    #super(HelloView, self).__init__()

    #self.logger = logging.getLogger(__name__ + '.' + self.__class__.__name__)
    self.widgets = {}
    self.widgets.update({'frame1': JFrame(),
      'vbox1': JPanel(GridLayout(3, 1)), 'vbox2': JPanel(),
      'label1': JLabel("jLabel1"), 'button1': JButton("jButton1"),
      'textview1': JTextArea(), 'entry1': JTextField(15)})
    self.widgets['dialog1'] = JDialog(self.widgets['frame1'],
      preferredSize = (200, 64), title = 'jDialog1')
    self.widgets['vbox2'].setLayout(BoxLayout(self.widgets['vbox2'], 
      BoxLayout.Y_AXIS))
    for widget in map(self.widgets.get, ['label1', 'button1', 'textview1']):
      self.widgets['vbox1'].add(widget)
    self.widgets['vbox2'].add(self.widgets['entry1'])
    self.widgets['frame1'].getContentPane().add(self.widgets['vbox1'])
    self.widgets['dialog1'].getContentPane().add(self.widgets['vbox2'])
    self.widgets['frame1'].pack()
    self.widgets['dialog1'].pack()
    self.widgets['frame1'].setSize(200, 160)
    self.widgets['dialog1'].setSize(200, 64)
    self.widgets['frame1'].setLocation(200, 300)
    self.widgets['dialog1'].setLocation(200, 300)

  def update(self, data):
    self._data = data
    self.widgets['textview1'].text = self.data
