Userifc_py.Aux
===========================================
.. .rst to .html: rst2html5 foo.rst > foo.html
..                pandoc -s -f rst -t html5 -o foo.html foo.rst

Auxiliary sub-package for Python User interface example project.

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
        python -i userifc_py/aux/subject.py
    
        >>> lib_main([])

or
        python
        
        >>> from userifc_py.aux import subject, observer
        
        >>> subj = subject.Subject()
        
        >>> obs = observer.Observer()
        
        >>> subj.attachObserver(obs)
        
        >>> subj.notifyObservers('To be set -- HELP.')
        
        >>> print('obs.data:', obs.data)

Author/Copyright
----------------
Copyright (c) 2013 by thebridge0491 <thebridge0491-codelab@yahoo.com>

License
-------
Licensed under the Apache-2.0 License. See LICENSE for details.
