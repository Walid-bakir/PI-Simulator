#!usr/bin/env python3
'''
donner une image animee avec les valeurs de pi
'''
import sys
import subprocess
from simulator import list_valeur

#dessiner les nombres
def put_point(liste_des_pixels):
    '''mettre un point dans le carre'''
    taille = len(liste_des_pixels[0])
    for i in range(5):
        for j in range(5):
            liste_des_pixels[int(i+(taille/2))][int(j+(taille/2))-50] = '0   0   0'
    return liste_des_pixels

def put_0(liste_des_pixels,position):
    '''mettre le nombre 0 dans le carre'''
    taille = len(liste_des_pixels[0])
    new_p = taille + (position)*50
    for i in range(80):
        liste_des_pixels[-i + int(taille/2)][int(new_p/2)] = '0  0  0'
        liste_des_pixels[-i + int(taille/2)][int(new_p/2)+20] = '0  0  0'
    for j in range(20):
        liste_des_pixels[int(taille/2)][j +int(new_p/2)] = '0  0  0'
        liste_des_pixels[int(taille/2) - 80][j +int(new_p/2)] = '0  0  0'
    return liste_des_pixels

def put_1(liste_des_pixels , position):
    '''mettre le nombre 1 dans le carre'''
    taille = len(liste_des_pixels[0])
    new_p = taille + (position)*50
    for i in range(80):
        liste_des_pixels[-i + int(taille/2)][int(new_p/2)+5] = '0  0  0'
    return liste_des_pixels

def put_2(liste_des_pixels,position):
    '''mettre le nombre 2 dans le carre'''
    taille = len(liste_des_pixels[0])
    new_p = taille + (position)*50
    for j in range(20):
        liste_des_pixels[int(taille/2)][j +int(new_p/2)] = '0  0  0'
        liste_des_pixels[int(taille/2) - 80][j +int(new_p/2)] = '0  0  0'
        liste_des_pixels[int(taille/2) - 40][j +int(new_p/2)] = '0  0  0'
    for i in range(40):
        liste_des_pixels[-i + int(taille/2)][int(new_p/2)] = '0  0  0'
    for i in range(40,80):
        liste_des_pixels[-i + int(taille/2)][int(new_p/2)+20] = '0  0  0'
    return liste_des_pixels

def put_3(liste_des_pixels,position):
    '''mettre le nombre 3 dans le carre'''
    taille = len(liste_des_pixels[0])
    new_p = taille + (position)*50
    for i in [int((taille/2)-40) , int(taille/2) , int((taille/2)-80) ]:
        for j in range(20):
            liste_des_pixels[i][int(-j + (new_p/2)+17)] = '0  0  0'
    for i in range(80):
        liste_des_pixels[-i + int(taille/2)][int(new_p/2)+17] = '0  0  0'

    return liste_des_pixels

def put_4(liste_des_pixels,position):
    '''mettre le nombre 4 dans le carre'''
    taille = len(liste_des_pixels[0])
    new_p = taille + (position)*50
    for i in range(40,80):
        liste_des_pixels[-i + int(taille/2)][int(new_p/2)] = '0  0  0'
    for i in range(80):
        liste_des_pixels[-i + int(taille/2)][int(new_p/2)+20] = '0  0  0'
    for j in range(20):
        liste_des_pixels[int(taille/2)-40][int(new_p/2)+j] = '0  0  0'
    return liste_des_pixels

def put_5(liste_des_pixels,position):
    '''mettre le nombre 5 dans le carre'''
    taille = len(liste_des_pixels[0])
    new_p = taille + (position)*50
    for j in range(20):
        liste_des_pixels[int(taille/2)][j +int(new_p/2)] = '0  0  0'
        liste_des_pixels[int(taille/2) - 80][j +int(new_p/2)] = '0  0  0'
        liste_des_pixels[int(taille/2) - 40][j +int(new_p/2)] = '0  0  0'
    for i in range(40,80):
        liste_des_pixels[-i + int(taille/2)][int(new_p/2)] = '0  0  0'
    for i in range(40):
        liste_des_pixels[-i + int(taille/2)][int(new_p/2)+20] = '0  0  0'
    return liste_des_pixels

def put_6(liste_des_pixels,position):
    '''mettre le nombre 6 dans le carre'''
    taille = len(liste_des_pixels[0])
    new_p = taille + (position)*50
    liste_des_pixels = put_5(liste_des_pixels, position)
    for i in range(40):
        liste_des_pixels[-i + int(taille/2)][int(new_p/2)] = '0  0  0'
    return liste_des_pixels

