import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

one_hot = pd.DataFrame({value: [1 if val == value else 0 for val in data['whoAmI']] 
                        for value in data['whoAmI'].unique()})

one_hot.head()



