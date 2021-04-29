import numpy as np

def Aij(df_i,df_j):
    fun_podc = lambda x: -df_i(x)*df_j(x)
    return fun_podc