#define Variables
#
# IntVariable(name: str,label: str, min_val:int, max_val:int, initial_val:int)
# ListVariable(name: str,label: str, items=[])


"""
Variable is an abstract class for a variable (integer, float,...). It encapsulates the python 
variable and and a name, and methods to observe changes to the variable. Using the observer
pattern changes to a variable ca be forwarded to other classes. Variables are used here as links
between gui elements. For example, a slider can be coupled to plot. All gui-elements that link
to the same variable will be synced automatically. Though you may have to program what an update()
entails.
The name and label of a variable cannot be changed after creation (TODO decide if we want to keep this).
The getters myvar.name and myvar.label, denote the id of the variable and the label to be used eg in
gui-elements, eg Variable(name="tstart","Start of simulation")
You'll never use this class directly, but use the derived types such as IntVariable.
"""
class Variable():
    def __init__(self,name: str, label:str):
        self._name=name
        self._label=label
        self._observers=[]
        self._value=None
    def observe(self,observer): 
        # an observer is a function that is called when the variable is changed
        # the only argument is the variable
        self._observers.append(observer)
    @property
    def name(self): # to allow for temp=variable.name
        return self._name
    #make immutable
    #@name.setter 
    #def name(self,new_name: str): # allow for variale.name=new_name
    #    self._name=new_name
    @property
    def label(self):
        return self._label
    #@label.setter
    #def label(self,new_label: str):
    #    self._label=new_label

"""
IntVariable encapsulates a python integer, see Variable for more info.
It also adds a miniumum and maximum value to define the valid range, eg
for use in a slider. Typical use cases, layer number and number of particles
"""
class IntVariable(Variable):
    def __init__(self,name: str,label: str, min_val:int, max_val:int, initial_val:int):
        super().__init__(name,label)
        self._min=min_val
        self._max=max_val
        self._value=initial_val
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self,new_value: int):
        print(f"set value of {self.name} to {new_value}\n")
        #truncate to range
        v=max(new_value,self._min)
        v=min(v,self._max)
        self._value=v
        #inform observers
        for obs in self._observers:
            obs.update(self)
    @property
    def min(self):
        return self._min
    @property
    def max(self):
        return self._max

"""
ListVariable encapsulates a python list, see Variable for more info.
Typical use case, list of location names
"""
class ListVariable(Variable):
    def __init__(self,name: str,label: str, items=[]):
        super().__init__(name,label)
        self._items=items
        if len(items)<1:
            self._value=None
        else:
            self._value=0
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self,new_value: int):
        print(f"set value of {self.name} to {new_value}\n")
        #truncate to range
        n=len(self._items)
        if n>0:
            value=max(new_value,0)
            value=min(value,n-1)
            self._value=value 
            #inform observers
            for obs in self._observers:
                obs.update(self)
    @property
    def value_str(self):
        if self._value==None:
            return ""
        else:
            res=self._items[self._value]
            return res
    @value_str.setter
    def value_str(self,new_value: str):
        print(f"set value of {self.name} to {new_value}\n")
        #truncate to range
        n=len(self._items)
        if n>0:
            if new_value in self._items:
                ivalue=self._items.index(new_value)
                self._value=ivalue 
                #inform observers
                for obs in self._observers:
                    obs.update(self)

