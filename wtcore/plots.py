# define plots
#
# 
import ipywidgets as widgets
import matplotlib.pyplot as plt

class wtPlot(widgets.Output):
    def __init__(self,variables,*args,**kwargs):
        # layout = widgets.Layout(width="100%",height='400px')
        super().__init__(*args,**kwargs)
        fig, ax = plt.subplots() #figsize=(6, 4)
        fig.canvas.header_visible = False
        fig.tight_layout()
        self._fig=fig
        self._ax=ax
        self._variables=variables
        for v in variables:
            v.observe(self)
    @property
    def caller(self):
        return self._caller
    @property
    def ax(self):
        return self._ax
    @property
    def fig(self):
        return self._fig
    @property
    def variables(self):
        return self._variables
    def redraw(self): pass 
    def update(self,v):
        self._caller=v
        self._ax.clear
        self.redraw()