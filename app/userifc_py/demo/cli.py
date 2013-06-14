# -*- coding: utf-8 -*-
'''Command line interface module for userifc_py-demo.

'''

from __future__ import (absolute_import, division, print_function,
    unicode_literals)

import os, sys, argparse, json
import logging, inspect
#from future.builtins import (ascii, filter, hex, map, oct, zip, str, open, dict)

from intro_py import util
from userifc_py import demo

__all__ = ['main']

# -- run w/out compile --
# python script.py [arg1 argN]
# 
# -- run REPL, import script, & run --
# python
# >>> from . import script.py
# >>> script.main([arg1, argN])
# 
# -- help/info tools in REPL --
# help(), quit(), help(<object>), help([modules|keywords|symbols|topics])
# 
# -- show module/type info --
# ex: pydoc list OR python> help(list)


logging.basicConfig(level = logging.DEBUG)
MODULE_LOGGER = logging.getLogger(__name__)

def deserialize_str(str1, fmt='json'):
	if str1 is not None:
		if 'json' == fmt:
			return json.loads(str1)
		elif 'yaml' == fmt:
			try:
				import yaml
				return yaml.load(str1)
			except ImportError as exc:
				print(repr(exc))
		elif 'toml' == fmt:
			try:
				import toml
				return toml.loads(str1)
			except ImportError as exc:
				print(repr(exc))
	return {}

def run_demo(name, rsrc_path=None):
    import re
    from datetime import datetime

    rexp = re.compile('(^quit$)', re.I)
    print('{0} match: {1} to {2}'.format('Good' if rexp.match(name)
        else 'Does not', name, rexp.pattern))

    greet_str = demo.greeting('greet.txt', name, rsrc_path=rsrc_path)
    print('{0}\n{1}'.format(datetime.now().strftime('%c'), greet_str))

def run_demo_gtk(name, rsrc_path=None):
    import re
    from datetime import datetime

    rexp = re.compile('(^quit$)', re.I)
    #os.environ['GTK_MAJOR_VERSION'] = 'LATEST'
    from userifc_py.gtk import hello_controller

    pretext = '{0}\n{1} match: {2} to {3}\n{4}\n'.format(
      hello_controller.userifc_version(), 'Good' if rexp.match(name)
      else 'Does not', name, rexp.pattern, datetime.now().strftime('%c'))
    uicontroller = hello_controller.HelloController('greet.txt', __name__)
    #uicontroller.view1.widgets['textview1'].props.buffer.props.text = pretext
    uicontroller.view1.widgets['textview1'].get_buffer().set_text(pretext)
    hello_controller.Gtk.main()

def run_demo_qt(name, rsrc_path=None, use_qtquick=False):
    import re
    from datetime import datetime

    rexp = re.compile('(^quit$)', re.I)
    #os.environ['QT_MAJOR_VERSION'] = 'LATEST'
    if use_qtquick:
      from userifc_py.qt.hello_quickcontroller import (HelloController, 
          QApplication, userifc_version)
    else:
      from userifc_py.qt.hello_controller import (HelloController, 
          QApplication, userifc_version)

    pretext = '{0}\n{1} match: {2} to {3}\n{4}\n'.format(
      userifc_version(), 'Good' if rexp.match(name)
      else 'Does not', name, rexp.pattern, datetime.now().strftime('%c'))
    app = QApplication([])
    uicontroller = HelloController('greet.txt', __name__)
    if use_qtquick:
      uicontroller.view1.widgets['textview1'].setProperty('text', pretext)
    else:
      uicontroller.view1.widgets['textview1'].setPlainText(pretext)
    app.exec_()

def run_demo_curses(name, rsrc_path=None):
    import re
    from datetime import datetime

    rexp = re.compile('(^quit$)', re.I)
    import curses
    from userifc_py.curses import hello_controller

    pretext = '{0}\n{1} match: {2} to {3}\n{4}\n'.format(
      hello_controller.userifc_version(), 'Good' if rexp.match(name)
      else 'Does not', name, rexp.pattern, datetime.now().strftime('%c'))
    uicontroller = hello_controller.HelloController('greet.txt', __name__)
    uicontroller.view1.stdscr.addstr(1, 1, pretext, curses.A_REVERSE)
    uicontroller.run()

