import datetime
import os.path

def save_transaction(file_path, amount):
    with open(file_path, "a") as f:
        f.write(f'{float(amount):.2f}, {datetime.datetime.now()}\n')
            
def save_balance(file_path, amount):
    with open(file_path, "w") as b:
        b.write(f'{float(amount):.2f}')
            
def read_first_line(file_path):
    with open(file_path, "r") as f:
        line = f.readline()
        return line

def check_path(file_path):
    return os.path.isfile(file_path)

def create_file(file_path):
    if not check_path(file_path):
        data = open(file_path, "w")
        data.close()
        

        