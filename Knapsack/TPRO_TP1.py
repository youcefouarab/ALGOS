EX1 = {
    "1" : {"w" : 7, "v" : 11, "x" : 0},
    "2" : {"w" : 6, "v" : 8, "x" : 0},
    "3" : {"w" : 4, "v" : 5, "x" : 0},
}
EX1wmax = 10

EX2 = {
    "1" : {"w" : 1, "v" : 1, "x" : 0},
    "2" : {"w" : 3, "v" : 4, "x" : 0},
    "3" : {"w" : 4, "v" : 5, "x" : 0},
    "4" : {"w" : 5, "v" : 7, "x" : 0},
    "5" : {"w" : 1, "v" : 9, "x" : 0}
}
EX2wmax = 7

EX3 = {
    "1" : {"w" : 2, "v" : 10, "x" : 0},
    "2" : {"w" : 3, "v" : 5, "x" : 0},
    "3" : {"w" : 5, "v" : 15, "x" : 0},
    "4" : {"w" : 7, "v" : 7, "x" : 0},
    "5" : {"w" : 1, "v" : 6, "x" : 0},
    "6" : {"w" : 4, "v" : 18, "x" : 0},
    "7" : {"w" : 1, "v" : 3, "x" : 0}
}
EX3wmax = 15

def tab_sac_dyn(objets, wmax):
    gains = [[0]*(wmax+1)]
    for i in range(1, len(objets)+1):
        gains.insert(i, [0]*(wmax+1))
        for j in range(1, wmax+1):
            if j<objets.get(str(i)).get("w"): gains[i][j] = gains[i-1][j]
            else: gains[i][j] = max(gains[i-1][j], objets.get(str(i)).get("v")+gains[i-1][j-objets.get(str(i)).get("w")])
    return gains

def sac_dyn(objets, wmax):
    gains = tab_sac_dyn(objets, wmax)
    g = gains[len(objets)][wmax]
    for i in range(len(objets), 0, -1):
        if g not in gains[i-1]:
            objets[str(i)]["x"] = 1
            g -= objets[str(i)]["v"]

def resoudre(objets, wmax) :
    print("\nExemple 1 :")
    print(objets)
    gains = tab_sac_dyn(objets, wmax)
    for i in range(0, len(objets)+1): print(gains[i])
    sac_dyn(objets, wmax)
    for i in range(1, len(objets)+1): print(str(i)+str(objets[str(i)]))

resoudre(EX1, EX1wmax)
resoudre(EX2, EX2wmax)
resoudre(EX3, EX3wmax)