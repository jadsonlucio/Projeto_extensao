
from .engine import filedialog
from .engine import messagebox

def show_info(titulo,mensagem,parent=None):
    messagebox.showinfo(titulo,mensagem,parent=parent)

def show_warning(titulo,mensagem):
    messagebox.showwarning(titulo,mensagem)

def show_error(titulo,mensagem):
    messagebox.showerror(titulo,mensagem)

def askyesno(titulo,mensagem):
    valor=messagebox.askyesno(titulo,mensagem)
    return valor

def openfiles(parent=None,title="Abrir arquivo",filetypes=()):
    try:
        files_choice = filedialog.askopenfilenames(parent=parent,title=title,filetypes=filetypes)
        return files_choice
    except Exception as e:
        print(str(e))

def openfile(parent=None,title="Abrir arquivo",filetypes=()):
    try:
        file_choice = filedialog.askopenfilename(parent=parent,title=title,filetypes=filetypes)
        return file_choice
    except Exception as e:
        print(str(e))

def opendirectory():
    try:
        url_directory = filedialog.askdirectory()
        return url_directory
    except Exception as e:
        print(str(e))

def save_file(parent=None,title="Salvar arquivo",defaultextension=".txt"):
    url=filedialog.asksaveasfilename(parent=parent,title=title,defaultextension=defaultextension)
    return url
