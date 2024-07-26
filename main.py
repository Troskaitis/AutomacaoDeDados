import os
import shutil
import zipfile
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def realizar_etapas_para_site(driver, site):
    # Adicionando um tempo de espera (ajuste conforme necessário)
    time.sleep(2)

    # Preenchendo os campos de usuário e senha
    user_field = driver.find_element(By.XPATH, user_xpath)
    password_field = driver.find_element(By.XPATH, password_xpath)

    user_field.send_keys(username)
    password_field.send_keys(password)

    _extracted_from_realizar_etapas_para_site_48(driver, ok_button_xpath, 2)
    # Tentando localizar o ícone "Relatórios" como um elemento visual
    try:
        _extracted_from_realizar_etapas_para_site_48(driver, relatorios_icon_xpath, 2)
        # Tentando localizar o botão ou link do relatório de telefonia e clicar nele
        try:
            _extracted_from_realizar_etapas_para_site_48(driver, relatorio_telefonia_xpath, 2)
            _extracted_from_realizar_etapas_para_site_38(driver, data_inicio_xpath, primeiro_dia_mes)
            _extracted_from_realizar_etapas_para_site_38(driver, data_final_xpath, data_final)
            # Desmarcar o checkbox
            if site == "http://pabxbf:9000/nxt3000/login.php":
                checkbox = driver.find_element(By.XPATH, '//*[@id="ativo-t"]')
                if checkbox.is_selected():
                    checkbox.click()
                    
            # Tentando localizar o botão ou link de exportação e clicar nele
            try:
                _extracted_from_realizar_etapas_para_site_48(driver, exportar_xpath, 20)
                # Lidar com o pop-up apenas para o site específico
                if site == "http://pabxbf:9000/nxt3000/login.php":
                    lidar_com_popup(driver)

            except Exception:
                print(f"Não foi possível localizar o botão ou link de exportação em {site}.")

        except Exception:
            print(f"Não foi possível localizar o botão ou link do relatório de telefonia em {site}.")

    except Exception:
        print(f"Não foi possível localizar o ícone 'Relatórios' em {site}")

def _extracted_from_realizar_etapas_para_site_38(driver, arg1, arg2):
    # Preenchendo os campos de data de início e data final
    data_inicio_field = driver.find_element(By.XPATH, arg1)
    data_inicio_field.clear()
    data_inicio_field.send_keys(arg2)

def _extracted_from_realizar_etapas_para_site_48(driver, arg1, arg2):
    exportar_element = driver.find_element(By.XPATH, arg1)
    exportar_element.click()
    # Aguardando um tempo suficiente para a exportação
    time.sleep(arg2)

def lidar_com_popup(driver):
    try:
        # Aguardar até que o pop-up apareça
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//div[@class="ui-dialog-titlebar"]')))

        # Localizar o botão "OK" no pop-up e clicar nele
        popup_ok_button = driver.find_element(By.XPATH, '//button[text()="OK"]')
        popup_ok_button.click()

    except Exception:
        print("Não foi possível lidar com o pop-up.")

def main():
    global user_xpath, password_xpath, ok_button_xpath, relatorios_icon_xpath, relatorio_telefonia_xpath, data_inicio_xpath, data_final_xpath, exportar_xpath, primeiro_dia_mes, data_final, username, password

    # Variáveis globais para facilitar ajustes
    user_xpath = '//*[@id="usuario"]'
    password_xpath = '//*[@id="senha"]'
    ok_button_xpath = '//*[@id="login"]/table/tbody/tr[4]/td/input'
    relatorios_icon_xpath = '//*[@id="ext-gen70"]'
    relatorio_telefonia_xpath = '//*[@id="ext-gen156"]/div/li[3]/ul/li[6]/div/a/span'
    data_inicio_xpath = '//*[@id="dataInicial"]'
    data_final_xpath = '//*[@id="dataFinal"]'
    exportar_xpath = '//*[@id="btnExportar"]/button'
    
    # Definição da data atual
    hoje = datetime.now()
    
    # Verificação se é o primeiro dia do mês
    if hoje.day == 1:
        # Definição da data inicial e data final para o mês anterior
        primeiro_dia_mes = (hoje - relativedelta(months=1)).replace(day=1).strftime("%d/%m/%Y")
        data_final = (hoje - relativedelta(months=1)).replace(day=hoje.day-1).strftime("%d/%m/%Y")
    else:
        # Definição da data inicial e data final para o mês atual
        primeiro_dia_mes = hoje.replace(day=1).strftime("%d/%m/%Y")
        data_final = hoje.strftime("%d/%m/%Y")
    
    username = "seu_usuario"
    password = "sua_senha"
    
    # Definição das opções do Firefox
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument("--headless")
    firefox_options.set_preference("browser.download.folderList", 2)
    firefox_options.set_preference("browser.download.manager.showWhenStarting", False)
    firefox_options.set_preference("browser.download.dir", os.getcwd())
    firefox_options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/zip")
    
    # Inicialização do WebDriver do Firefox
    driver = webdriver.Firefox(options=firefox_options)

    try:
        sites = [
            "http://pabxsbc:9000/nxt3000/login.php",
            "http://pabxbf:9000/nxt3000/login.php",
            "http://pabxliberty:9000/nxt3000/login.php"
        ]
        
        for site in sites:
            driver.get(site)
            realizar_etapas_para_site(driver, site)
            time.sleep(2)  # Adicionando um tempo de espera entre os sites

    finally:
        driver.quit()

    # Definindo o diretório de downloads e o diretório de destino
    download_dir = os.getcwd()
    destination_dir = os.path.join(download_dir, "extraidos")

    # Criando o diretório de destino, se não existir
    os.makedirs(destination_dir, exist_ok=True)

    # Iterando pelos arquivos no diretório de downloads
    for file_name in os.listdir(download_dir):
        if file_name.endswith(".zip"):
            file_path = os.path.join(download_dir, file_name)
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(destination_dir)
            
            # Movendo o arquivo ZIP para um diretório de backup
            backup_dir = os.path.join(download_dir, "backup")
            os.makedirs(backup_dir, exist_ok=True)
            shutil.move(file_path, os.path.join(backup_dir, file_name))
    
    # Movendo e renomeando os arquivos extraídos
    for root, dirs, files in os.walk(destination_dir):
        for file in files:
            if file.endswith(".csv"):
                old_path = os.path.join(root, file)
                new_file_name = f"detalhamento_{file}"
                new_path = os.path.join(destination_dir, new_file_name)
                shutil.move(old_path, new_path)

if __name__ == "__main__":
    main()