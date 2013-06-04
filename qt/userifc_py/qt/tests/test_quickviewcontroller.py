# -*- coding: utf-8 -*-
'''Test cases for Model, View, and Controller.'''
from __future__ import (absolute_import, division, print_function,
    unicode_literals)

import os, unittest
#from future.builtins import (ascii, filter, hex, map, oct, zip, range)

from userifc_py.qt.hello_quickcontroller import (QtCore, HelloController,
  QApplication)

if '4' != os.environ.get('QT_MAJOR_VERSION', 'LATEST'):
  from PyQt5.QtTest import QTest
else:
  from PyQt4.QtTest import QTest

def setUpModule():
  '''Set up (module-level) test fixtures, if any.'''
  print('Setup module: {0}'.format(__name__))

def tearDownModule():
  '''Tear down (module-level) test fixtures, if any.'''
  print('Teardown module: {0}'.format(__name__))

def refresh_ui(delay=0):
  '''Refresh UI by cycling through all pending events'''
  import time

  while QApplication.hasPendingEvents():
    QApplication.processEvents()    # or (block=False)
  time.sleep(delay)


class TestQuicjViewController(unittest.TestCase):
  app = QApplication([])
  userifc = HelloController('greet.txt', 'userifc_py.qt')
  view1 = userifc.view1
  #hdlr = userifc # ??? userifc.hdlr OR userifc
  hdlr = view1.engine.rootContext().contextProperty('handler')
  delay_secs = 3.0

  @classmethod
  def setUpClass(cls):
    #print('Setup class: {0}'.format(cls.__name__))
    pass

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
    self.assertTrue(QtCore)

  def test_use_ok(self):
    '''Can use HelloController class'''
    self.assertTrue(self.userifc)

  def test_on_button1_clicked(self):
    '''Ensure correct actions on button1 clicked.

    Entry1 text is set to ""
    Dialog1 is shown
    Textview1 is shown
    '''
    [entry1, simpleentry1, simplebutton1] = map(self.view1.widgets.get,
      ['entry1', 'simpleentry1', 'simplebutton1'])
    entry1.setProperty('text', 'xxxxxx')
    self.hdlr.on_button1_clicked()
    refresh_ui(self.delay_secs)
    
    self.assertEqual(simplebutton1.property('opacity'), 0)
    self.assertEqual(entry1.property('text'), '')
    self.assertEqual(simpleentry1.property('opacity'), 1)
    self.assertEqual(entry1.property('focus'), 1)

  def test_on_entry1_returnPressed(self):
    '''Ensure correct actions on entry1 returnPressed'''

    [entry1, simpleentry1, textview1, simplebutton1] = map(
      self.view1.widgets.get, ['entry1', 'simpleentry1', 'textview1',
      'simplebutton1'])
    entry1.setProperty('text', 'John Doe')
    self.hdlr.on_entry1_returnPressed()
    refresh_ui(self.delay_secs)
    
    self.assertEqual(simpleentry1.property('opacity'), 0)
    self.assertEqual(simplebutton1.property('opacity'), 1)
    #self.assertEqual(textview1.property('text'),
    #  list(self.userifc.model._observers)[0].data)
    self.assertEqual(textview1.property('text'), self.userifc.view1._data)
