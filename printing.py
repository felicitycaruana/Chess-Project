# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 14:36:53 2023

@author: Felicity Caruana
"""

def print_board(board):
    print("  ", end= "")
    for i in range(len(board)):
        print(i+1, end = " ")
    print()
    for i in range(len(board)):
        print(i+1, end = " ")
        for j in range(len(board[i])):
            print(board[i][j], end = " ")
        print()