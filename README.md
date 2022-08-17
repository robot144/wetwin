# wetwin
Collaborative digital twin modelling

## First test for showing results on the web

Here we explore the use of jupyter notebooks, together with the package voila and the online service of mybinder.org to create a dashboard directly from a github repository with a jupyter notebook. The aim is 
to test if the development of a dashboard

Show the jupyter notebook online at mybinder.org
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/robot144/wetwin/HEAD?labpath=show_timeseries.ipynb)

You can also directly launch a notebook as an app in binder.
- for widgets.ipynb [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/robot144/wetwin/HEAD?urlpath=voila%2Frender%2Fwidgets.ipynb)
- for show_timeseries.ipynb [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/robot144/wetwin/HEAD?urlpath=voila%2Frender%2Fshow_timeseries.ipynb)

### Some technical notes

- Voila is a package that strips the code and editing functionality from a notebook and just shows the text and results. Together with ipywidgets you can make the page interactive and make the code respond to the buttons that you add.
- you can install voila also locally (with pip or conda) and run eg `voila widgets.ipynb` to preview the app locally first.
