# Import for the Web Bot
from botcity.web import WebBot, Browser, By

class Browser_jornadaRPA():

    #Configuração paraabrir o navegador escolhido
    def configurar_browser(bot, navegador="CHROME", headless=False):

        #define se vai rodar em for ou background
        bot.headless = headless

        #Define o navegador
        if navegador == "CHROME":
            bot.browser = Browser.CHROME
            bot.driver_path = "E:\RPA\DRIVERS\web_Driver\chromedriver.exe"
        elif navegador == "EDGE":
            bot.browser = Browser.EDGE
            bot.driver_path = "E:\RPA\DRIVERS\web_Driver\msedgedriver.exe"
        elif navegador == "FIREFOX":
            bot.browser = Browser.FIREFOX
            bot.driver_path = "E:\RPA\DRIVERS\web_Driver\geckodriver.exe"
       
       #retorna a estancia do bot
        return bot
    



