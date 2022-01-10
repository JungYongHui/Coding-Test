#%%
class foo():
    def __init__(self) -> None:
        self.x=0

    def set_param(self,**kwargs):
        for k,v in kwargs.items():
            if hasattr(self,k):
                self.__setattr__(k,v)
            else: # raise error
                self.__getattribute__(k,v)
a=foo()
a.set_param(y=3)
a.x


# %%
for i in xrange(3):
    print(i)
# %%
