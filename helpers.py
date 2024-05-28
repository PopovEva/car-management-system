import os
import json
from car import Car 
from rich import print 

def clear_screen(): #не использую в этой программе.
    if os.name == 'nt': os.system('cls')
    else: os.system('clear')
    
def print_cars(cars):
    for index, car in enumerate(cars):
        print(f"[green]{index}, {car}[/green]")    
    
def add_car(cars):
    cars.append(Car(input("Car Type?  "), input("Car Model?  "), input(" Color?  "),input("Client name?")))
    
def get_index(cars):
    print_cars(cars)
    choice=int(input("Choose car's number: "))
    return choice
    
def delete_car(cars):
    choice= get_index(cars)
    print(f'[red]The car: {cars[choice]} is deleted[/]')
    cars.pop(choice)

def update_car(cars):
    choice= get_index(cars)
    cars[choice]=Car(input("Car Type?  "), input("Car Model?  "), input(" Color?  "),input("Client name?"))
    print(f'[bold magenta]The car: {cars[choice]} is updated successfully[/]')

def info(cars):
    print(f'[bold magenta]Total cars in the garage: {len(cars)}[/] ')
        
def clear_data(cars):
    cars.clear()
    print("[red]All car data has been successfully cleared.[/]")        
         
def save_cars_to_file(cars):
    with open('cars.json', 'w', encoding='utf-8') as file:
        json.dump([car.to_dict() for car in cars], file, ensure_ascii=False, indent=4)
        
def load_cars_from_file():
    try:
        with open('cars.json', 'r', encoding='utf-8') as file:
            cars_data = json.load(file)
            return [Car.from_dict(car) for car in cars_data]
    except FileNotFoundError:
        print("File 'cars.json' not found. Created a new list of cars.")
        return []    
    
      