plot_mercator.py
----------------

Summary
=======

This script subsets the AMSR-E 1 degree SST dataset for the tropical warm pool,
does a time average of months between 2003-4-1 and 2006-3-1 and plots
the result as a color image.   Once you've cloned the cookbook repository and
put tne tos_AMSRE_L3_v7_200206-201012.nc netcdf file in the cookbook directory,
make the plots using  the plot_mercator.ipynb notebook or plot_mercator.py

The SST dataset (23 Mbytes) used for this plot is available from:

ftp://podaac-ftp.jpl.nasa.gov/allData/amsre/L3/sst_1deg_1mo/tos_AMSRE_L3_v7_200206-201012.nc

and described at:

http://podaac.jpl.nasa.gov/dataset/AMSRE_L3_SST_1DEG_1MO

The source code is at:

https://github.com/phaustin/cookbook/blob/master/plot_mercator.py

and also uses the my_namedtuple class defined in:

https://github.com/phaustin/cookbook/blob/master/constants.py


IPython notebook
================

Click on this link for a read-only view of the notebook using nbviewer:

* `plot_mercator.ipynb <http://nbviewer.ipython.org/github/phaustin/cookbook/blob/master/notebooks/plot_mercator.ipynb?create=1>`_


To get the source code plus the IPython notebook in notebooks/plot_mercator.ipynb clone the
git repository::

  git clone https://github.com/phaustin/cookbook.git