def run_demo_tcltk(name, rsrc_path=None):
    import re
    from datetime import datetime

    rexp = re.compile('(^quit$)', re.I)
    import curses
    from userifc_py.tcltk import hello_controller

    pretext = '{0}\n{1} match: {2} to {3}\n{4}\n'.format(
      hello_controller.userifc_version(), 'Good' if rexp.match(name)
      else 'Does not', name, rexp.pattern, datetime.now().strftime('%c'))
    app = hello_controller.tk.Tk()
    uicontroller = hello_controller.HelloController(app, 'greet.txt',
      __name__)
    uicontroller.view1.widgets['textview1'].delete(1.0,
      hello_controller.tk.END)
    uicontroller.view1.widgets['textview1'].insert(hello_controller.tk.INSERT,
      pretext)
    app.mainloop()

def run_demo_wxwidgets(name, rsrc_path=None):
    import re
    from datetime import datetime

    rexp = re.compile('(^quit$)', re.I)
    from userifc_py.wxwidgets import hello_controller

    pretext = '{0}\n{1} match: {2} to {3}\n{4}\n'.format(
      hello_controller.userifc_version(), 'Good' if rexp.match(name)
      else 'Does not', name, rexp.pattern, datetime.now().strftime('%c'))
    #initialized wx.App(False) in HelloController
    uicontroller = hello_controller.HelloController('greet.txt', __name__)
    uicontroller.view1.widgets['textview1'].SetValue(pretext)
    uicontroller.app.MainLoop()

def run_demo_swing(name, rsrc_path=None):
    import re
    from datetime import datetime

    rexp = re.compile('(^quit$)', re.I)
    from userifc_py.swing import hello_controller
    #from java.awt import EventQueue

    pretext = '{0}\n{1} match: {2} to {3}\n{4}\n'.format(
      hello_controller.userifc_version(), 'Good' if rexp.match(name)
      else 'Does not', name, rexp.pattern, datetime.now().strftime('%c'))
    #EventQueue.invokeLater(hello_controller.App(pretext, 'greet.txt',
    #  __name__))
    uicontroller = hello_controller.HelloController('greet.txt', __name__)
    uicontroller.view1.widgets['textview1'].text = pretext

if 'java' in sys.platform.lower():
    from userifc_py.javafx import hello_controller
    from javafx.scene import Scene
    from javafx.application import Application
    
    class JfxApp(Application):
      def start(self, stagePrime):
        params = self.getParameters()
        param0 = params.getRaw()[0] if 0 < len(params.getRaw()) else ''
        
        uicontroller = hello_controller.HelloController(stagePrime,
          'greet.txt', 'userifc_py.javafx')
        uicontroller.view1.widgets['textview1'].text = \
          params.getNamed()['pretext']
        stagePrime.setScene(Scene(uicontroller.view1.parent, 200, 160))
        stagePrime.show()

def run_demo_javafx(name, rsrc_path=None):
    import re
    from datetime import datetime

    rexp = re.compile('(^quit$)', re.I)
    #from userifc_py.javafx import hello_controller

    pretext = '{0}\n{1} match: {2} to {3}\n{4}\n'.format(
      hello_controller.userifc_version(), 'Good' if rexp.match(name)
      else 'Does not', name, rexp.pattern, datetime.now().strftime('%c'))
    
    #JfxApp.launch(JfxApp, ['--pretext=' + pretext])
    Application.launch(JfxApp, ['--pretext=' + pretext])

