import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spint
from GeometriaDefinicja import *
from AutomatycznyGeneratorGeometrii import *
from RysujGeometrie import *
from Alokacja import *
from FunkcjeBazowe import *
from Aij import *

if __name__ == '__main__':
    c = 0
    f = lambda x:1  
    x_a = 0
    x_b = 1
    n = 5
    WB = [{"ind": 1, "typ":'D', "wartosc":0},
          {"ind": n, "typ":'D', "wartosc":1}]
    
    RysujGeometrie(WEZLY, ELEMENTY, MB)
   
    A,b=Alokacja(n)
    stopien_fun_bazowych = 1
    phi, dphi = FunkcjeBazowe(stopien_fun_bazowych)
    liczbaElementow = np.shape(ELEMENTY)[0]
    for ee in np.arange(0,liczbaElementow):
        elemRowInd = ee
        elemGlobalInd = ELEMENTY[ee, 0]
        elemWezel1 = ELEMENTY[ee, 1]
        elemWezel2 = ELEMENTY[ee, 2]
        
        x_a = WEZLY[elemWezel1-1, 1]
        x_b = WEZLY[elemWezel2-1, 1]
        
        Ml = np.zeros(stopien_fun_bazowych+1, stopien_fun_bazowych+1)
        J = (b-a)/2
        Ml[0.0] = spint.quad(Aij(dphi[0], dphi[0], c, phi[0], phi[0], -1, 1))

