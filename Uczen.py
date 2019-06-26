import subprocess
import datetime
import time

uczeniowie=[{'Robert Mak', '1B'}, {'Ryszard Nowak', '2C'}, {'Anna Mak', '3A'}, {'Monika Zdun', '1B'}]
oceny=[]
nauczyciele=['Maria Konopka', 'Janusz Miłosz', 'Anna Nosowska', 'Henryk Kozłowski', 'Monika Zatorska']
przedmioty=['matematyka', 'j.polski', 'geografia', 'biologia', 'fizyka']

def dodajUcznia():
    koniec=False
    while koniec==False:
        imieNazwisko = str(input('Podaj imie i nazwisko ucznia: '))
        klasa = str(input('Klasa ucznia (1B,2A...3C): '))
        uczen={'imieNazwisko': imieNazwisko, 'klasa': klasa}
        uczeniowie.append(uczen)
        takNie=str(input('Chcesz dodać kolejnrgo ucznia? Y/N: '))
        if takNie=='Y' or takNie=='y':
            koniec=False
        else:
            koniec=True
    print(uczeniowie)

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
    pauza = input('')
 #   time.sleep(5)
