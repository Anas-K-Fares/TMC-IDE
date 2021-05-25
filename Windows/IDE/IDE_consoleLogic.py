import tkinter as tk
from tkinter import scrolledtext
import subprocess
import os


def createShellFile(command): #, bRemoveLastCall  ## bug when previous command resulted in error
    with open('./IDE_consoleIO.py', 'r') as f:
        lines = f.readlines()

    with open('./IDE_consoleIO.py', 'w') as f:
        # remove any lines that contain a print
        for line in lines:
            if 'print(' not in line:
                f.write(line)
 
        # add print to the final commandLine expression if not already present
        if 'print(' in command:
            f.write(command+'\n')
        elif '=' in command:
            f.write(command+'\n')
            f.write('print('+command.split('=')[0]+')'+'\n')
        else:
            f.write('print('+command+')'+'\n')
        

def onKeyPress(event):
    
    value = event.char
    linesNum = int(event.widget.index('end-1c').split('.')[0])
    charLoc = int(event.widget.index(tk.INSERT).split('.')[1])
    cursorLoc = event.widget.index(tk.INSERT)

    if cursorLoc.split('.')[0]!=str(linesNum) or charLoc<=3:
        event.widget.yview('end')
        event.widget.mark_set("insert", "end-1c")    
    event.widget.insert("insert", value)
    
    #status.configure(text=cursorLoc)

    return "break"

def backspaceHandler(event):
    linesNum = int(event.widget.index('end-1c').split('.')[0])
    charLoc = int(event.widget.index(tk.INSERT).split('.')[1])
    cursorLoc = event.widget.index(tk.INSERT)

    try:
        firstSel=event.widget.index('sel.first')
        firstSelInt=int(firstSel.split('.')[1])
        lastSel=event.widget.index('sel.last')
        lastSelInt=int(lastSel.split('.')[1])
    except:
        firstSel=''
        lastSel=''

    if cursorLoc.split('.')[0]==str(linesNum):
        if firstSel!='' and lastSel!='' and firstSelInt>3 and lastSelInt>3:
            
            #endSelection=str(abs(charLoc-len(event.widget.selection_get())))

            #event.widget.insert("insert", firstSel+' '+lastSel)
            event.widget.delete( firstSel, lastSel)
        elif firstSel=='' and lastSel=='' and charLoc>4:
            event.widget.delete(cursorLoc+'-1c')
        # return "break" so that the default behavior doesn't happen
    return "break"

def enterHandler(event):
    linesNum = int(event.widget.index('end-1c').split('.')[0])
    value = event.widget.get(str(linesNum)+".0",'end-1c')
    #status.configure(text=value)
    
    event.widget.mark_set("insert", "end-1c")
    command = event.widget.get( str(linesNum) + ".4",'end-1c')
    
    createShellFile(command)
    
    #exec(command)
    path = os.path.dirname(os.path.realpath(__file__))
    process = subprocess.Popen("py -3 IDE_consoleIO.py", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()

    if output.decode('ascii') != '': 
        event.widget.insert("insert", '\n\n'+output.decode('ascii'))
    if error.decode('ascii') != '': 
        event.widget.insert("insert", '\n\n'+error.decode('ascii'))
    event.widget.insert("insert", '\n>>> ')
    event.widget.yview('end')
    return "break"


def scriptOutput(widget, output, error):
    if output.decode('ascii') != '': 
        widget.insert("insert", '\n\n'+output.decode('ascii'))
    if error.decode('ascii') != '': 
        widget.insert("insert", '\n\n'+error.decode('ascii'))
    widget.insert("insert", '\n>>> ')
    widget.yview('end')
