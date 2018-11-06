from . import _BACKEND

CAMINHO_JANELA_HELP=""
CAMINHO_JANELA_INFO=""
CAMINHO_JANELA_INICIAL=""
CAMINHO_JANELA_SERIES=""
CAMINHO_JANELA_ESTATISTICAS="app//backend//tkinter_backend//janelas//janela_estatisticas//janela_parametros.ini"
CAMINHO_JANELA_PARAMETROS=""
CAMINHO_JANELA_TABELA=""
CAMINHO_JANELA_TABELA_PLOT=""
CAMINHO_FRAMES_INI=""
CAMINHO_ICON_JANELA="app//data//icones//icones_janelas//icon.ico"
CAMINHO_ICONS_FRAME_INI="app//data//icones//icones_botoes//"
CAMINHO_ICONS_FRAME_SERIES="app//data//icones//icones_botoes//"
CAMINHO_ICONS_FRAME_CODE="app//data//icones//icones_botoes//"
CAMINHO_ICONS_FRAME_TABELA="app//data//icones//icones_botoes//"
if(_BACKEND=="tkinter"):
    CAMINHO_JANELA_HELP="app//backend//tkinter_backend//janelas//janela_help//janela_help.ini"
    CAMINHO_JANELA_INFO="app//backend//tkinter_backend//janelas//janela_info//janela_info.ini"
    CAMINHO_JANELA_INICIAL="app//backend//tkinter_backend//janelas//janela_inicial//janela_inicial.ini"
    CAMINHO_JANELA_SERIES="app//backend//tkinter_backend//janelas//janela_series_temporais//janela_series_temporais.ini"
    CAMINHO_JANELA_ADD_DATABASE="app//backend//tkinter_backend//janelas//janela_add_database//janela_add_database.ini"
    CAMINHO_JANELA_DATABASE="app//backend//tkinter_backend//janelas//janela_database//janela_database.ini"
    CAMINHO_JANELA_ESTATISTICAS="app//backend//tkinter_backend//janelas//janela_estatisticas//janela_parametros.ini"
    CAMINHO_JANELA_PARAMETROS="app//backend//tkinter_backend//janelas//janela_parametros//janela_parametros.ini"
    CAMINHO_JANELA_TABELA="app//backend//tkinter_backend//janelas//janela_tabela//janela_tabela.ini"
    CAMINHO_JANELA_TABELA_PLOT = "app//backend//tkinter_backend//janelas//janela_tabela_plot//janela_tabela_plot.ini"
    CAMINHO_FRAMES_INI="app//backend//tkinter_backend//frames//frames.ini"
elif(_BACKEND=="kivy"):
    CAMINHO_JANELA_HELP = "app//backend//kivy_backend//janelas//janela_help//janela_help.ini"
    CAMINHO_JANELA_INFO = "app//backend//kivy_backend//janelas//janela_info//janela_info.ini"
    CAMINHO_JANELA_INICIAL="app/backend//kivy_backend//janelas//janela_inicial//janela_inicial.ini"
    CAMINHO_JANELA_SERIES="app//backend//kivy_backend//janelas//janela_series_temporais//janela_series_temporais.ini"
    CAMANHO_JANELA_ESTATISTICAS = "app//backend//kivy_backend//janelas//janela_estatisticas//janela_parametros.ini"
    CAMINHO_JANELA_TABELA = "app//backend//kivy_backend//janelas//janela_tabela//janela_tabela.ini"
    CAMINHO_JANELA_TABELA_PLOT = "app//backend//kivy_backend//janelas//janela_tabela_plot//janela_tabela_plot.ini"
    CAMINHO_FRAMES_INI = "app//backend//kivy_backend//frames//frames.ini"