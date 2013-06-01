Userifc_py.Demo
===========================================
.. .rst to .html: rst2html5 foo.rst > foo.html
..                pandoc -s -f rst -t html5 -o foo.html foo.rst

Main app sub-package for Python User interface examples project.

Installation
------------
source code tarball download:
    
        # [aria2c --check-certificate=false | wget --no-check-certificate | curl -kOL]
        
        FETCHCMD='aria2c --check-certificate=false'
        
        $FETCHCMD https://bitbucket.org/thebridge0491/userifc_py/[get | archive]/master.zip

version control repository clone:
        
        git clone https://bitbucket.org/thebridge0491/userifc_py.git

cd <path> ; pip install --user -e .

$FETCHCMD http://peak.telecommunity.com/dist/ez_setup.py # jython setuptools

jython ez_setup.py

cd <path> ; jython setup.py develop -d $HOME/.local/bin/Lib/site-packages

python setup.py test

Usage
-----
        [env RSRC_PATH=<path>/resources] [p|j]ython -m userifc_py.demo

or
        [env RSRC_PATH=<path>/resources] [p|j]ython userifc_py/demo/cli.py

or
        [env RSRC_PATH=<path>/resources] [p|j]ython
    
        >>> from userifc_py.demo import cli
    
        >>> cli.main([])

Author/Copyright
----------------
Copyright (c) 2013 by thebridge0491 <thebridge0491-codelab@yahoo.com>

License
-------
Licensed under the Apache-2.0 License. See LICENSE for details.
