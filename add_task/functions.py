from .models import *


def filling_db_with_defects_parts_employees():
    """
    A function that populates the database with random records for parts, employees, and defects.
    """
    Parts.objects.create(description="Koło przednie", average_price=50)
    Parts.objects.create(description="Opona", average_price=30)
    Parts.objects.create(description="Przerzutka tylna", average_price=70)
    Parts.objects.create(description="Kierownica", average_price=40)
    Parts.objects.create(description="Siodełko", average_price=25)
    Parts.objects.create(description="Hamulce", average_price=60)
    Parts.objects.create(description="Pedały", average_price=15)
    Parts.objects.create(description="Łańcuch", average_price=35)
    Parts.objects.create(description="Kaseta", average_price=55)
    Parts.objects.create(description="Widelec", average_price=80)
    Parts.objects.create(description="Rama", average_price=100)
    Parts.objects.create(description="Koło tylne", average_price=45)
    Parts.objects.create(description="Suport", average_price=30)
    Parts.objects.create(description="Manetki", average_price=50)
    Parts.objects.create(description="Łańcuch napędowy", average_price=65)

    Employees.objects.create(name="Adam", surname="Kowalski")
    Employees.objects.create(name="Anna", surname="Nowak")
    Employees.objects.create(name="Piotr", surname="Wójcik")
    Employees.objects.create(name="Magda", surname="Jankowska")
    Employees.objects.create(name="Tomasz", surname="Wojciechowski")

    Defects.objects.create(description="Przerzutka nie działa poprawnie", average_price=80)
    Defects.objects.create(description="Hamulec przecieka", average_price=45)
    Defects.objects.create(description="Koło przednie zagięte", average_price=60)
    Defects.objects.create(description="Rower drży podczas jazdy", average_price=55)
    Defects.objects.create(description="Problem z przerzutkami przednimi", average_price=70)
    Defects.objects.create(description="Wyciek oleju w hamulcach", average_price=40)
    Defects.objects.create(description="Problem z pedałami", average_price=30)
    Defects.objects.create(description="Uszkodzony mostek kierownicy", average_price=50)
    Defects.objects.create(description="Złamana rama roweru", average_price=120)
    Defects.objects.create(description="Dźwignia hamulca zniszczona", average_price=25)
    Defects.objects.create(description="Przerzutka tylna nie przechodzi na większe przełożenie", average_price=90)
    Defects.objects.create(description="Problem z suportem", average_price=65)
    Defects.objects.create(description="Koło tylne traci równowagę", average_price=70)
    Defects.objects.create(description="Awaria oświetlenia", average_price=35)
    Defects.objects.create(description="Uszkodzona siodełka", average_price=30)

