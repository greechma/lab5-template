#!/usr/bin/env python3
# Author ID:ggairhe

def add(number1, number2)
    try:
        num1 = float(number1)  
        num2 = float(number2) 
        return num1 + num2      
    except (ValueError, TypeError):  
        return 'error: could not add numbers'


def read_file(filename):
     try:
        with open(filename, 'r') as file:
            return file.readlines()  
    except (FileNotFoundError, IOError): 
        return 'error: could not read file'


if __name__ == '__main__':
    print(add(10, 5))                      
    print(add('10', 5))                      
    print(add('abc', 5))                     
    print(read_file('seneca2.txt'))         
    print(read_file('file10000.txt'))       
