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
            _extracted_from_realizar_etapas_para_site_48(
                driver, relatorio_telefonia_xpath, 2
            )
            _extracted_from_realizar_etapas_para_site_38(
                driver, data_inicio_xpath, primeiro_dia_mes
            )
            _extracted_from_realizar_etapas_para_site_38(
                driver, data_final_xpath, data_final
            )
            # desmarcar o checkbox
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
                print(
                    f"Não foi possível localizar o botão ou link de exportação em {site}."
                )

        except Exception:
            print(
                f"Não foi possível localizar o botão ou link do relatório de telefonia em {site}."
            )

    except Exception:
        print(f"Não foi possível localizar o ícone 'Relatórios' em {site}")


# TODO Rename this here and in `realizar_etapas_para_site`
def _extracted_from_realizar_etapas_para_site_38(driver, arg1, arg2):
            # Preenchendo os campos de data de início e data final
    data_inicio_field = driver.find_element(By.XPATH, arg1)
    data_inicio_field.clear()
    data_inicio_field.send_keys(arg2)


# TODO Rename this here and in `realizar_etapas_para_site`
def _extracted_from_realizar_etapas_para_site_48(driver, arg1, arg2):
    exportar_element = driver.find_element(By.XPATH, arg1)
    exportar_element.click()

    # Aguardando um tempo suficiente para a exportação
    time.sleep(arg2)


# Função para lidar com o pop-up
def lidar_com_popup(driver):
    try:
        # Aguardar até que o pop-up seja visível
        pop_up = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, pop_up_xpath))
        )

        # Marcar a opção desejada no pop-up
        opcao_tipo_arquivo = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.XPATH, opcao_tipo_arquivo_xpath))
        )
        opcao_tipo_arquivo.click()

        # Aguardar um curto período para permitir que o pop-up seja processado
        time.sleep(2)

        # Localizar o botão "EXPORTAR" pelo XPath e clicar
        exportar_botao = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[1]/div[2]/table/tbody/tr[3]/td/input[1]")
            )
        )
        exportar_botao.click()

        print("Opção selecionada no pop-up. Iniciando exportação.")

    except Exception as e:
        print(f"Não foi possível interagir com o pop-up. Erro: {str(e)}")


# Função para descompactar os arquivos zip
def descompactar_arquivos_zip():
    # Caminho do diretório de downloads
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")

    # Lista todos os arquivos na pasta de downloads
    arquivos_zip = [
        arquivo for arquivo in os.listdir(downloads_path) if arquivo.endswith(".zip")
    ]

    # Diretório de destino para a extração (pode ser ajustado conforme necessário)
    diretorio_destino = os.path.join(downloads_path, "Extrações_Elev")

    # Certificando-se de que o diretório de destino existe, se não, criá-lo
    os.makedirs(diretorio_destino, exist_ok=True)

    # Descompactando todos os arquivos zip
    for arquivo_zip in arquivos_zip:
        caminho_arquivo_zip = os.path.join(downloads_path, arquivo_zip)
        with zipfile.ZipFile(caminho_arquivo_zip, "r") as zip_ref:
            zip_ref.extractall(diretorio_destino)
        print(f"Arquivo {arquivo_zip} descompactado em {diretorio_destino}")

        # Excluindo o arquivo zip original
        os.remove(caminho_arquivo_zip)
        print(f"Arquivo {arquivo_zip} removido.")


# Configuração do WebDriver para Firefox
firefox_options = webdriver.FirefoxOptions()
# Executar em modo headless, se necessário
# firefox_options.add_argument("--headless")  

# Inicializando o driver do Firefox
driver = webdriver.Firefox(options=firefox_options)

# Maximiza a janela de visualização
driver.maximize_window()

# Sites a serem percorridos
sites = [
    "http://sitefilial1",
    "http://sitefilial2",
    "http://sitefilial3",
]

# XPath para os campos de usuário e senha (substitua pelos valores corretos)
user_xpath = (
    "/html/body/center/div/table[2]/tbody/tr[3]/td[2]/form/table/tbody/tr[2]/td/input"
)
password_xpath = (
    "/html/body/center/div/table[2]/tbody/tr[3]/td[2]/form/table/tbody/tr[4]/td/input"
)

# Credenciais (substitua pelos seus valores)
username = "seu.usuario"
password = "senha"

