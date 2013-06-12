Userifc_py.Swing
===========================================
.. .rst to .html: rst2html5 foo.rst > foo.html
..                pandoc -s -f rst -t html5 -o foo.html foo.rst

Swing sub-package for Python User interface examples project.

Installation
------------
source code tarball download:
    
        # [aria2c --check-certificate=false | wget --no-check-certificate | curl -kOL]
        
        FETCHCMD='aria2c --check-certificate=false'
        
        $FETCHCMD https://bitbucket.org/thebridge0491/userifc_py/[get | archive]/master.zip

version control repository clone:
        
        git clone https://bitbucket.org/thebridge0491/userifc_py.git

$FETCHCMD http://peak.telecommunity.com/dist/ez_setup.py # jython setuptools

PYUSERSITE=`python -m site --user-site` ; JYUSERSITE=`jython -m site --user-site`

jython ez_setup.py -d $JYUSERSITE setuptools

cd <path> ; [JYTHONPATH="$PYUSERSITE"] jython setup.py develop -d $JYUSERSITE

[JYTHONPATH="$PYUSERSITE"] jython -m unittest discover .

Usage
-----
        [JYTHONPATH="$PYUSERSITE"] jython -i userifc_py/swing/hello_model.py

        >>> lib_main([])

or
        [JYTHONPATH="$PYUSERSITE"] jython

        >>> from userifc_py.swing import hello_model, hello_formview

        >>> mod = hello_model.HelloModel('greet.txt')
        
        >>> view1 = hello_formview.HelloView()

        >>> mod.attachObserver(view1)
        
        >>> mod.notifyObservers('To be set -- HELP.')

        >>> print('view1.data:', view1.data)

Author/Copyright
----------------
Copyright (c) 2013 by thebridge0491 <thebridge0491-codelab@yahoo.com>

License
-------
Licensed under the Apache-2.0 License. See LICENSE for details.
