Extração Automatizada de Relatório de Telefonia
Este script Python foi desenvolvido para realizar a extração automatizada de um relatório de telefonia denominado 'Detalhamento de Chamadas Recebidas'. O relatório é obtido por meio da interface web na plataforma Elev, especificamente em três diferentes sites correspondentes a cada matriz da empresa.

Periodicidade e Critérios Temporais
Data Inicial e Data Final:

A data inicial do relatório é definida como o primeiro dia do mês vigente.
A data final é configurada como o dia atual da execução do script.
Exceção para o Primeiro Dia do Mês:

No primeiro dia de cada mês, o script ajusta automaticamente a extração para abranger o mês anterior, proporcionando uma visão abrangente do desempenho telefônico.
Sites e Matrizes Correspondentes
O script interage com os seguintes sites, cada um associado a uma matriz específica da empresa:

Site SBC: http://pabxsbc:9000/nxt3000/login.php
Site BF: http://pabxbf:9000/nxt3000/login.php
Site Liberty: http://pabxliberty:9000/nxt3000/login.php
Observações
Certifique-se de fornecer as credenciais de acesso adequadas para autenticação nos respectivos sites. As credenciais costumam ser as mesmas para todos os sites.
O código está configurado para lidar com a exportação de relatórios e interações com pop-ups específicos do site.
Recomenda-se revisar e ajustar os caminhos XPath e outros elementos específicos do site conforme necessário para garantir a funcionalidade contínua. Ajustes são importantes em caso de alterações no site.
Índice
Instalação
Configuração do Ambiente
Uso
Instalação
Antes de executar o script, assegure-se de ter o Python instalado em seu ambiente de desenvolvimento. Caso ainda não tenha o Python instalado, você pode baixá-lo e instalá-lo a partir do site oficial do Python.

Além disso, instale as bibliotecas necessárias com o seguinte comando no terminal:

bash
Copiar código
pip install -r requirements.txt
Certifique-se também de ter o Visual Studio Code (VS Code) ou outro editor de código de sua preferência.

Configuração do Ambiente
Para garantir o funcionamento correto do script, siga as instruções abaixo:

Caminho do Executável do Firefox:

Certifique-se de ter o navegador Mozilla Firefox instalado em sua máquina.
Caminho do Driver do Firefox (GeckoDriver):

Faça o download do GeckoDriver e ajuste o script para refletir o caminho correto em sua máquina. O código já está configurado para usar o WebDriver do Firefox.
Opções do Firefox:

Ajuste as opções do Firefox de acordo com suas preferências, se necessário. Adicione argumentos ou configure parâmetros específicos do navegador.
Instale as seguintes bibliotecas no seu terminal:

bash
Copiar código
pip install os shutil zipfile selenium time datetime python-dateutil
Uso
Para utilizar o script de extração de relatórios de telefonia:

Configuração de Credenciais:

Abra o script em seu editor de código e localize as variáveis username e password. Substitua-as pelas credenciais adequadas para acesso aos sites.
python
Copiar código
# Credenciais (substitua pelos seus valores)
username = "seu_usuario"
password = "sua_senha"
Definição de Caminhos XPath:

Verifique e ajuste os caminhos XPath no script para corresponder aos elementos reais nas páginas dos sites.
python
Copiar código
# XPath para os campos de usuário e senha (substitua pelos valores corretos)
user_xpath = "/caminho/do/campo/de/usuario"
password_xpath = "/caminho/do/campo/de/senha"
Configuração de Sites:

O script está configurado para interagir com três sites. Adicione ou remova sites conforme necessário.
python
Copiar código
sites = [
    "http://pabxsbc:9000/nxt3000/login.php",
    "http://pabxbf:9000/nxt3000/login.php",
    "http://pabxliberty:9000/nxt3000/login.php"
]
Execução do Script:

Abra um terminal na pasta onde o script está localizado e execute o seguinte comando:
bash
Copiar código
python nome_do_script.py
Acompanhamento da Execução
Durante a execução, o script imprimirá mensagens indicando o progresso e eventuais problemas. Revise a saída no terminal.

Descompactação e Movimentação de Arquivos
Ao final da execução, o script descompactará os arquivos ZIP, unificará os arquivos extraídos e os salvará em uma pasta especificada, cujo caminho pode ser alterado conforme necessário. O script também renomeará e moverá os arquivos para um diretório específico e fechará automaticamente o navegador ao finalizar a extração.
