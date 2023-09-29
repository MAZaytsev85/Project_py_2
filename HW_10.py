import pandas as pd
# import random
#
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()


def onehot_df(data, col='whoAmI'):
  df = pd.DataFrame({col: data[col],'tmp': [1] * len(data)})
  return pd.pivot_table(data = df, index = data.index, columns = df[col], fill_value = 0).droplevel(0, axis = 1).rename_axis('', axis = 1)

