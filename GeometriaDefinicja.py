import numpy as np

def GeometriaDefinicja():
    NODES = np.array([[1, 0],
                      [2, 1],
                      [3, 0.5],
                      [4, 0.75]])

    ELEMS=np.array([[1, 1, 3],
                    [2, 3, 2],
                    [3, 3, 4]])
    WB = [{"ind": 1, "typ":'D', "wartosc":1},
          {"ind": 2, "typ":'D', "wartosc":2}]
    
    return NODES, ELEMS, WB
