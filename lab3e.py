#!/usr/bin/env python3
'''Lab 3 Part 2 – list indexing helpers'''
# Author ID: eroshy   # <-- replace with your Seneca ID if needed

# Create the list called "my_list" here, not inside any function.
my_list = [100, 200, 300, 'six hundred']

def give_list():
    # Returns all of the items in the global object my_list unchanged
    return my_list

def give_first_item():
    # Returns the first item in the global object my_list as a string
    return str(my_list[0])

def give_first_and_last_item():
    # Returns a list with the first and last items of my_list
    return [my_list[0], my_list[-1]]

def give_second_and_third_item():
    # Returns a list with the second and third items of my_list
    return my_list[1:3]

if __name__ == '__main__':   # Main block
    print(give_list())
    print(give_first_item())
    print(give_first_and_last_item())
    print(give_second_and_third_item())
