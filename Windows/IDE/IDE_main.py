import tkinter as tk
import tkinter.ttk as ttk
from tkinter import Menu
from tkinter import scrolledtext
from PIL import Image, ImageTk

from IDE_consoleLogic import onKeyPress,backspaceHandler, enterHandler
import IDE_fileTree
import IDE_ScriptFldHndlr

# need to destroy connection before closing
def closeConnOnExit(SFH, window):
    SFH.closeConn()
    window.destroy()

window = tk.Tk()
window.title("TMC IDE by Anas Fares")

menu_bar = Menu(window)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='File', menu=file_menu)

run_bar = Menu(menu_bar, tearoff=0)

menu_bar.add_cascade(label='Run', menu=run_bar)

window.config(menu=menu_bar)


quickAccess = tk.Frame(width=1280, height=30, background="light gray")
quickAccess.pack(fill="x", expand=False)

newIM = ImageTk.PhotoImage(Image.open('./icons-ide/filenew.png'))
openIM =ImageTk.PhotoImage(Image.open('./icons-ide/fileopen.png'))
saveIM =ImageTk.PhotoImage(Image.open('./icons-ide/filesave.png'))
undoIM =ImageTk.PhotoImage(Image.open('./icons-ide/undo.png'))
redoIM =ImageTk.PhotoImage(Image.open('./icons-ide/redo.png'))
runIM =ImageTk.PhotoImage(Image.open('./icons-ide/run.png'))


newBtn = tk.Button(quickAccess, text="New File", image = newIM)
newBtn.pack(side = 'left', padx=(25,5), pady=5)
openBtn = tk.Button(quickAccess, text="Open File", image = openIM)
openBtn.pack(side = 'left', padx=5, pady=5)
saveBtn = tk.Button(quickAccess, text="Save File", image = saveIM)
saveBtn.pack(side = 'left', padx=5, pady=5)


devicesList = tk.Menubutton(quickAccess, text="Disconnected", width=25)
devicesList.config(background='white', activebackground='white')
devicesList.menu = Menu(devicesList, tearoff=0)

devicesList["menu"]= devicesList.menu  
devicesList.pack(side = 'left', padx=(200,5), pady=5)


runBtn = tk.Button(quickAccess, text="Run", image = runIM)
runBtn.pack(side = 'left', padx=10, pady=5)


redoBtn = tk.Button(quickAccess, text="Redo", image = redoIM)
redoBtn.pack(side = 'right', padx=(0, 25), pady=5)
undoBtn = tk.Button(quickAccess, text="Undo", image = undoIM)
undoBtn.pack(side = 'right', padx=5, pady=5)

# the main window is divided into left and right sections,
# and the sidebar is divided into a top and bottom section.
pw = ttk.PanedWindow(orient="horizontal")
body = ttk.PanedWindow(pw, orient="vertical")
sidebar = tk.Frame(pw, width=260, height=720, background="white")

scriptArea = tk.Frame(body, width=1020, height=500)
consoleArea = tk.Frame(body, width=1020, height=220)

# add the paned window to the root
pw.pack(fill="both", expand=True)

# add the sidebar and main area to the main paned window
pw.add(sidebar)
pw.add(body)


# add the top and bottom to the sidebar
body.add(scriptArea, weight=1)
body.add(consoleArea)

fileTree = IDE_fileTree.FileTree(sidebar) # , path='/home/anas/Desktop')

scriptField = scrolledtext.ScrolledText(scriptArea, height=20,  background="beige", wrap = tk.WORD)
scriptField.pack(fill="both", expand=True)


commandLine = scrolledtext.ScrolledText(consoleArea, height=10,  wrap = tk.WORD)
commandLine.pack(fill="both", expand=True)
commandLine.bind( "<BackSpace>", backspaceHandler)
commandLine.bind( "<Return>", enterHandler)
commandLine.bind( "<KP_Enter>", enterHandler)
commandLine.bind( "<KeyPress>", onKeyPress)
commandLine.insert("insert", '>>> ')

SFH = IDE_ScriptFldHndlr.ScriptFieldHndlr(window, devicesList, scriptField, commandLine, fileTree)
file_menu.add_command(label='New', command=SFH.new_file)
file_menu.add_command(label='Open', command=SFH.open_file)
file_menu.add_command(label='Save', command=SFH.save)
file_menu.add_command(label='Save As', command=SFH.save_as)
file_menu.add_command(label='Exit', command=exit)
run_bar.add_command(label='Run', command=SFH.run)

newBtn.config(command=SFH.new_file)
openBtn.config(command=SFH.open_file)
saveBtn.config(command=SFH.save)
#devicesList.menu.add_command(label = "   Connect        ", background='white', activebackground='white', command=SFH.connectHndlr)
devicesList.bind("<ButtonRelease-1>", SFH.populateDevLst)
runBtn.config(command=SFH.run)

# need to destroy connection before closing
window.protocol('WM_DELETE_WINDOW', lambda: closeConnOnExit(SFH, window))
window.mainloop()
