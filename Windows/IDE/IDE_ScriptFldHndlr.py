import tkinter
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess
import os

from IDE_consoleLogic import scriptOutput
from Network_client import Client


    

class ScriptFieldHndlr:
    def __init__(self, window, devicesList, scriptField, commandLine, fileTree):
        self.window = window
        self.devicesList = devicesList
        self.scriptField =  scriptField
        self.commandLine = commandLine
        self.fileTree = fileTree
        self.file_path=''
        self.file_saved = False
        self.client = Client()

    def __del__(self):
        self.conn.close() 

    def set_file_path(self, path):
        self.file_path = path


    def new_file(self):
        self.fileTree.clear_tree()
        self.set_file_path('')
        self.scriptField.delete('1.0', 'end')
        self.window.title("TMC IDE by Anas Fares")
        self.file_saved = False

    def open_file(self):
        path = askopenfilename(filetypes=[('Python Files', '*.py')])
        if path!='' and isinstance(path, tuple) != True:
            self.window.title(path.split('/')[-1]+" - TMC IDE by Anas Fares")
            self.fileTree.open_project(path)
            self.file_saved = False
            with open(path, 'r') as file:
                code = file.read()
                self.scriptField.delete('1.0', 'end')
                self.scriptField.insert('1.0', code)
                self.set_file_path(path)


    def save(self):
        if self.file_path == '':
            path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
        else:
            path = self.file_path
        if path!='' and isinstance(path, tuple) != True:
            self.fileTree.open_project(path)
            self.file_saved = True
            with open(path, 'w+') as file:
                code = self.scriptField.get('1.0', 'end')
                file.write(code)
                self.set_file_path(path)

    def save_as(self):
        path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
        if path!='' and isinstance(path, tuple) != True:
            self.fileTree.open_project(path)
            self.file_saved = True
            with open(path, 'w') as file:
                code = self.scriptField.get('1.0', 'end')
                file.write(code)
                self.set_file_path(path)


    def run(self):
        self.save()
        if self.file_saved == True:
            self.closeConn()
            command = f'py -3 "{self.file_path}"'
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            output, error = process.communicate()
            self.commandLine.insert("insert", '"run '+self.file_path.split('/')[-1]+'"')
            scriptOutput(self.commandLine, output, error)
            self.file_saved = False
            self.connectHndlr()

    
    def connectHndlr(self):
        self.conn = self.client.connectTMC()
        self.devicesList.config(text = "                  ")
        self.devicesList.menu.delete( 0 , 'end') 

    def closeConn(self):
        self.conn.close()

    def populateDevLst(self, coordinates): # parameter coordinates is an assumed output to the bind function and not actually known
        #delete children first    
        self.devicesList.menu.delete( 0 , 'end')  
        try:
            devsStr =  self.client.sendMsg(self.conn, 'lstmc')
            devsLst = devsStr[1:-1].replace("'", "").replace(", ", "").split('\\n')              
            for dev in devsLst:
                if dev != '':
                    self.devicesList.menu.add_command(label = dev, background='white')
                
        except:
            self.devicesList.menu.add_command(label = "                   Connect               ", background='white', command=self.connectHndlr)




        


        
