import tkinter as tk
from ...engine import ttk

from ....constantes import CAMINHO_ICONS_FRAME_TABELA
from ...load import load_icons
from ...frames.frame import frame
from ...box import save_file,openfile
from ...tktable import Table

from .....processamento.tabela import criar_tabela
from .....processamento.series_temporais.processamento import processamento

class frame_tabela(frame):

    #gets e sets objeto

    def set_title_janale(self,titulo):
        self.janela.title(titulo)

    #gets e sets classe

    def set_tabela_data(self,index_plan, array, row_ini=1, col_ini=1, NaN_fill=False):
        try:
            self.tabela.salvar_planilha(index=index_plan,array=array,row_ini=row_ini,col_ini=col_ini,NaN_fill=NaN_fill)
        except Exception as e:
            print(str(e))

    def set_frame_tabela_data(self):
        try:
            data_tabela=self.get_tabela_data(0)
            self.frame_tabela.set_header(data_tabela[0])
            self.frame_tabela.set_data(data_tabela[1:])
        except Exception as e:
            print(str(e))

    def get_tabela_data(self,index_plan,min_row=1,max_row=None,min_column=1,max_column=None,mode="horizontal"):
        try:
            return self.tabela.copiar_planilha(index=index_plan, min_row=min_row, max_row=max_row, min_col=min_column, max_col=max_column, mode=mode)
        except Exception as e:
            print(str(e))

    def __init__(self,janela,container,tabela=None):
        frame.__init__(self,janela,"frame_tabela",container)
        self.icones = load_icons(CAMINHO_ICONS_FRAME_TABELA, ".png")
        if(tabela==None):
            self.tabela=criar_tabela()
        else:
            self.tabela=tabela

    def iniciar_componentes(self):
        try:
            self.frame_div_opcoes=tk.Frame(self)
            self.frame_div_opcoes.pack_propagate(False)
            self.frame_div_opcoes.config(height=30,background="whitesmoke")
            self.frame_div_opcoes.pack(anchor=tk.NW,fill=tk.X)

            self.botao_salvar_tabela=tk.Button(self.frame_div_opcoes,image=self.icones["save_2"],command=self.salvar_tabela)
            self.botao_salvar_tabela.config(relief=tk.FLAT,background="whitesmoke")
            self.botao_salvar_tabela.image=self.icones["save_2"]
            self.botao_salvar_tabela.pack(side=tk.LEFT)

            self.botao_load_tabela=tk.Button(self.frame_div_opcoes,image=self.icones["open_2"],command=self.load_tabela)
            self.botao_load_tabela.config(relief=tk.FLAT,background="whitesmoke")
            self.botao_load_tabela.image=self.icones["open_2"]
            self.botao_load_tabela.pack(side=tk.LEFT)

            self.botao_desenhar_serie=tk.Button(self.frame_div_opcoes,image=self.icones["desenha_2"])
            self.botao_desenhar_serie.config(relief=tk.FLAT,background="whitesmoke")
            self.botao_desenhar_serie.image=self.icones["desenha_2"]
            self.botao_desenhar_serie.pack(side=tk.LEFT)

            data_tabela=self.get_tabela_data(index_plan=0)
            self.frame_tabela=Table(self,data_tabela[0])
            self.frame_tabela.place(x=0,y=30,relwidth=1,relheight=1,width=-25,height=-32)
            self.frame_tabela.set_data(data_tabela[1:])

            self.config(background=self.frame_tabela.background_cel_color)
        except Exception as e:
            print(str(e))

    def salvar_tabela(self):
        try:
            url_file=save_file(parent=self.janela,title="Salvar tabela",defaultextension=".xlsx")
            print(url_file)
            if(url_file!=""):
                self.tabela.salvar_tabela(url_file)
        except Exception as e:
            print(str(e))

    def load_tabela(self,ready_only=True,data_only=True):
        try:
            filetypes=(("Planilhas ( xlsx , csv )","*.xlsx;*.csv"), ("All files", "*.*"))
            url_file=openfile(parent=self.janela,title="Abir tabela",filetypes=filetypes)
            if(url_file!=""):
                self.tabela.load_tabela(url_file,ready_only,data_only)
                self.set_frame_tabela_data()
                self.set_title_janale(url_file)
        except Exception as e:
            print(str(e))