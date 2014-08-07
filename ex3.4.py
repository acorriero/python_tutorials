#!/usr/bin/env python3

def do_twice(f, word):
    f(word)
    f(word)

def do_four(f, word):
    do_twice(f, word)
    do_twice(f, word)

def print_twice(word):
    print(word)
    print(word)

do_four(print_twice, 'spam')
