#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 15:23:01 2017

Designed to be used with MicroPython
https://micropython.org

This is just a random collection of modules that are applications of the concepts taught in my Discrete Math Class.

@author: danielsalazar
"""

def binToDec():
    num = input("Enter a binary number: ")
    print(int(num, 2))
    convert()

def binToHex():
    num = input("Enter a binary number: ")
    print(hex(int(num, 2)))
    convert()

def dectoBin():
    num = int(input("Enter a decimal number: "))
    print(bin(num))
    convert()  
    
def dectoHex():
    num = int(input("Enter a decimal number: "))
    print(hex(num))
    convert() 
    
def hexToDec():
    num = int(input("Enter a hexidecimal number: "), 16)
    print(num)
    convert()

def hexToBin():
    num = int(input("Enter a hexidecimal number: "), 16)
    print(bin(num))
    convert()

def convert():
    print("Convert Menu\n\n")
    print("1) Bin to Dec")
    print("2) Bin to Hex")
    print("3) Dec to Bin")
    print("4) Dec to Hex")
    print("5) Hex to Dec")
    print("6) Hex to Bin")
    print("7) return")
    choice = int(input("Make a selection: "))
    if choice == 1:
        binToDec()
    elif choice == 2:
        binToHex()
    elif choice == 3:
        dectoBin()
    elif choice == 4:
        dectoHex()
    elif choice == 5:
        hexToDec()
    elif choice == 6:
        hexToBin()
    elif choice == 7:
        main()

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
    
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
    
def inverse():
    m = int(input("Enter mod number: "))
    l = []
    for a in range(1, m):
        l.append(modinv(a, m))
    print(l)
    main()
    
def is_prime(n):
    if n < 2: 
         return False;
    if n % 2 == 0:             
         return n == 2  # return False
    k = 3
    while k*k <= n:
         if n % k == 0:
             return False
         k += 2
    return True

def is_square(n):
    return int(n**0.5)**2 == n

def prime4K():
    mi = int(input("Enter min: "))
    ma = int(input("Enter max: "))
    l = []
    for x in range(0, 1000):
        a = 4 * x + 1
        if a > mi and is_prime(a):
            l.append(a)
        if (4 * (x+1) + 1) > ma:
            break
    done = False
    while not done:
        print("\n", l)
        num = int(input("Pick a number to factor, 0 to exit: "))
        if num == 0:
            main()
        else:
            ans = []
            if is_square(num):
                ans.append(num**0.5)
                ans.append(num**0.5)
                print(ans)
            else:
                for i in range(0,int(num**0.5 + 1)):
                    b = (num - i**2)
                    for j in range(i,int(b**0.5 + 1)):
                        if (i**2 + j**2) == num:
                            ans.append(i)
                            ans.append(j)
                            print(ans)   
                            
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

def nCk():
    n = int(input("Enter n: "))
    k = int(input("Enter k: "))
    print(fact(n) / (fact(k) * fact(n - k)))
    main()
    

def nPk():
    a = input("Enter string: ")
    
    d = {}
    for item in a:
        if item in d:
            d[item] = d.get(item)+1
        else:
            d[item] = 1
            
    l = []
    for k,v in d.items():
        l.append(int(v))
    n = sum(l)
    ret = fact(n)
    for i in l:
        ret //= fact(i)
    km = n - sum(l)
    print(ret//fact(km))
    main()
    
def mult_nCr():
    n = int(input("Enter last n: "))
    k = int(input("Enter last k: "))
    for x in range(0, k + 1):
        print(fact(n) / (fact(x) * fact(n - x)))
    main()
   
def fib(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return fib(n-1) + fib(n-2)
    
    
def printFib():
    n = int(input("Enter number of places: "))
    l = []
    for x in range(0, n + 1): 
        l.append(fib(x))
    print(l)
    series()
    
def fibMult():
    n = int(input("Enter number of places: "))
    k = int(input("Enter number for multiples of: "))
    l = []
    for x in range(0, n + 1): 
        tmp = fib(x)
        if(tmp % k == 0):
            l.append(tmp)
    print(l)
    series()
   
def printFact():
    n = int(input("Enter number of places: "))
    l = []
    for x in range(0, n + 1): 
        l.append(fact(x))
    print(l)
    series()
        
def pascals_triangle(n_rows):
    results = []
    for _ in range(n_rows): 
        row = [1]
        if results:
            last_row = results[-1]
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row.append(1)
        results.append(row)
    return results

def printTri():
    n = int(input("Enter number of places: "))
    t = pascals_triangle(n + 1)
    for i in t:
        print(i)
    series()
    
def p(s):
    powerset = set()
    for i in range(2**len(s)):
        subset = tuple([x for j,x in enumerate(s) if (i >> j) & 1])
        powerset.add(subset)
    return powerset
    
def powerSet():
    pSet = input("Enter the set: ")
    print(p(pSet))
    series()

def series():
    print("\nSeries Menu\n\n")
    print("1) Fib")
    print("2) Fib Multiples")
    print("3) Fact")
    print("4) Pascal's Triangle")
    print("5) Power Set")
    print("anything else to return")
    choice = int(input("Make a selection: "))
    if choice == 1:
        printFib()
    elif choice == 2:
        fibMult()
    elif choice == 3:
        printFact()
    elif choice == 4:
        printTri()
    elif choice == 5:
        powerSet()
    else:
        main()
   
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
     
     
def isOperator(x):
    if x == "not" or x == "and" or x == "or" or x == "xor" or x == "imp" or x == "dimp":
        return True
    else:
        return False

def convertLogic(eq):
    stack = Stack()
    s = eq.split()
    stack.push("(")
    s.append(")")
    postfix = []
    for x in s:
        if x == "p" or x == "q":
            postfix.append(x)
        elif x == "(":
            stack.push("(")
        elif isOperator(x):
            
            while isOperator(stack.peek()):
                postfix.append(stack.pop())
            stack.push(x)
        elif x == ")":
                while stack.peek() != "(":
                    postfix.append(stack.pop())
                stack.pop()
    return postfix

def bit_not(n, numbits):
    a = int(n, 2)
    return (1 << numbits) - 1 - a

def calcLogic(u, v1, v2, op):
    a = int(v1, 2)
    b = int(v2, 2)
    if op == "and":
        return bin(a & b)
    elif op == "or":
        return bin(a | b)
    elif op == "imp":
        return bin((bit_not(v1, len(u))) | b)
    elif op == "xor":
        return bin(a ^ b)
    else:
        x = str(bin(a ^ b))
        return bin(bit_not(x, len(u)))
        


def evalLogic(eq, u, p, q):
    stack = Stack()
    v1 = 0
    v2 = 0
    for x in eq:
        if x == "p":
            stack.push(p)
        elif x == "q":
            stack.push(q)
        elif x == "not":
            a = stack.pop()
            stack.push(str(bin(bit_not(a, len(u)))))
        else:
            v2 = stack.pop()
            v1 = stack.pop()
            stack.push(str(calcLogic(u, v1, v2, x)))
    return stack.pop()

def logic():
    u = input("Enter U: ")
    a = input("Enter A: ")
    b = input("Enter B: ")
    done = False
    while not done:
        eq = input("Enter equation (use space to sep every object): ")
        print(evalLogic(convertLogic(eq), u, a, b))
        choice = int(input("Press 0 to stop, anything else to continue: "))
        if choice == 0:
            main()
 

def convertSet(eq):
    stack = Stack()
    s = eq.split()
    stack.push("(")
    s.append(")")
    postfix = []
    for x in s:
        if x == "r" or x == "s" or x == "t":
            postfix.append(x)
        elif x == "(":
            stack.push("(")
        elif isOperator(x):            
            while isOperator(stack.peek()):
                postfix.append(stack.pop())
            stack.push(x)
        elif x == ")":
                while stack.peek() != "(":
                    postfix.append(stack.pop())
                stack.pop()
    return postfix

def evalSet(eq, u, r, s, t):
    stack = Stack()
    v1 = 0
    v2 = 0
    for x in eq:
        if x == "r":
            stack.push(r)
        elif x == "s":
            stack.push(s)
        elif x == "t":
            stack.push(t)
        elif x == "not":
            a = stack.pop()
            stack.push(u - a)
        else:
            v2 = stack.pop()
            v1 = stack.pop()
            if x == "and":
                stack.push(v1 & v2)
            else:
                stack.push(v1 | v2)
    if not stack.isEmpty():
        return stack.pop()
    else:
        return []
    

def Sets(): 
    u = set(input("Enter universe: "))
    r = set(input("Enter R set: "))
    s = set(input("Enter S set: "))
    t = set(input("Enter T set: "))
    done = False
    while not done:
        eq = input("Enter eq (put () around not vars): ")
        print(evalSet(convertSet(eq), u, r, s, t))
        choice = int(input("Press 0 to stop, anything else to continue: "))
        if choice == 0:
            done = True
    main()

def infixToPrefix():
    prec = {'/':3,'*':3,'+':2,'-':2,'^':4,'(':1}
    opStack = Stack()
    prefixList = []
    temp = []
    s = input("Enter infix equation (no spaces): ")
    for token in s:
        if token in "abcdefghijklmnopqrstuvwxyz" or token in "0123456789":
            prefixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                temp.append(topToken)
                topToken = opStack.pop()
            prefixList = temp + prefixList
            temp = []
        else:
            while (not opStack.isEmpty()) and \
                (prec[opStack.peek()]>= prec[token]):
                temp.append(opStack.pop())
            prefixList = temp + prefixList
            temp = []
            opStack.push(token)
    while not opStack.isEmpty():
        temp.append(opStack.pop())
    prefixList = temp + prefixList
    print(''.join(prefixList))
    main()

def evalPrefix(operator, value_one, value_two):
    if operator == "+":
        return value_one + value_two
    elif operator == "-":
        return value_one - value_two
    elif operator == "*":
        return value_one * value_two
    elif operator == "/":
        return value_one / value_two
    elif operator == "^":
        return value_one ** value_two
    else:
        print("Bad Format\n")
    main()

def prefix():
    equation = input("Enter prefix equation (use spaces): ")
    tokens = equation.split(" ")
    eval_stack = [ ]
    total = None
    for token in tokens:
        if token.isdigit():
            token = int(token)
            if total is None:
                total = token
            else:
                total = evalPrefix(eval_stack.pop(0), total, token)
        else:
            eval_stack.insert(0, token)
    print(total)
    main()
    
def main():
    print("\nMain Menu\n\n")
    print("1) Convert numbers")
    print("2) Mult inverse")
    print("3) 4K+1")
    print("4) nCk")
    print("5) nPk")
    print("6) multiplcitive nCr")
    print("7) Series expansion")
    print("8) Logic")
    print("9) Sets")
    print("10) Infix to Prefix")
    print("11) Eval Prefix")
    print("anything else to exit")
    choice = int(input("Make a selection: "))
    if choice == 1:
        convert()
    elif choice == 2:
        inverse()
    elif choice == 3:
        prime4K()
    elif choice == 4:
        nCk()
    elif choice == 5:
        nPk()
    elif choice == 6:
        mult_nCr()
    elif choice == 7:
        series()
    elif choice == 8:
        logic()
    elif choice == 9:
        Sets()
    elif choice == 10:
        infixToPrefix()
    elif choice == 11:
        prefix()
    else:
        raise SystemExit
    
main();
