Userifc_py.Curses
===========================================
.. .rst to .html: rst2html5 foo.rst > foo.html
..                pandoc -s -f rst -t html5 -o foo.html foo.rst

Curses sub-package for Python User interface examples project.

Installation
------------
source code tarball download:
    
        # [aria2c --check-certificate=false | wget --no-check-certificate | curl -kOL]
        
        FETCHCMD='aria2c --check-certificate=false'
        
        $FETCHCMD https://bitbucket.org/thebridge0491/userifc_py/[get | archive]/master.zip

version control repository clone:
        
        git clone https://bitbucket.org/thebridge0491/userifc_py.git

cd <path> ; pip install --user -e .

python setup.py test

Usage
-----
        python -i userifc_py/curses/hello_model.py

        >>> lib_main([])

or
        python

        >>> from userifc_py.curses import hello_model, hello_formview

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
