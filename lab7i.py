#!/usr/bin/env python3
# Student ID: Pirajeen Kandasamy

def function1():
    # Make this change the global object so main reflects "SICT" 
    global schoolName
    schoolName = 'SICT'
    print('print() in function1 on schoolName:', schoolName)

def function2():
    # Already intended to modify the global
    global schoolName
    schoolName = 'SSDO'
    print('print() in function2 on schoolName:', schoolName)

schoolName = 'Seneca'
print('print() in main on schoolName:', schoolName)
function1()
print('print() in main on schoolName:', schoolName)
function2()
print('print() in main on schoolName:', schoolName)