def parse_cmdopts(args=None):
    func_name = inspect.stack()[0][3]
    MODULE_LOGGER.info(func_name + '()')

    opts_parser = argparse.ArgumentParser()

    opts_parser.add_argument('-v', '--log_lvl', action = 'store',
        default = None, choices = [None, 'debug', 'info', 'warning', 'error',
        'critical'], dest = 'log_lvl', help = 'Set logging level')
    opts_parser.add_argument('-l', '--log', action = 'store', type = str,
        default = 'cfg', choices = [None, 'basic', 'cfg'],
        dest = 'log_opt', help = 'Set logging config')
    opts_parser.add_argument('-u', '--user', action = 'store', type = str,
        default = 'World', help = 'set name')
    opts_parser.add_argument('-i', '--ifc', action = 'store', type = str,
        default = None, choices = [None, 'term', 'gtk', 'qt', 'qtquick',
        'curses', 'tcltk', 'wxwidgets', 'swing', 'javafx'],
        dest = 'ifc', help = 'Set user interface')

    return opts_parser.parse_args(args)

def main(argv=None):
    '''Main entry.

    Args:
        argv (list): list of arguments
    Returns:
        int: A return code
    Demonstrates Python syntax
    '''
    
    rsrc_path = os.environ.get('RSRC_PATH')
    logjson_str = util.read_resource('logging.json', rsrc_path=rsrc_path)
    log_cfg = deserialize_str(logjson_str, fmt='json')
    util.config_logging('info', 'cfg', log_cfg)
    opts_hash = parse_cmdopts(argv)
    util.config_logging(opts_hash.log_lvl, opts_hash.log_opt, log_cfg)
    MODULE_LOGGER.info('main()')

    cfg_blank = {'hostname':'???', 'domain':'???', 'file1':{'path':'???', 
        'ext':'txt'}, 'user1':{'name':'???', 'age': -1}}
    cfg_ini = dict(cfg_blank.items())
    cfg_ini.update(util.ini_to_dict(util.read_resource('prac.conf',
        rsrc_path=rsrc_path)).items())
    #cfg_json = dict(cfg_blank.items())
    #cfg_json.update(deserialize_str(util.read_resource('prac.json',
    #   rsrc_path=rsrc_path)).items())
    #cfg_yaml = dict(cfg_blank.items())
    #cfg_yaml.update(deserialize_str(util.read_resource('prac.yaml',
    #   rsrc_path=rsrc_path), fmt='yaml').items())
    #cfg_toml = dict(cfg_blank.items())
    #cfg_toml.update(deserialize_str(util.read_resource('prac.toml',
    #   rsrc_path=rsrc_path), fmt='toml').items())
    
    tup_arr = [
        (cfg_ini, cfg_ini['domain'], cfg_ini['user1']['name'])
        #, (cfg_json, cfg_json['domain'], cfg_json['user1']['name'])
        #, (cfg_yaml, cfg_yaml['domain'], cfg_yaml['user1']['name'])
        #, (cfg_toml, cfg_toml['domain'], cfg_toml['user1']['name'])
    ]
    
    for (cfg, domain, user1Name) in tup_arr:
        print('\nconfig: {0}'.format(cfg))
        print('domain: {0}'.format(domain))
        print('user1Name: {0}'.format(user1Name))
    print('')
    
    switcher = {
        None: run_demo,
        'term': run_demo,
        'gtk': run_demo_gtk,
        'qt': run_demo_qt,
        'qtquick': lambda u, rsrc_path: run_demo_qt(u, rsrc_path,
            use_qtquick=True),
        'curses': run_demo_curses,
        'tcltk': run_demo_tcltk,
        'wxwidgets': run_demo_wxwidgets,
        'swing': run_demo_swing,
        'javafx': run_demo_javafx
    }
    func = switcher.get(opts_hash.ifc, lambda x, y, z:
        print('Invalid interface: {0}'.format(opts_hash.ifc)))
    func(opts_hash.user, rsrc_path=rsrc_path)
    #run_demo(opts_hash.user, rsrc_path=rsrc_path)

    logging.shutdown()
    return 0

if '__main__' == __name__:
    sys.exit(main(sys.argv[1:]))