# XPath para o botão "OK" (substitua pelos valores corretos)
ok_button_xpath = (
    "/html/body/center/div/table[2]/tbody/tr[3]/td[2]/form/table/tbody/tr[5]/td/input"
)

# XPath para o ícone "Relatórios" baseado em suas características visuais
relatorios_icon_xpath = (
    "/html/body/center/div/table[1]/tbody/tr[3]/td/table/tbody/tr/td/a[2]"
)

# XPath para o botão ou link que leva ao relatório de telefonia (substitua pelos valores corretos)
relatorio_telefonia_xpath = (
    "/html/body/center/div/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[11]/td[1]"
)

# XPath para o campo de data de início (substitua pelos valores corretos)
data_inicio_xpath = "/html/body/center/div/table[2]/tbody/tr[3]/td[2]/form/table[2]/tbody/tr[2]/td[2]/input[1]"

# XPath para o campo de data final (substitua pelos valores corretos)
data_final_xpath = "/html/body/center/div/table[2]/tbody/tr[3]/td[2]/form/table[2]/tbody/tr[2]/td[2]/input[2]"

# XPath para o botão ou link de exportação (substitua pelos valores corretos)
exportar_xpath = "/html/body/center/div/table[2]/tbody/tr[3]/td[2]/form/table[1]/tbody/tr/td/a[1]/img"

# XPath para o pop-up
pop_up_xpath = '//*[@id="div-exportar-relatorio8"]/table'

# XPath para a opção desejada do tipo de arquivo no pop-up
opcao_tipo_arquivo_xpath = (
    '//*[@id="div-exportar-relatorio8"]/table/tbody/tr[1]/td/label[2]/input'
)

# Caminho do diretório de downloads
downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")

# Diretório de destino para a extração (pode ser ajustado conforme necessário)
diretorio_destino = os.path.join(downloads_path, "Extrações_Elev")

# Obtendo a data atual
data_atual = datetime.now()

# Calculando a data final (dia atual)
# data_final = (data_atual - timedelta(days=1)).strftime("%d/%m/%Y")
data_final = data_atual.strftime("%d/%m/%Y")

# Verificando se a data final é o primeiro dia do mês
if data_atual.day == 1:
    # Se a data final for o primeiro dia do mês, ajustamos a lógica
    data_inicial = (data_atual - relativedelta(months=1)).replace(day=1)
else:
    data_inicial = data_atual.replace(day=1)
    
# Formatando as datas
primeiro_dia_mes = data_inicial.strftime("%d/%m/%Y")

# Obtendo o ano atual
ano_atual = data_inicial.year

# Construindo o caminho da pasta
caminho_destino_final = "caminho de destino do arquivo"

# Obtendo o mês atual no formato "Jan"
mes_atual_numero = data_inicial.strftime("%m")
mes_atual_abreviado = data_inicial.strftime("%b")

# Iterando pelos sites
for site in sites:
    driver.get(site)
    realizar_etapas_para_site(driver, site)

# Descompactando os arquivos ao final
descompactar_arquivos_zip()

# Movimentação e Renomeação de Arquivos:
arquivos_extraidos = [
    arquivo for arquivo in os.listdir(diretorio_destino) if not arquivo.endswith(".zip")
]

for indice, arquivo in enumerate(arquivos_extraidos):
    caminho_arquivo = os.path.join(diretorio_destino, arquivo)
    
    # Determinando o nome do site com base no índice
    if indice == 0:
        nome_site = "SBC"
    elif indice == 1:
        nome_site = "BF"
    elif indice == 2:
        nome_site = "LB"
    else:
        nome_site = "Desconhecido"
        
    # Obtendo a extensão do arquivo original
    extensao_arquivo = os.path.splitext(arquivo)[1]

    # Construindo o novo nome do arquivo
    novo_nome_arquivo = f"detalhamento_chamadas_recebidas_{ano_atual} {mes_atual_numero} {mes_atual_abreviado} {nome_site}{extensao_arquivo}"

    # Construindo o caminho do arquivo com o novo nome
    caminho_novo_arquivo = os.path.join(caminho_destino_final, novo_nome_arquivo)

    # Movendo e renomeando o arquivo
    shutil.move(caminho_arquivo, caminho_novo_arquivo)

# Removendo a pasta Extrações_Elev
shutil.rmtree(diretorio_destino)

# Fechando o navegador
driver.quit()
