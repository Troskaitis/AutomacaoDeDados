Descrição
Este script Python foi desenvolvido para realizar a extração automatizada de um relatório de telefonia denominado 'Detalhamento de Chamadas Recebidas'. O relatório é obtido por meio da interface web na plataforma Elev, especificamente em três diferentes sites que correspondem a cada matriz da empresa.
Periodicidade e Critérios Temporais
Data Inicial e Data Final:
A data inicial do relatório é definida como o primeiro dia do mês vigente.
A data final é configurada como o dia atual da execução do script.
Exceção para o Primeiro Dia do Mês:
No primeiro dia de cada mês, o script ajusta automaticamente a extração para abranger o mês anterior.
Isso resulta na obtenção do consolidado do mês anterior, proporcionando uma visão abrangente do desempenho telefônico.
Sites e Matrizes Correspondentes
O script foi concebido para interagir com os seguintes sites, cada um associado a uma matriz específica da empresa:
Site SBC: 'http://pabxsbc:9000/nxt3000/login.php'
Site BF: 'http://pabxbf:9000/nxt3000/login.php'
Site Liberty: 'http://pabxliberty:9000/nxt3000/login.php'
Observações
Certifique-se de fornecer as credenciais de acesso adequadas para autenticação nos respectivos sites. As credenciais costumam ser as mesmas para os três sites.
O código está configurado para lidar com a exportação de relatórios, incluindo interações com pop-ups específicos do site.
Recomenda-se revisar e ajustar os caminhos XPath e outros elementos específicos do site conforme necessário para garantir a funcionalidade contínua. Esta recomendação é importante caso ocorra alterações no site.
Índice
Instalação
Configuração do Ambiente
Uso
Instalação
Antes de executar o script, assegure-se de ter o Python devidamente instalado em seu ambiente de desenvolvimento. Caso ainda não tenha o Python instalado, você pode baixá-lo e instalá-lo a partir do site oficial do Python.
Além disso, é essencial garantir que as bibliotecas necessárias estejam presentes em sua máquina. Você pode instalar essas bibliotecas utilizando o seguinte comando no terminal:
pip install -r requirements.txt
Certifique-se também de ter o Visual Studio Code (VS Code) instalado em sua máquina, pois será utilizado como ambiente de desenvolvimento para a execução do script, ou se preferir, um editor de código de sua escolha.
Agora, você está pronto para iniciar a configuração e utilização do script para extração automatizada do relatório de telefonia.
Configuração do Ambiente
Para garantir o correto funcionamento do script, siga as instruções abaixo para configurar adequadamente o ambiente:
Caminho do Executável do Firefox: Certifique-se de ter o navegador Mozilla Firefox instalado em sua máquina.
Caminho do Driver do Firefox (GeckoDriver): Faça o download do GeckoDriver e ajuste o script para refletir o caminho correto em sua máquina. O código já está configurado para usar o WebDriver do Firefox com as opções corretas.
Opções do Firefox: Caso necessário, ajuste as opções do Firefox de acordo com suas preferências. Por exemplo, adicione argumentos ou configure parâmetros específicos do navegador.
Essas configurações são fundamentais para garantir a integração adequada entre o script Python e o navegador Firefox. Certifique-se de ajustar os caminhos conforme a estrutura de diretórios em sua máquina.
Além disso, instale as seguintes bibliotecas no seu Prompt de Comando:
pip install os shutil zipfile selenium time datetime python-dateutil
Uso
Para utilizar o script de extração de relatórios de telefonia, siga os passos abaixo:
Configuração de Credenciais:
Abra o script em seu editor de código preferido. Localize as variáveis username e password e substitua-as pelas credenciais adequadas para acesso aos sites correspondentes.
# Credenciais (substitua pelos seus valores)
username = "seu_usuario"
password = "sua_senha"
Definição de Caminhos XPath:
Certifique-se de que os caminhos XPath utilizados no script correspondam aos elementos reais nas páginas dos respectivos sites. Ajuste os seguintes caminhos conforme necessário:
# XPath para os campos de usuário e senha (substitua pelos valores corretos)
user_xpath = "/caminho/do/campo/de/usuario"
password_xpath = "/caminho/do/campo/de/senha"
Configuração de Sites:
O script está configurado para interagir com três sites diferentes. Certifique-se de adicionar ou remover sites conforme necessário:
sites = [
    "http://pabxsbc:9000/nxt3000/login.php",
    "http://pabxbf:9000/nxt3000/login.php",
    "http://pabxliberty:9000/nxt3000/login.php"
]
Execução do Script:
Abra um terminal na pasta onde o script está localizado. Execute o seguinte comando para iniciar a extração de relatórios:
python nome_do_script.py
Acompanhamento da Execução
Durante a execução, o script imprimirá mensagens indicando o progresso e eventuais problemas. Certifique-se de revisar a saída no terminal.
Descompactação de Arquivos
Ao final da execução, o script descompactará os arquivos ZIP, unificará os arquivos extraídos e os salvará em uma pasta, cujo caminho pode ser alterado de acordo com a necessidade.
Movimentação e Renomeação de Arquivos
O script renomeará e moverá os arquivos extraídos para um diretório especificado, seguindo um padrão de nomenclatura específico.
Fechamento do Navegador
O script fechará automaticamente o navegador ao finalizar a extração.
Lembre-se de que é fundamental seguir as boas práticas de segurança, como proteger as credenciais de acesso e garantir a confidencialidade dos dados extraídos.# AutomacaoDeDados
