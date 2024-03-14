# 1. How to import pandas and check the version?
import pandas as pd
import numpy as np

# print(pd.__version__)
# print(pd.show_versions())

# 2. How to create a series from a list, numpy array and dict?

# mylist = list('abcedfghijklmnopqrstuvwxyz')
# myarr = np.arange(26)
# mydict = dict(zip(mylist, myarr))
#
# print(mylist)
# print(myarr)
# print(mydict)
#
# s1 = pd.Series(mylist)
# s2 = pd.Series(myarr)
# s3 = pd.Series(mydict)
#
# # print(s1)
# # print(s2)
# # print(s3)

# 3. How to convert the index of a series into a column of a dataframe?

# mylist = list('abcedfghijklmnopqrstuvwxyz')
# s1 = pd.Series(mylist)
# # df = s1.to_frame().reset_index()
# # print(df)
#
# # Alternate method by me
# df1 = pd.DataFrame(s1).reset_index()
# print(df1)

# 4. How to combine many series to form a dataframe?

# mylist = list('abcedfghijklmnopqrstuvwxyz')
# myarr = np.arange(26)
# mydict = dict(zip(mylist, myarr))
#
# s1 = pd.Series(mylist)
# s2 = pd.Series(myarr)
# s3 = pd.Series(mydict)
#
# df = pd.DataFrame({'col1': s1, 'col2': s2, 'col3': s3})
# print(df) # NAN are visible because s3's index is different from s1 and s2 since it is dict.

# 5. How to assign name to the series’ index?

# myarr = np.arange(26)
# mydict = dict(zip(myarr, myarr))
# s2 = pd.Series(myarr)
# s3 = pd.Series(mydict)
#
# s2.name = 'Shaileja'
# s3.name = 'Jungkook'

# df = pd.DataFrame({s2.name: s2, s3.name: s3})
# print(df)

