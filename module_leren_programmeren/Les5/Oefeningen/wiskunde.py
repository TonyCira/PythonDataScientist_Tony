import math

def oppv_vierkant(zijde):
    return zijde ** 2

def oppv_rechthoek(lengte, breedte):
    return lengte * breedte

def oppv_cirkel(straal):
    return math.pi * straal ** 2

def inhoud_kubus(zijde):
    return zijde ** 3

def inhoud_balk(lengte, breedte, hoogte):
    return lengte * breedte * hoogte

def inhoud_cilinder(straal, hoogte):
    return math.pi * straal ** 2 * hoogte