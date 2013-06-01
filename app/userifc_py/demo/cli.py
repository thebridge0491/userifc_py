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
        default = None, choices = [None, 'term'],
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
        'term': run_demo
    }
    func = switcher.get(opts_hash.ifc, lambda x, y, z:
        print('Invalid interface: {0}'.format(opts_hash.ifc)))
    func(opts_hash.user, rsrc_path=rsrc_path)
    #run_demo(opts_hash.user, rsrc_path=rsrc_path)

    logging.shutdown()
    return 0

if '__main__' == __name__:
    sys.exit(main(sys.argv[1:]))
