#%%
import pandas as pd

data_info = {'standard1': [None, None, None, None, 929],
            'longTP'   : [4000, 7000, None, None, 936],
            'shortTP'  : [6500, 7000, None, None, 936],
            'pause'    : [None, None, 7000,  500, 936],
            'standard2': [None, None, None, None, 936],
            'slow'     : [None, None, None, None, 1637],
            'standard3': [None, None, None, None, 938],
            'fast'     : [None, None, None, None, 576]}

# %%
df1 = pd.DataFrame(
    data_info,
    index = [
        'TP_start', 'TP_end', 'pause_start', 'pause_time', 'reference_time'
        ]
    ).T

def foo(x:pd.Series):
    """
    clac by col
    """
    y = x
    cond = x.notnull()
    replace_ = (y[cond]*df1['reference_time'][cond]/9700).astype('float')
    y[cond] = replace_.round() # round
    return y

# 데이터 프레임 생성    
df2 = pd.DataFrame()

# '1' , '2', '3' 계산
df2[['1','2','3']] = df1[['TP_start', 'TP_end', 'pause_start']].apply(foo)

# '4' 계산
df2['4'] = df1['pause_time']+df2['3']

# 병합
df3 = pd.concat([df1,df2], axis=1)
# 전치
print(df3.T)

