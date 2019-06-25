import subprocess
import datetime
import time

uczeniowie=[]
oceny=[]
nauczyciele=[]
przedmioty=['matematyka', 'j.polski', 'geografia', 'biologia', 'fizyka']

def dodajUcznia():
    print('czekamy na kod')

def modyfikujUcznia():
    print('czekamy na kod')

def usunUcznia():
    print('czekamy na kod')

def ocenyUcznia():
    print('czekamy na kod')

def dodajOcene():
    print('czekamy na kod')

def najlepszyUczen():
    print('czekamy na kod')

def najgorszyUczen():
    print('czekamy na kod')

def najwyzszaSrednia():
    print('czekamy na kod')


tak = True
while tak == True:
    subprocess.call("cls", shell=True)
    print(' MENU: ')
    print('1 - Dodaj ucznia')
    print('2 - Modyfikuj ucznia')
    print('3 - Usun ucznia')
    print('4 - Oceny ucznia')
    print('5 - Dodaj ocenę')
    print('6 - Najlepszy uczeń')
    print('7 - Najgorszy uczeń')
    print('8 - Najwyższa średnia')
    print('0 - Koniec')
    wybor = int(input('Twój wybór: '))
    if wybor == 1:
        dodajUcznia()
    if wybor == 2:
        modyfikujUcznia()
    if wybor == 3:
        usunUcznia()
    if wybor == 4:
        ocenyUcznia()
    if wybor == 5:
        dodajOcene()
    if wybor == 6:
        najlepszyUczen()
    if wybor == 7:
        najgorszyUczen()
    if wybor == 8:
        najwyzszaSrednia()
    if wybor == 0:
        tak = False
 #   pauza = input('')
    time.sleep(5)
