import subprocess
import datetime
import time

uczeniowie = [{'imieNazwisko': 'Robert Mak', 'klasa': '1B'}, {'imieNazwisko': 'Ryszard Nowak', 'klasa': '2C'},
              {'imieNazwisko': 'Anna Mak', 'klasa': '3A'}, {'imieNazwisko': 'Monika Zdun', 'klasa': '1B'}]
oceny = []
nauczyciele = ['Maria Konopka', 'Janusz Miłosz', 'Zuzanna Nowak'
               'Anna Nosowska', 'Henryk Kozłowski', 'Monika Zatorska']
przedmioty = ['matematyka', 'j.polski', 'geografia', 'biologia', 'fizyka']


def wypiszListe(lista):
    print('-----------------------------------------------')
    for i in range(len(lista)):
        print(str(i+1)+' - '+str(lista[i]))
    if len(lista)==0:
        print('                 Brak danych')
    print('-----------------------------------------------')


def wypiszListy():
    print('-----------------------------------------------')
    print('                  UCZNIOWIE')
    wypiszListe(uczeniowie)
    print('-----------------------------------------------')
    print('                    OCENY')
    wypiszListe(oceny)
    print('-----------------------------------------------')
    print('                 NAUCZYCIELE')
    wypiszListe(nauczyciele)
    print('-----------------------------------------------')
    print('                 PRZEDMIOTY')
    wypiszListe(przedmioty)


def dodajUcznia():
    koniec = False
    while koniec == False:
        imieNazwisko = str(input('Podaj imie i nazwisko ucznia: '))
        klasa = str(input('Klasa ucznia (1B,2A...3C): '))
        uczen = {'imieNazwisko': imieNazwisko, 'klasa': klasa}
        uczeniowie.append(uczen)
        print('Dodano ucznia '+uczen['imieNazwisko']+' do klasy '+uczen['klasa'])
        takNie = str(input('Chcesz dodać kolejnego ucznia? Y/N: '))
        if takNie == 'Y' or takNie == 'y':
            koniec = False
        else:
            koniec = True
    wypiszListe(uczeniowie)


def modyfikujUcznia():
    print('-----------------------------------------------')
    print('                  UCZNIOWIE')
    wypiszListe(uczeniowie)
    nr=int(input('Podaj numer ucznia: '))
    if nr>=len(uczeniowie):
        print('Lista obejmuje '+str(len(uczeniowie))+' uczniów.')
        print('Sprubój jeszcze raz.')
    else:
        takNie=str(input('Czy chodzi o ucznia: '+uczeniowie[nr-1]['imieNazwisko']+' ('+uczeniowie[nr-1]['klasa']+')? Y/N: '))
        if takNie == 'Y' or takNie == 'y':
            imieNazwisko = str(input('Podaj imie i nazwisko ucznia: '))
            klasa = str(input('Klasa ucznia (1B,2A...3C): '))
            uczeniowie[nr-1]['imieNazwisko']= imieNazwisko
            uczeniowie[nr-1]['klasa']= klasa
    print('Zmodyfikowano ucznia nr '+str(nr)+') '+imieNazwisko+' ('+klasa+')')


def usunUcznia():
    print('-----------------------------------------------')
    print('                  UCZNIOWIE')
    wypiszListe(uczeniowie)
    imieNazwisko = str(input('Podaj imie i nazwisko ucznia do usunięcia: '))
    klasa = str(input('Podaj klasę ucznia (1B,2A...3C): '))
    uczenDoUsuniecia={'imieNazwisko': imieNazwisko, 'klasa': klasa}
    if uczenDoUsuniecia in uczeniowie:
        takNie=str(input('Czy chcesz usunąć ucznia: '+imieNazwisko+' ('+klasa+') z listy uczniów? Y/N: '))
        if takNie == 'Y' or takNie == 'y':
            uczeniowie.remove(uczenDoUsuniecia)
            print('Usunięto ucznia z listy.')
            print('-----------------------------------------------')
            print('                  UCZNIOWIE')
            wypiszListe(uczeniowie)
    else:
        print('Nie ma takiego ucznia na liście.')




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
    print('9 - Wszystkie listy')
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
    if wybor == 9:
        wypiszListy()
    if wybor == 0:
        tak = False
    pauza = input('')
 #   time.sleep(5)
