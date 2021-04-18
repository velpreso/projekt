import numpy as np
#funkcja preprocessing
def parametry_sterujace():
    global c, f, xa, xb, lw, z, wezly, elementy; 
    global twb_L, twb_P, wwb_L, wwb_P;
    c=0;
    f=0;
    xa=0; #poczatek przedzialu
    xb=1; #koniec przedzialu
    lw=10; #liczba wezlow
    z=n-1; #liczba elementow
    
    #tablica wezlow
    wezly=np.array([[1, 0],
                    [2, 1],
                    [3, 0.5],
                    [4, 0.75]])
    
    #tablica elementow
    elementy=np.array([[1, 1, 3],
                       [2, 3, 2],
                       [3, 3, 4]])
     
    #warunki brzegowe 
    twb_L = 'D'; #lewy brzeg Dirichlet
    twb_P = 'D'; #prawy brzeg Dirichlet
    wwb_L = 0; 
    wwb_P = 1;

#parametry_sterujace() #testowe wywołanie funckji
