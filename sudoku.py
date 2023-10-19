import tkinter as tk
from tkinter import ttk

fen = tk.Tk()

def click(i,j):
    curr = boutons[i][j]["text"]
    if curr == ".": boutons[i][j]["text"] = "1"
    elif curr == "9": boutons[i][j]["text"] = "."
    else: boutons[i][j]["text"] = str(int(curr)+1)
    boutons[i][j]["fg"] = "black"
def right_click(event,i,j):
    curr = boutons[i][j]["text"]
    if curr == ".": boutons[i][j]["text"] = "9"
    elif curr == "1": boutons[i][j]["text"] = "."
    else: boutons[i][j]["text"] = str(int(curr)-1)
    boutons[i][j]["fg"] = "black"

def solve_click():
    board = [["."]*9 for _ in range(9)]
    def valid(n, i, j, b):
            if n == ".": return True
            for x in range(9):
                if b[i][x] == n or b[x][j] == n: return False
            for x in range(i//3*3, i//3*3+3):
                for y in range(j//3*3, j//3*3+3):
                    if b[x][y] == n: return False
            return True
    for i in range(9):
        for j in range(9):
            if not valid(boutons[i][j]["text"], i, j, board):
                return False
            board[i][j] = boutons[i][j]["text"]
    
    def solve(i,j):
        if j >= 9: return solve(i+1, 0)
        if i >= 9: return True
        if board[i][j] != ".": return solve(i, j+1)
        for x in range(1, 10):
            if valid(str(x), i, j, board):
                board[i][j] = str(x)
                if solve(i,j+1): return True
                else: board[i][j] = "."
    solve(0,0)
    for i in range(9):
        for j in range(9):
            if boutons[i][j]["text"] == ".":
                boutons[i][j]["text"] = board[i][j]
                boutons[i][j]["fg"] = "red"

def reset():
    for i in range(9):
        for j in range(9):
            boutons[i][j]["text"] = "."
            boutons[i][j]["fg"] = "black"

boutons = [[tk.Button(fen, text=".",padx=15, pady=10, command=lambda i=i,j=j:click(i,j)) for j in range(9)] for i in range(9)]
for i in range(9):
    for j in range(9):
        boutons[i][j].bind("<Button-3>", lambda event,i=i,j=j: right_click(event,i,j))
        boutons[i][j].grid(column=j+j//3, row=i+i//3)
ttk.Separator(fen, orient="horizontal").grid(row=3, column=0, columnspan=11, ipadx=200,pady=4)
ttk.Separator(fen, orient="horizontal").grid(row=7, column=0, columnspan=11, ipadx=200,pady=4)
ttk.Separator(fen, orient="vertical").grid(column=3, row=0, rowspan=11, ipady=200,padx=4)
ttk.Separator(fen, orient="vertical").grid(column=7, row=0, rowspan=11, ipady=200,padx=4)
tk.Button(fen, text="Solve", command=lambda : solve_click()).grid(row=11, column=5)
tk.Button(fen, text="Reset", command=lambda : reset()).grid(row=11, column=10)
fen.mainloop()