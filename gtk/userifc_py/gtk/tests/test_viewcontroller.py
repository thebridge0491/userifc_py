# -*- coding: utf-8 -*-
'''Test cases for Model, View, and Controller.'''
from __future__ import (absolute_import, division, print_function,
    unicode_literals)

import unittest
#from future.builtins import (ascii, filter, hex, map, oct, zip, range)

from userifc_py.gtk.hello_controller import Gtk, HelloController

def setUpModule():
  '''Set up (module-level) test fixtures, if any.'''
  print('Setup module: {0}'.format(__name__))

def tearDownModule():
  '''Tear down (module-level) test fixtures, if any.'''
  print('Teardown module: {0}'.format(__name__))

def refresh_ui(delay=0):
  '''Refresh UI by cycling through all pending events'''
  import time

  while Gtk.events_pending():
    Gtk.main_iteration_do(False)    # or (block=False)
  time.sleep(delay)


class TestViewController(unittest.TestCase):
  userifc = HelloController('greet.txt', 'userifc_py.gtk')
  view1 = userifc.view1
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
    self.assertTrue(Gtk)

  def test_use_ok(self):
    '''Can use HelloController class'''
    self.assertTrue(self.userifc)

  def test_class_is_gtk_builder_or_window(self):
    '''Ensure class is Gtk.Builder or Gtk.Window'''
    self.assertTrue(isinstance(self.view1, Gtk.Builder) or
      isinstance(self.view1, Gtk.Window))

  def test_button1_clicked_cb(self):
    '''Ensure correct actions on button1 clicked.

    Entry1 text is set to ""
    Dialog1 is shown
    Textview1 is shown
    '''
    [entry1, dialog1, textview1, button1] = map(self.view1.widgets.get,
      ['entry1', 'dialog1', 'textview1', 'button1'])
    entry1.set_text('xxxxxx')

    button1.clicked()
    refresh_ui(self.delay_secs)
    self.assertTrue(dialog1.get_visible() and textview1.get_visible())
    self.assertEqual(entry1.get_text(), '')

  def test_dialog1_response_cb(self):
    '''Ensure correct actions on dialog1 response'''

    dialog1 = self.view1.widgets['dialog1']
    dialog1.show()

    dialog1.response(1)
    refresh_ui(self.delay_secs)
    self.assertTrue(not dialog1.get_visible())

  def test_entry1_activate_cb(self):
    '''Ensure correct actions on entry1 activate'''

    [entry1, dialog1, textview1] = [self.view1.widgets[x] for x in
      ['entry1', 'dialog1', 'textview1']]
    dialog1.show()
    entry1.set_text('John Doe')

    entry1.activate()
    refresh_ui(self.delay_secs)
    iter_start = textview1.get_buffer().get_iter_at_offset(0)
    iter_end = textview1.get_buffer().get_iter_at_offset(-1)
    #self.assertEqual(textview1.get_buffer().get_slice(iter_start, iter_end,
    #  False), list(self.userifc.model._observers)[0].data)
    self.assertEqual(textview1.get_buffer().get_slice(iter_start, iter_end,
      False), self.userifc.view1._data)
    self.assertTrue(not dialog1.get_visible())
