# Import for the Web Bot
from botcity.web import WebBot, Browser, By
from botcity.plugins.excel import BotExcelPlugin

# Import date time
import datetime

class Dados_jornadaRPA():

    #Ler planilha
    def ler_planilha(path, range, sheet, head=True):

        # Instantiate the plugin
        bot_excel = BotExcelPlugin()

        # Ober dados da Planilha
        if head:
            dados = bot_excel.read(path).get_range(range, sheet)
        else:
            # Ignora o cabeçalho
            dados = bot_excel.read(path).get_range(range, sheet)[1:]

        return dados
    
    def convertData(data):
        dataConv = data.strftime("%d/%m/%Y")
        return dataConv

    





