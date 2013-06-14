Userifc_py.Javafx
===========================================
.. .rst to .html: rst2html5 foo.rst > foo.html
..                pandoc -s -f rst -t html5 -o foo.html foo.rst

JavaFX sub-package for Python User interface examples project.

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
        [JYTHONPATH="$PYUSERSITE"] jython -i userifc_py/javafx/hello_model.py

        >>> lib_main([])

or
        [JYTHONPATH="$PYUSERSITE"] jython
        
        >>> from javafx.scene import Scene
        
        >>> from javafx.application import Application
        
        >>> from userifc_py.javafx import hello_model, hello_formview
        
        >>> class JfxApp(Application):
        
		>>>   def start(self, stagePrime):
		
		>>> 	params = self.getParameters()
		
		>>> 	from userifc_py.javafx import hello_model, hello_formview
	
		>>> 	mod = hello_model.HelloModel('greet.txt')
		
		>>> 	view1 = hello_formview.HelloView()
	    
		>>> 	mod.attachObserver(view1)
		
		>>> 	mod.notifyObservers(params.getNamed()['data'])
		
		>>> 	print('view1.data:', view1.data)
		
		>>> 	stagePrime.setScene(Scene(view1.parent, 200, 160))
		
		>>> 	stagePrime.show() ; stagePrime.close()
        
        >>> data = 'To be set -- HELP.'
        
        >>> Application.launch(JfxApp, ['--data=' + data])

Author/Copyright
----------------
Copyright (c) 2013 by thebridge0491 <thebridge0491-codelab@yahoo.com>

License
-------
Licensed under the Apache-2.0 License. See LICENSE for details.