def put_7(liste_des_pixels,position):
    '''mettre le nombre 7 dans le carre'''
    taille = len(liste_des_pixels[0])
    new_p = taille + (position)*50
    for i in range(80):
        liste_des_pixels[-i + int(taille/2)][int(new_p/2)+20] = '0  0  0'
    for j in range(20):
        liste_des_pixels[int(taille/2) - 80][20-j +int(new_p/2)] = '0  0  0'
    return liste_des_pixels

def put_8(liste_des_pixels,position):
    '''mettre le nombre 8 dans le carre'''
    taille = len(liste_des_pixels[0])
    new_p = taille + (position)*50
    liste_des_pixels = put_0(liste_des_pixels, position)
    for j in range(20):
        liste_des_pixels[int(taille/2)-40][j+int(new_p/2)] = '0  0  0'
    return liste_des_pixels

def put_9(liste_des_pixels,position):
    '''mettre le nombre 9 dans le carre'''
    taille = len(liste_des_pixels[0])
    new_p = taille + (position)*50
    liste_des_pixels = put_5(liste_des_pixels, position)
    for i in range(40,80):
        liste_des_pixels[-i + int(taille/2)][int(new_p/2)+20] = '0  0  0'
    return liste_des_pixels


def get_valeur_in_list(liste_des_pixels,list_de_nbrs):
    '''
    mettre les pixels correspendants a dessiner les element de la valeur de pi,
    dans la list des pixels
    '''
    for i in range(len(list_de_nbrs)):
        if list_de_nbrs[i] == '.':
            liste_des_pixels = put_point(liste_des_pixels)
        elif list_de_nbrs[i] == '0':
            liste_des_pixels = put_0(liste_des_pixels,i-3)
        elif list_de_nbrs[i] == '1':
            liste_des_pixels = put_1(liste_des_pixels,i-3)
        elif list_de_nbrs[i] == '2':
            liste_des_pixels = put_2(liste_des_pixels,i-3)
        elif list_de_nbrs[i] == '3':
            liste_des_pixels = put_3(liste_des_pixels,i-3)
        elif list_de_nbrs[i] == '4':
            liste_des_pixels = put_4(liste_des_pixels,i-3)
        elif list_de_nbrs[i] == '5':
            liste_des_pixels = put_5(liste_des_pixels,i-3)
        elif list_de_nbrs[i] == '6':
            liste_des_pixels = put_6(liste_des_pixels,i-3)
        elif list_de_nbrs[i] == '7':
            liste_des_pixels = put_7(liste_des_pixels,i-3)
        elif list_de_nbrs[i] == '8':
            liste_des_pixels = put_8(liste_des_pixels,i-3)
        elif list_de_nbrs[i] == '9':
            liste_des_pixels = put_9(liste_des_pixels,i-3)
    return liste_des_pixels



def generate_ppm_file(valeur_de_pi : str ,liste_des_pixels : list, num : int):
    '''
    generer l'image numero num depuis la list des valeur_de_pixels
    d'hauteur et largeur = taille
    '''
    list_de_nbrs = list(valeur_de_pi) # valeur est la str de la valeur de valeur_de_pi approchee
    taille = len(liste_des_pixels[0])
    liste_des_pixels = get_valeur_in_list(liste_des_pixels,list_de_nbrs)
    file1 = open(f'img{num}.ppm', 'w')
    file1.write("P3\n"+str(taille)+" "+str(taille)+"\n255\n")
    for elt in liste_des_pixels:
        for sous_elt in elt:
            file1.write(sous_elt)
            file1.write('  ')
    file1.close()


def main():
    '''point d'entre du code'''
    taille = sys.argv[1]
    nbr_points = sys.argv[2]
    occurence = sys.argv[3] # nombre de nombres apres la virgule
    if len(sys.argv) < 4:
        raise IndexError("il faut au moins trois nombres ")
    if not taille.isdecimal() or not nbr_points.isdecimal() or not occurence.isdecimal():
        raise IndexError("les entrees en ligne de commande doivent etre des entiers positifs")
    taille = int(taille)
    nbr_points = int(nbr_points)
    occurence = int(occurence) # nombre de nombres apres la virgule
    i = 10
    while i > 0: # dix images
        nbr = nbr_points//i
        valeur_de_pi = str(list_valeur(taille,nbr)[1]) # extraire la valeur de pi
        valeur_de_pi = valeur_de_pi[:occurence + 2]
        liste_des_pixels = list_valeur(taille,nbr)[0] # la liste des pixels
        generate_ppm_file(valeur_de_pi,liste_des_pixels,11-i)
        i -= 1
    subprocess.run("convert -delay 100 img*.ppm images_anime.gif", check=True, shell=True)



if __name__ == '__main__':
    main()
