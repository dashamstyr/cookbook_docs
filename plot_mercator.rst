.. index:: Basemap, pcolormesh, colorbar 

plot_mercator.py
----------------

Summary
=======

This script subsets the AMSR-E 1 degree SST dataset for the tropical warm pool,
does a time average of months between 2003-4-1 and 2006-3-1 and plots
the result as a color image, with a colorbar that has adjustable upper and
lower values and a reserved color for missing values.   
Once you've cloned the cookbook repository and
put tne tos_AMSRE_L3_v7_200206-201012.nc netcdf file in the cookbook directory,
make the plots using  the plot_mercator.ipynb notebook or plot_mercator.py

Click on this link for a read-only view of the notebook using nbviewer:

* `plot_mercator.ipynb <http://nbviewer.ipython.org/github/phaustin/cookbook/blob/master/notebooks/plot_mercator.ipynb?create=1>`_

The source code is at:

* `plot_mercator.py <https://github.com/phaustin/cookbook/blob/master/plot_mercator.py>`_


To get the source code plus the IPython notebook in notebooks/plot_mercator.ipynb go to

* :ref:`downloads`


Dependencies
============

Uses routines from `slice_nc.py <slice_nc.html>`_ 




