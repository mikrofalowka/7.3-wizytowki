import logging
logging.basicConfig(level=logging.DEBUG, format="%(message)s")
from faker import Faker
fake = Faker()
import sys


class Wizytowka:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def __str__(self):
        return f'Imie: {self.imie} \nNazwisko: {self.nazwisko}'
    
    def __repr__(self):
        return f'Wizytowka(imie={self.imie} Nazwisko={self.nazwisko} )'
    
    def contact(self):
        return f'Kontaktuje sie z {self.imie.title()} {self.nazwisko.title()} '
    
    def create_contact_with_faker(type, quantity):
        kontakty = []
        logging.info(f'Generuje kontakt z uzyciem faker')
        wizytowka_type = (input("wpisz 'P'aby wygenerowac prywatne wizytowki lub wpisz 'B' aby wygenerowac biznesowe wizytowki \n Wpisz 'q' aby zakonczyc dzialanie programu: ")).upper().strip()
        quantity = int(input("Ile wizytowek wygenerowac? "))

        if wizytowka_type == "B":
            print(f'Generuje {quantity} wizytowek biznesowych')
            for i in range(quantity):
                kontakty.append(f'{BusinessContact(imie=fake.first_name(),nazwisko=fake.last_name(), nazwa_firmy=fake.company(), stanowisko=fake.job(), sluzbowy_nr_telefonu=fake.phone_number())}')

        elif wizytowka_type == "P":
            print(f'Generuje {quantity} wizytowek osobistych')
            for i in range(quantity):
                kontakty.append(f'{BaseContact(imie=fake.first_name(),nazwisko=fake.last_name(), nr_telefonu=fake.phone_number(), adres_e_mail=fake.email())}')
                return BaseContact(imie=fake.first_name(),nazwisko=fake.last_name(), nr_telefonu=fake.phone_number(), adres_e_mail=fake.email())
        elif wizytowka_type == "Q":
            sys.exit()
    
    @property
    def label_lenght(self):
        return len(self.imie) + len(self.nazwisko) + 1 #+1 jest spacja pomiedzy

class BaseContact(Wizytowka):
    def __init__(self, nr_telefonu, adres_e_mail, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.nr_telefonu = nr_telefonu
        self.adres_e_mail = adres_e_mail
    
    def make_contact(self):
        return f'Dzwonie do {self.imie} {self.nazwisko} na prywatny nr telefonu {self.nr_telefonu}'

    @property
    def lenght(self):
        return len(self.imie) + len(self.nazwisko)

class BusinessContact(Wizytowka):
    def __init__(self, nazwa_firmy,stanowisko, sluzbowy_nr_telefonu, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.nazwa_firmy = nazwa_firmy
        self.stanowisko = stanowisko
        self.sluzbowy_nr_telefonu = sluzbowy_nr_telefonu

    def make_contact(self):
        return f'Dzwonie do {self.imie} {self.nazwisko} z firmy {self.nazwa_firmy} na służbowy numer {self.sluzbowy_nr_telefonu}'
    
    @property
    def lenght(self):
        return len(self.imie) + len(self.nazwisko) + 1
    
    def create_business_contact(self, contact_type, quantity):
        self.contact_type = contact_type
        self.quantity = quantity


