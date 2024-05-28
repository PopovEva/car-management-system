from rich import print 
from enum import Enum
from helpers import print_cars, add_car, delete_car, update_car, info, clear_data, save_cars_to_file, load_cars_from_file
from car import Car 

class Operations(Enum):
    PRINT = 1
    ADD = 2
    DELETE = 3
    UPDATE = 4
    EXIT = 5
    INFO = 6
    CLEAR = 7
    
def menu():
    for oper in Operations: print(f'{oper.value} - {oper.name}')   
    return Operations(int(input("Choose your action:")))

    
if __name__ == "__main__":  
    cars = load_cars_from_file()  
    while True:
        try:
            user_selection = menu()
            if user_selection== Operations.EXIT:
                save_cars_to_file(cars)
                exit()    
            if user_selection== Operations.ADD:
                add_car(cars)
                save_cars_to_file(cars)

            if user_selection== Operations.PRINT: print_cars(cars)
            if user_selection== Operations.DELETE:
                delete_car(cars)
                save_cars_to_file(cars)
            if user_selection== Operations.UPDATE:
                update_car(cars)
                save_cars_to_file(cars)
            if user_selection== Operations.INFO: info(cars)
            if user_selection == Operations.CLEAR: 
                clear_data(cars)
                save_cars_to_file(cars)
        except Exception as e:
            print("[red]Incorrect syntax, try again:[/] ")   
            print("[red]Choose a action number:[/] ")      