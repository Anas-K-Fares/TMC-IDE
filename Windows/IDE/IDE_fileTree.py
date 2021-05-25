# source: https://stackoverflow.com/questions/16746387/display-directory-content-with-tkinter-treeview-widget
import os#, gi
import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk

class FileTree(object):
    def __init__(self, master):
        self.nodes = dict()
        frame = tk.Frame(master)
        self.tree = ttk.Treeview(frame)
        #ysb = ttk.Scrollbar(frame, orient='vertical', command=self.tree.yview)
        #xsb = ttk.Scrollbar(frame, orient='horizontal', command=self.tree.xview)
        #self.tree.configure(yscroll=ysb.set)
        self.tree.heading('#0', text='Project Tree', anchor='w')
 
        self.tree.pack(fill="both", expand=True)
        #ysb.pack(fill="both", expand=True)
        #xsb.grid(row=1, column=0, sticky='ew')
        frame.pack(fill="both", expand=True)

    def clear_tree(self):
         ## clear previous project tree
        for node in self.tree.get_children():
            self.tree.delete(node)
        self.nodes = dict()
        self.tree.icons =[]

    def open_project(self, path):
        ## clear previous project tree
        self.clear_tree()
        
        ## saturate tree with files
        abspath = os.path.dirname(path)

        self.nodeIcon= Image.open(self.get_thumbnail(abspath))
        self.nodeIcon= ImageTk.PhotoImage(self.nodeIcon)
        self.tree.icons =[]
        self.tree.icons.append(self.nodeIcon)
        
        self.insert_node('', abspath, abspath)
        self.tree.bind('<<TreeviewOpen>>', self.open_node)


    def insert_node(self, parent, text, abspath):
        node = self.tree.insert(parent, 'end', text=text, image=self.tree.icons[-1], open=False)
        if os.path.isdir(abspath):
            self.nodes[node] = abspath
            self.tree.insert(node, 'end')

    def open_node(self, event):
        node = self.tree.focus()
        abspath = self.nodes.pop(node, None)
        if abspath:
            self.tree.delete(self.tree.get_children(node))
            for p in os.listdir(abspath):
                self.nodeIcon= Image.open(self.get_thumbnail(os.path.join(abspath, p)))
                self.nodeIcon= ImageTk.PhotoImage(self.nodeIcon)
                self.tree.icons.append(self.nodeIcon)
                self.insert_node(node, p, os.path.join(abspath, p))


    def get_thumbnail(self, filename):
        if os.path.isdir(filename):
            iconName= './icons/folder.png'
        else:
            extensionIndex = filename.rfind('.')
            extension = filename[extensionIndex:]
            extension = extension.lower()
            
            if extension == '.png' or extension =='.jpg' or extension =='.jpeg' or extension =='.gif' or extension =='.tiff':
                iconName= './icons/image-x-generic.png'
            elif extension == '.pdf':
                iconName= './icons/application-pdf.png'
            elif extension == '.csv' or extension =='.xls' or extension =='xlsx':
                iconName= './icons/spreadsheet.png'
            elif extension == '.txt':
                iconName= './icons/text-x-generic.png'
            elif extension == '.py':
                iconName= './icons/text-x-python.png'
            elif extension == '.exe':
                iconName= './icons/application-x-executable.png'
            elif extension == '.mp4' or extension =='.mkv' or extension =='.mov' or extension =='.wmv' or extension =='.avi' or extension =='.mpeg-2' or extension =='.flv' or extension =='.swf' or extension =='.f4v':
                iconName= './icons/video-x-generic.png'
            elif extension == extension =='.mp3' or extension =='.wav' or extension =='.aac' or extension =='.flac':
                iconName= './icons/audio-x-generic.png'
            else:
                iconName= './icons/empty.png'        
        return iconName


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root, path='/home/anas/Desktop')
    root.mainloop()




