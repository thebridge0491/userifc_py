# -*- coding: utf-8 -*-
'''Test cases for Model, View, and Controller.'''
from __future__ import (absolute_import, division, print_function,
    unicode_literals)

import sys, unittest
#from future.builtins import (ascii, filter, hex, map, oct, zip, range)

if 'java' not in sys.platform.lower():
    raise Exception('This package can only be used with Jython.')

from java.lang import Thread
from javafx.scene import Scene
from javafx.application import Application, Platform
from javafx.stage import WindowEvent
from javafx.event import ActionEvent

from userifc_py.javafx.hello_controller import HelloController

def setUpModule():
  '''Set up (module-level) test fixtures, if any.'''
  print('Setup module: {0}'.format(__name__))

def tearDownModule():
  '''Tear down (module-level) test fixtures, if any.'''
  print('Teardown module: {0}'.format(__name__))

def refresh_ui(delay=0):
  '''Refresh UI by cycling through all pending events'''
  import time

  time.sleep(delay)


class JfxApp(Application):
  def start(self, stagePrime):
    params = self.getParameters()
    param0 = params.getRaw()[0] if 0 < len(params.getRaw()) else ''
    
    gui = HelloController(stagePrime, params.getNamed()['greetpath'],
      params.getNamed()['pkg_or_mod'])
    #gui.view1.widgets['textview1'].text = params.getNamed()['pkg_or_mod']
    TestViewController.stage = stagePrime
    TestViewController.userifc = gui
    TestViewController.view1 = gui.view1
    stagePrime.setScene(Scene(gui.view1.parent, 200, 160))
    stagePrime.show()

class JfxThread(Thread):
  def run(self):
    print('Running JfxThread...')
    #JfxApp.launch(JfxApp, ['--greetpath=greet.txt',
    #  '--pkg_or_mod=userifc_py.javafx'])
    Application.launch(JfxApp, ['--greetpath=greet.txt',
      '--pkg_or_mod=userifc_py.javafx'])

class TestViewController(unittest.TestCase):
  stage, userifc, view1 = None, None, None
  delay_secs = 3.0

  @classmethod
  def setUpClass(cls):
    #print('Setup class: {0}'.format(cls.__name__))
    #pass
    threadJfx = JfxThread()
    threadJfx.setDaemon(True)
    threadJfx.start()
    #threadJfx.sleep(int(cls.delay_secs) * 1000)
    refresh_ui(cls.delay_secs)

  @classmethod
  def tearDownClass(cls):
    #print('\nTeardown class: {0}'.format(cls.__name__))
    pass

  def setUp(self):
    #print('Setup method: {0}'.format(self._testMethodName))
    pass

  def tearDown(self):
    #print('Teardown method: {0}'.format(self.id().split('.')[-1]))
    pass

  def test_main(self):
    self.assertTrue(HelloController)  # use your library here

  def test_use_ok(self):
    '''Can use HelloController class'''
    self.assertTrue(self.userifc)

  def test_on_button1_action(self):
    '''Ensure correct actions from button1 ActionListener.
    
    Entry1 text is set to ""
    Dialog1 is shown
    Frame1 is not shown
    '''
    
    [entry1, dialog1, pane1, button1] = map(self.view1.widgets.get, 
      ['entry1', 'dialog1', 'pane1', 'button1'])
    entry1.text = 'xxxxxx'
    
    button1.fire()
    refresh_ui(self.delay_secs)
    self.assertTrue(dialog1.visible and not pane1.visible)
    self.assertEqual(entry1.text, '')

  def test_on_stage_windowClosing(self):
    '''Ensure correct actions from stage WindowListener'''
    
    self.assertTrue(self.stage.showing)
    
    #Platform.runLater(self.stage.close)
    Platform.runLater(lambda : self.stage.fireEvent(WindowEvent(self.stage,
      WindowEvent.WINDOW_CLOSE_REQUEST)))
    refresh_ui(self.delay_secs)
    self.assertTrue(not self.stage.showing)

  def test_on_entry1_action(self):
    '''Ensure correct actions from entry1 ActionListener'''
    
    [entry1, dialog1, textview1] = [self.view1.widgets.get(x) for x in 
      ['entry1', 'dialog1', 'textview1']]
    dialog1.visible = True
    entry1.text = 'John Doe'
    
    entry1.fireEvent(ActionEvent())
    refresh_ui(self.delay_secs)
    #self.assertEqual(textview1.text,
    #  list(self.userifc.model._observers)[0].data)
    self.assertEqual(textview1.text, self.userifc.view1._data)
    self.assertTrue(not dialog1.visible)
