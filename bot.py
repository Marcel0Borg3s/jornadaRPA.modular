# Import for the Web Bot
from botcity.web import WebBot, Browser, By
# import dos módulos Web e Dados Excel
from jornadaRPA_browser import *
from jornadaRPA_dados import *


def main():
    
    bot = WebBot()

    #Instancia o navegador configurado
    navegador = Browser_jornadaRPA.configurar_browser(bot, "CHROME", False)

    # Opens the Forms by Jornada RPA website. / import
    navegador.browse("https://jornadarpa.com.br/alunos/desafios/inputforms/inputforms.html")

    # Wait 3 seconds before closing
    navegador.wait(1000)

    #importando a leitura de dados 
    dados = Dados_jornadaRPA.ler_planilha("E:\\RPA\\BotCity\\Projetos\\entradaDados_randomico\\resources\\lista.xlsx", 
                                          None, 
                                          "Dados",
                                           False)
    

    for linha in dados:

        # Extraindo da Tabela e descompactando a lista em linha
        ID, PrimeiroNome, UltimoNome, Pais, DataNasc, Solicitacao = linha

        # Formatar a datas como string no formato dd/mm/aaaa
        #DataNasc = DataNasc.strftime("%d/%m/%Y")
        #Solicitacao = Solicitacao.strftime("%d/%m/%Y")

        # Mapeamento dos campos formulário/ dentro do for pois são dinâmicos os campos
        try:
            campoID = bot.find_element("/html/body/div[2]/section/div[2]/div/section/div[2]/form/div/div[1]/div/div/input",
            by=By.XPATH)
            campoPriNome = bot.find_element("/html/body/div[2]/section/div[2]/div/section/div[2]/form/div/div[2]/div/div/input", 
            by=By.XPATH)
            campoUltNome = bot.find_element("/html/body/div[2]/section/div[2]/div/section/div[2]/form/div/div[3]/div/div/input",
            by=By.XPATH)
            campoPais = bot.find_element("/html/body/div[2]/section/div[2]/div/section/div[2]/form/div/div[5]/div/div/select",
            by=By.XPATH)
            campoNasc = bot.find_element("/html/body/div[2]/section/div[2]/div/section/div[2]/form/div/div[4]/div/div/input",
            by=By.XPATH)
            campoSolCred = bot.find_element("/html/body/div[2]/section/div[2]/div/section/div[2]/form/div/div[6]/div/div/input",
            by=By.XPATH)
            btnGravar = bot.find_element("btao", by=By.ID)
        except Exception as e:
            print(f"Erro ao mapear campos: {e}")

        try:
            # Preenchimento dos campos formulário
            campoID.send_keys(ID)
            campoPriNome.send_keys(PrimeiroNome)
            campoUltNome.send_keys(UltimoNome)
            campoPais.send_keys(Pais)
            campoNasc.send_keys(Dados_jornadaRPA.convertData(DataNasc))
            campoSolCred.send_keys(Dados_jornadaRPA.convertData(Solicitacao))
        except Exception as e:
            print(f"Erro ao preencher campos: {e}")

        # Click botão Gravar
        btnGravar.click()

        


    # Finish and clean up the Web Browser
    # You MUST invoke the stop_browser to avoid
    # leaving instances of the webdriver open
    navegador.stop_browser()

    

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
