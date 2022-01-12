#%%
def foo():
    print('foo 실행')
    print(__name__)
    foo.a=2
    print(foo.a)
foo()
foo.a = 3
foo.a
getattr(foo,'a')
# %%
getattr(globals,'foo')
# %%
if __name__==_:
    print('__name__')
# %%
__package__
# %%
locals()
# %%
