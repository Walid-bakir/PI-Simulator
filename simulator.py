#!usr/bin/env python3
'''
importer les modules
'''

import sys
import random

def white_board(taille):
    '''
    creer un carre blanc de hauteur taille
    '''
    return [['255 255 255' for x in range(taille)] for y in range(taille)]


def dans_le_cercle(absc,ordo):
    '''
    test d'appartenance du point (absc,ord) au cercle unite
    '''
    return (absc**2 + ordo**2) <= 1

def translation(absc,ordo,taille):
    '''
    prendre deux valeurs (absc et ordo) dans [-1,1] et donner les
    entiers correspendants dans le carre de taille n = taille
    '''
    absc = absc*(taille/2)
    ordo = ordo*(taille/2)
    i = absc + taille/2
    j = ordo + taille/2
    return round(i) , round(j)

def list_valeur(taille,nbr_points):
    '''
    taille est la taille de carre
    nbr_points est le nombre de points dans la simulation
    cette fonction va donner la valeur de pi et la liste des
    pixels correspendante.
    '''
    contour = 0
    list_pixels = white_board(taille) # liste initiale
    for _ in range(nbr_points):
        absc = random.uniform(-1,1)
        ordo = random.uniform(-1,1)
        i , j = translation(absc,ordo,taille) # travailler avec les coordonnees de carre
        if dans_le_cercle(absc,ordo):
            contour += 1
            list_pixels[i%taille][j%taille] = '200  104  255'
        else:
            list_pixels[i%taille][j%taille] = '110  191  156'
    return (list_pixels,(4*contour)/nbr_points)


def valuer_pi(nbr_points):
    '''
    donner une valeur approche de pi en utilisant nbr_points points
    dans la simulation de M.C
    '''
    contour = 0
    for _ in range(1,nbr_points+1):
        absc = random.uniform(-1,1)
        ordo = random.uniform(-1,1)
        if dans_le_cercle(absc,ordo):
            contour += 1
    return (4*contour)/nbr_points


def main():
    '''
    point d'entrees
    '''
    nbr_points = sys.argv[1]
    if len(sys.argv) < 2:
        raise IndexError("il faut au moins un nombre ")
    if not nbr_points.isdecimal():
        raise IndexError("il faut au moins un nombre positif ")
    nbr_points = int(nbr_points)
    print(valuer_pi(nbr_points))

if __name__ == '__main__':
    main()
