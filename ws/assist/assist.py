from tkinter import *
from tkinter import ttk
import os

class FeetToMeters:

    # Sample set python 
    def set_python_env(self):
        pydir=os.getcwd()+"\\bin"
        pyscript=pydir+"\\Scripts"
        os.environ['PATH'] += ";" + pyscript

    def __init__(self, root):

        root.title("My Python")

        mainframe = ttk.Frame(root, padding="24 24 24 24")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        ttk.Button(mainframe, text="VC Env", command=self.launchvcenv).grid(column=0, row=0, sticky=W)
        ttk.Button(mainframe, text="Python Env", command=self.launchpyenv).grid(column=1, row=0, sticky=W)
        ttk.Button(mainframe, text="Code Python", command=self.launchcode).grid(column=2, row=0, sticky=W)
        ttk.Button(mainframe, text="Python WS", command=self.explorerws).grid(column=3, row=0, sticky=W)

        ttk.Button(mainframe, text="Thonny", command=self.launchthonny).grid(column=0, row=1, sticky=W)
        ttk.Button(mainframe, text="spyder", command=self.launchspyder).grid(column=1, row=1, sticky=W)
        ttk.Button(mainframe, text="jupyter", command=self.launchjupyter).grid(column=2, row=1, sticky=W)
        ttk.Button(mainframe, text="pydoc", command=self.launchpydoc).grid(column=3, row=1, sticky=W)

        for child in mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)
        
    def launchvcenv(self, *args):
        os.system('start %s\\script\\vsenv.bat' % os.getcwd())

    def launchpyenv(self, *args):
        os.system('start %s\\script\\pyenv.bat' % os.getcwd())

    def launchcode(self, *args):
        os.system('code %s\\home' % os.getcwd())

    def explorerws(self, *args):
        os.system('explorer %s' % os.getcwd())

    # Python Tools
    def launchthonny(self, *args):
        exe = '%s\\bin\Scripts\\thonny.exe' % os.getcwd()
        os.system('start ' + exe)

    def launchspyder(self, *args):
        exe = '%s\\bin\Scripts\\spyder.exe' % os.getcwd()
        os.system('start ' + exe)

    def launchjupyter(self, *args):
        exe = '%s\\bin\Scripts\\jupyter-lab.exe' % os.getcwd()
        os.system('start ' + exe)

    def launchpydoc(self, *args):
        exe = '%s\\bin\python -m pydoc -b' % os.getcwd()
        os.system('start ' + exe)

def Main():
    root = Tk()
    FeetToMeters(root)
    root.mainloop()


if __name__ == '__main__':
    Main()