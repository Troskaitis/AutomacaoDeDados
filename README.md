# Telefonia - Detalhamento de Chamadas Recebidas

## Descrição:

Este script Python foi desenvolvido para realizar a extração automatizada de um relatório de telefonia denominado 'Detalhamento de Chamadas Recebidas'. O relatório é obtido por meio da interface web na plataforma Elev, especificamente em três diferentes sites que correspondem a cada matriz da empresa.

Periodicidade e Critérios Temporais:

O processo de extração segue uma lógica temporal específica:

Data Inicial e Data Final:

A data inicial do relatório é definida como o primeiro dia do mês vigente.
A data final é configurada como o dia anterior à execução do script.

Exceção para o Primeiro Dia do Mês:

No primeiro dia de cada mês, o script ajusta automaticamente a extração para abranger o mês anterior.
Isso resulta na obtenção do consolidado do mês anterior, proporcionando uma visão abrangente do desempenho telefônico.

Sites e Matrizes Correspondentes:
O script foi concebido para interagir com os seguintes sites, cada um associado a uma matriz específica da empresa:

1. Site SBC: 'http://pabxbf:9000/nxt3000/login.php'
2. Site BF: 'http://pabxsbc:9000/nxt3000/login.php'
3. Site Liberty: 'http://pabxliberty:9000/nxt3000/login.php'

Observações:

Certifique-se de fornecer as credenciais de acesso adequadas para autenticação nos respectivos sites. as credenciais costumam ser as mesmas para os 3 sites.
O código está configurado para lidar com a exportação de relatórios, incluindo interações com pop-ups específicos do site.
Recomenda-se revisar e ajustar os caminhos XPath e outros elementos específicos do site conforme necessário para garantir a funcionalidade contínua. esta é recomenda caso ocorra alterações no site.
Este script oferece uma solução automatizada e eficiente para a obtenção regular de relatórios de telefonia, mantendo a consistência e relevância das informações extraídas.

## Índice

1. [Instalação](#instalação)
2. [Configuração do Ambiente](#configuração-do-ambiente)
3. [Uso](#uso)

## Instalação

Antes de executar o script, assegure-se de ter o Python devidamente instalado em seu ambiente de desenvolvimento. Caso ainda não tenha o Python instalado, você pode baixá-lo e instalá-lo a partir do site oficial do Python.

Além disso, é essencial garantir que as bibliotecas necessárias estejam presentes em sua máquina. Você pode instalar essas bibliotecas utilizando o seguinte comando no terminal:

pip install -r requirements.txt

Certifique-se também de ter o Visual Studio Code (VS Code) instalado em sua máquina, pois será utilizado como ambiente de desenvolvimento para a execução do script, ou se preferir, um editor de código de sua escolha.

Agora, você está pronto para iniciar a configuração e utilização do script para extração automatizada do relatório de telefonia.

## configuração-do-ambiente

Para garantir o correto funcionamento do script, siga as instruções abaixo para configurar adequadamente o ambiente:

1. Caminho do Executável do Chrome:
   Certifique-se de ter o navegador Google Chrome instalado em sua máquina.
   No código, defina o caminho do executável do Chrome (chrome_path) para refletir o caminho correto em sua máquina.

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

2. Caminho do Driver do Chrome (ChromeDriver):
   Faça o download do ChromeDriver e substitua chrome_driver_path pelo caminho real onde o ChromeDriver está localizado em sua máquina.

chrome_driver_path = r'C:\Caminho\Para\chromedriver.exe'

3. Opções do Chrome:
   Caso necessário, ajuste as opções do Chrome de acordo com suas preferências. Por exemplo, adicione extensões ou configure parâmetros específicos do navegador.

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = chrome_path
chrome_options.add_argument(f"webdriver.chrome.driver={chrome_driver_path}")

Essas configurações são fundamentais para garantir a integração adequada entre o script Python e o navegador Chrome. Certifique-se de ajustar os caminhos conforme a estrutura de diretórios em sua máquina.

instale tambem as seguintes bibliotecas no seu Prompt de Comando:

1. os: Fornece uma maneira de usar funcionalidades dependentes do sistema operacional, como interação com o sistema de arquivos.
2. zipfile: Oferece ferramentas para criar, ler, escrever, anexar e listar arquivos ZIP.
3. selenium: Uma biblioteca para automação de testes em navegadores web.
4. time: Fornece várias funções relacionadas ao tempo, como sleep para pausar a execução do programa.
5. datetime: Oferece classes para manipulação de datas e horas.
6. dateutil.relativedelta: Uma extensão do módulo datetime que fornece uma maneira fácil de fazer cálculos com datas.

Após realizar essas configurações, o ambiente estará pronto para a execução bem-sucedida do script de extração de relatórios de telefonia.

## Uso

Para utilizar o script de extração de relatórios de telefonia, siga os passos abaixo:

1. Configuração de Credenciais:

Abra o script em seu editor de código preferido.
Localize as variáveis username e password e substitua-as pelas credenciais adequadas para acesso aos sites correspondentes.

Credenciais (substitua pelos seus valores)
username = "seu_usuario"
password = "sua_senha"

2. Definição de Caminhos XPath:
   Certifique-se de que os caminhos XPath utilizados no script correspondam aos elementos reais nas páginas dos respectivos sites. Ajuste os seguintes caminhos conforme necessário:

XPath para os campos de usuário e senha (substitua pelos valores corretos)
user_xpath = "/caminho/do/campo/de/usuario"
password_xpath = "/caminho/do/campo/de/senha"

3. Configuração de Sites:
   O script está configurado para interagir com três sites diferentes. Certifique-se de adicionar ou remover sites conforme necessário:

Sites a serem percorridos:

sites = [
"http://pabxsbc:9000/nxt3000/login.php",
"http://pabxbf:9000/nxt3000/login.php",
"http://pabxliberty:9000/nxt3000/login.php"
]

4. Execução do Script:
   Abra um terminal na pasta onde o script está localizado.
   Execute o seguinte comando para iniciar a extração de relatórios:

python nome_do_script.py

Acompanhamento da Execução:
Durante a execução, o script imprimirá mensagens indicando o progresso e eventuais problemas. Certifique-se de revisar a saída no terminal.

Descompactação de Arquivos:
Ao final da execução, o script descompactará os arquivos ZIP, unificará os arquivos extraídos e os salvará em uma pasta, cujo caminho pode ser alterado de acordo com a necessidade. Lembrando que, durante este processo o código irá identificar se no caminho informado já existe uma pasta ano correspondente, assim como uma pasta mês, não existindo, ele irá criar seguindo este padrão: Ano '2023', mês '12 Dec'.

Fechamento do Navegador:
O script fechará automaticamente o navegador ao finalizar a extração.
Lembre-se de que é fundamental seguir as boas práticas de segurança, como proteger as credenciais de acesso e garantir a confidencialidade dos dados extraídos.
