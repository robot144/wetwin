
import ipywidgets as widgets
from wtcore.variables import *

class WtIntSlider(widgets.IntSlider):
    def __init__(self,v: IntVariable, orientation='horizontal'):
        super().__init__(value=v.value, min=v.min, max=v.max, step=1,
        description=v.label, disabled=False, continuous_update=False,
        orientation=orientation) #, readout=True, readout_format='d' 
        self._variable=v
        self.observe(self.update_from_slider,names="value")
        v.observe(self)
    def update_from_slider(self,obj):
        print("signal from slider")
        self._variable.value=self.value
    def update(self,v: IntVariable):
        print(f"slider receives signal from variable {v.name}. Value is {v.value}\n")
        self.value=str(v.value)

class WtIntLabel(widgets.Label):
    def __init__(self,v: IntVariable, orientation='horizontal'):
        super().__init__(value=str(v.value), description=v.label, 
        disabled=False, orientation=orientation)
        self._variable=v
        v.observe(self)
    def update(self,v: IntVariable):
        print(f"signal from variable {v.name}. Value is {v.value}\n")
        self.value=str(v.value)

class WtListDropdown(widgets.Dropdown):
    def __init__(self,v: ListVariable, orientation='horizontal'):
        super().__init__(options=v._items, value=v.value_str,
        description=v.label, disabled=False, continuous_update=False,
        orientation=orientation)
        self._variable=v
        self.observe(self.update_from_dropdown,names="value")
        v.observe(self)
    def update_from_dropdown(self,obj):
        print("signal from dropdown")
        self._variable.value_str=self.value
    def update(self,v: ListVariable):
        print(f"dropdown receives signal from variable {v.name}. Value is {v.value_str}\n")
        if self.value!=v.value_str:
            self.value=v.value_str

class WtListLabel(widgets.Label):
    def __init__(self,v: ListVariable, orientation='horizontal'):
        super().__init__(value=v.value_str, description=v.label, 
        disabled=False, orientation=orientation)
        self._variable=v
        v.observe(self)
    def update(self,v: ListVariable):
        print(f"signal from variable {v.name}. Value is {v.value}\n")
        self.value=v.value_str