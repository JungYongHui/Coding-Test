#%%
def foo(num):
    if num < foo.min:
        foo.min = num
    elif num > foo.max:
        foo.max = num

# %%
n = int(input())
nums = list(map(int,input().split()))
foo.min = foo.max = nums[0]
for num in nums[1:]:
    foo(num)
print(foo.min * foo.max)
# %%