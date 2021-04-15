import numpy as np
def parametry_sterujace():
    global c, f, xa, xb, n, z;
    c=0;
    f=0;
    xa=0; #poczatek przedzialu
    xb=1; #koniec przedzialu
    n=10; #liczba wezlow
    z=n-1; #liczba elementow
    wezly=np.array([[1, 0],
                    [2, 1],
                    [3, 0.5],
                    [4, 0.75]])
    elementy=np.array([[1, 1, 3],
                       [2, 3, 2],
                       [3, 3, 4]])      
parametry_sterujace()
