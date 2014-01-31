.. _build:

Notes on adding a paper/edting webpages
=======================================

0) Pro-tip: There's a nice emacs mode for rst files: http://docutils.sourceforge.net/docs/user/emacs.html

1) Clone the repository via ssh::

     git clone ssh://jcole@roc.eos.ubc.ca/users/phil/repos/feedback_papers

2) To get a bibtex entry from a doi use my crossref.py script::

     phil@denmank% python crossref.py 10.1175/JCLI-D-11-00726.1

     @ARTICLE{Sanderson12,
     author = {Sanderson, Benjamin M. and Shell, Karen M.},
     title = {Model-Specific Radiative Kernels for Calculating Cloud and Noncloud Climate Feedbacks},
     journal = {J. Climate},
     volume = {25},
     number = {21},
     year = {2012},
     pages = {7607-7624},
     doi = {10.1175/JCLI-D-11-00726.1},
     resource = {url=http://journals.ametsoc.org/doi/abs/10.1175/JCLI-D-11-00726.1},
     }

3) Append this bibitem to feedbacks.bib

4) Make sure you have the pybtex and sphinx-bibtex modules installed::

     pip install --upgrade pybtex

     pip install --upgrade sphinxcontrib-bibtex

5) Run readit.py to produce a new reference list with journal URLs called index_out.rst::

     python readit.py

6) Add the URL-enhanced journal item to index.rst::
 
     * :cite:`Sanderson12`:  `Sanderson12: Model-Specific ...

7) Rebuild the web pages::

     bash doit.sh

8) When you're ready -- commit and push your changes and I'll rebuild the website  (or if you're working
   on roc), you could rebuild the website in your home directory and I'll rsync it to the server.
