# wetwin
Collaborative digital twin modelling

## First test for showing results on the web

Here we explore the use of jupyter notebooks, together with the package voila and the online service of mybinder.org to create a dashboard directly from a github repository with a jupyter notebook. The aim is 
to test if the development of a dashboard

Show the jupyter notebook online at mybinder.org
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/robot144/wetwin/HEAD?labpath=show_timeseries.ipynb)

You can also directly launch a notebook as an app in binder.
- for show_timeseries_from_nextcloud.ipynb [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/robot144/wetwin/HEAD?urlpath=voila%2Frender%2Fshow_timeseries_from_nextcloud.ipynb)

There are two other notebooks with more tests:
- for widgets.ipynb [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/robot144/wetwin/HEAD?urlpath=voila%2Frender%2Fwidgets.ipynb)
- for show_timeseries.ipynb [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/robot144/wetwin/HEAD?urlpath=voila%2Frender%2Fshow_timeseries.ipynb)


### Some technical notes

- Voila is a package that strips the code and editing functionality from a notebook and just shows the text and results. Together with ipywidgets you can make the page interactive and make the code respond to the buttons that you add.
- you can install voila also locally (with pip or conda) and run eg `voila widgets.ipynb` to preview the app locally first.
- The standard netCDF4 library cannot read from a regular download, ie one that is not backed by opendap. Using Xarray, this can be done however. The advantage is that a regular web-url will be enough to access the netcdf file. This can for example easily be done using research-drive from surfsara (https://researchdrive.surfsara.nl/index.php/login), which can be obtained together with an account on Snellius or Lisa, or surfdrive as available to all employees of the TU Delft (surfdrive.surf.nl). It is also possible to rent storage commercially (eg at hetzner.de storage share 3 to 5 euro/Tb/month). There re many options.