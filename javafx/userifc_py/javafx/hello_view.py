# -*- coding: utf-8 -*-
'''JavaFX interface (hand-coded) Hello-View module (for Model-View-Controller)

'''

from __future__ import (absolute_import, division, print_function,
  unicode_literals)

import sys, os, logging, inspect
#from future.builtins import (ascii, filter, hex, map, oct, zip, str)

from intro_py import util
from userifc_py.aux import observer

if 'java' not in sys.platform.lower():
    raise Exception('This package can only be used with Jython.')

from javafx.embed.swing import JFXPanel
_ = JFXPanel() # ? prevent JavaFX Toolkit not initialized exception
from javafx.geometry import Pos
from javafx.scene.layout import StackPane, Pane, VBox
from javafx.scene.control import (Label, Button, TextField, DialogPane,
  TextArea)

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
    self.parent = StackPane(id='stackpane1', alignment=Pos.CENTER)
    self.widgets.update({'parent': self.parent, 'pane1': Pane(id='pane1'),
      'vbox1': VBox(id='vbox1', alignment=Pos.CENTER),
      'label1': Label('label1', id='label1', alignment=Pos.CENTER),
      'button1': Button('button1', id='button1', alignment=Pos.CENTER),
      'textview1': TextArea(id='textview1'),
      'entry1': TextField(id='entry1', promptText='Enter name')})
    self.widgets['dialog1'] = DialogPane(id='dialog1', headerText='dialog1',
      content=self.widgets['entry1'])
    #self.widgets['vbox1'].children.add(self.widgets['label1'])
    self.widgets['vbox1'].children.addAll(self.widgets['label1'], 
      self.widgets['button1'], self.widgets['textview1'])
    self.widgets['pane1'].children.add(self.widgets['vbox1'])
    self.widgets['parent'].children.addAll(self.widgets['pane1'], 
      self.widgets['dialog1'])
    self.widgets['dialog1'].visible = False
    self.widgets['parent'].setPrefSize(202.0, 208.0)
    self.widgets['pane1'].setPrefSize(198.0, 205.0)
    self.widgets['vbox1'].setPrefSize(195.0, 205.0)
    self.widgets['label1'].setPrefSize(174.0, 38.0)
    self.widgets['button1'].setPrefSize(174.0, 48.0)
    self.widgets['textview1'].setPrefSize(174.0, 107.0)

  def update(self, data):
    self._data = data
    self.widgets['textview1'].text = self.data
