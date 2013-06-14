# -*- coding: utf-8 -*-
'''JavaFX interface Hello-Controller module (for Model-View-Controller)

'''

from __future__ import (absolute_import, division, print_function,
  unicode_literals)

import sys, os, logging, inspect
#from future.builtins import (ascii, filter, hex, map, oct, zip, str)

if 'java' not in sys.platform.lower():
    raise Exception('This package can only be used with Jython.')

from java.lang import System

#from javafx.embed.swing import JFXPanel
#_ = JFXPanel() # ? prevent JavaFX Toolkit not initialized exception
from javafx.scene import Scene
from javafx.application import Application
from javafx.stage import WindowEvent
#from javafx.event import EventHandler

from userifc_py.javafx.hello_model import HelloModel
from userifc_py.javafx.hello_formview import HelloView

__all__ = ['HelloController', 'userifc_version']


#MODULE_LOGGER = logging.getLogger(__name__)

def userifc_version():
  import platform

  return "(Jython {0}) Java {1} JavaFX {2}".format(platform.python_version(),
    System.getProperty("java.version"), System.getProperty("javafx.version"))

class HelloController(object):
  '''Description:: '''

  def __init__(self, stageX, greetpath, pkg_or_mod=__name__, rsrc_path=None):
    '''Construct object'''

    #super(HelloController, self).__init__(stage, greetpath, pkg_or_mod, rsrc_path)
    
    self.stage = stageX
    self.logger = logging.getLogger(__name__ + '.' + self.__class__.__name__)
    self._model = HelloModel(greetpath, pkg_or_mod, rsrc_path)
    self._view1 = HelloView(pkg_or_mod, rsrc_path) # HelloView()
    #self._view2 = HelloView(pkg_or_mod, rsrc_path) # HelloView()
    
    #self.view1.widgets['button1'].setOnAction(self.Button1EventHandler())
    #self.view1.widgets['entry1'].setOnAction(self.Entry1EventHandler())
    self.view1.widgets['button1'].setOnAction(self.onButton1Action)
    self.view1.widgets['entry1'].setOnAction(self.onEntry1Action)
    
    #self.stage.setOnCloseRequest(self.StageCloseHandler())
    self.stage.setOnCloseRequest(self.onStageClose)

    self.model.attachObserver(self.view1) # view[1 .. N]
    self.stage.setTitle(self.view1.parent.id)
    self.view1.parent.visible = True

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

#  class StageCloseHandler(EventHandler):
#    '''Window listener for stage'''
#    
#    def handle(self, event):
#      if WindowEvent.WINDOW_CLOSE_REQUEST == event.eventType:
#        #event.target.close()
#        HelloController.stage.close()
    
#  class Button1EventHandler(EventHandler):
#    '''Action listener for button1'''
#    
#    def handle(self, event):
#      HelloController.view1.widgets['pane1'].visible = False
#      HelloController.view1.widgets['dialog1'].visible = True
#      HelloController.view1.widgets['entry1'].text = ""

#  class Entry1EventHandler(EventHandler):
#    '''Action listener for entry1'''
#    
#    def handle(self, event):
#      HelloController.view1.widgets['dialog1'].visible = False
#      HelloController.view1.widgets['pane1'].visible = True
#      HelloController.model.notifyObservers(
#        HelloController.view1.widgets['entry1'].text)
  
  def onStageClose(self, event):
    '''Window listener for stage'''
    
    if WindowEvent.WINDOW_CLOSE_REQUEST == event.eventType:
      #event.target.close()
      self.stage.close()
  
  def onButton1Action(self, event):
    '''Action listener for button1'''
    
    self.view1.widgets['pane1'].visible = False
    self.view1.widgets['dialog1'].visible = True
    self.view1.widgets['entry1'].text = ""

  def onEntry1Action(self, event):
    '''Action listener for entry1'''
    
    self.view1.widgets['dialog1'].visible = False
    self.view1.widgets['pane1'].visible = True
    self.model.notifyObservers(self.view1.widgets['entry1'].text)

class JfxApp(Application):
  def start(self, stagePrime):
    params = self.getParameters()
    param0 = params.getRaw()[0] if 0 < len(params.getRaw()) else ''
    
    gui = HelloController(stagePrime, 'greet.txt', 'userifc_py.javafx')
    gui.view1.widgets['textview1'].text = params.getNamed()['pretext']
    stagePrime.setScene(Scene(gui.view1.parent, 200, 160))
    stagePrime.show()

def lib_main(argv=None):
  pretext = '{0} GUI\n'.format(userifc_version())
  
  #JfxApp.launch(JfxApp, ['--pretext=' + pretext])
  Application.launch(JfxApp, ['--pretext=' + pretext])
  
  return 0
  
if '__main__' == __name__:
  sys.exit(lib_main(sys.argv[1:]))
