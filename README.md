# Aplicativo Streamlit de Preços de Ações

Este é um aplicativo Streamlit que permite aos usuários visualizar preços históricos de ações do índice IBOV (Ibovespa) e acompanhar o desempenho dos ativos selecionados.

**Criador**: Edilson Alves da Silva

**Objetivo**: Estudar o uso de Streamlit e subir um arquivo para nuvem (serviço de hospedagem StreamlitCloud)

## Funcionalidades

* **Gráfico Interativo de Preços de Ações**: Exibe um gráfico de linha dos preços de fechamento para as ações selecionadas.
* **Período Personalizável**: Os usuários podem selecionar um período específico para visualizar os dados das ações.
* **Desempenho Individual e da Carteira**: Mostra o desempenho percentual das ações individuais selecionadas e o desempenho geral da carteira dentro do período escolhido.
* **Tema**: Utiliza um tema escuro para melhor legibilidade.

## Arquivos Neste Repositório

* `main.py`: O script principal da aplicação Streamlit.
* `IBOV.csv`: Um arquivo CSV contendo uma lista de tickers do Ibovespa e seus detalhes.
* `.streamlit/config.toml`: Arquivo de configuração para o Streamlit, definindo o tema como escuro.
* `.devcontainer/devcontainer.json`: Configuração para um contêiner de desenvolvimento, útil para ambientes de desenvolvimento consistentes.

## Como Executar Localmente

### Pré-requisitos

* Python 3.x
* pip (gerenciador de pacotes Python)

### Configuração

1.  **Clone o repositório (ou baixe os arquivos):**

    ```bash
    git clone <url_do_repositorio>
    cd <nome_do_repositorio>
    ```

2.  **Instale os pacotes Python necessários:**

    O aplicativo usa `streamlit`, `pandas` e `yfinance`.

    ```bash
    pip install streamlit pandas yfinance
    ```

### Executando o Aplicativo

1.  **Navegue até o diretório do projeto** (onde `main.py` está localizado) no seu terminal.

2.  **Execute o aplicativo Streamlit:**

    ```bash
    streamlit run main.py
    ```

    Isso abrirá o aplicativo em seu navegador da web, geralmente em `http://localhost:8501`.

## Uso do Aplicativo

1.  **Barra Lateral de Filtros**: Na barra lateral esquerda, você encontrará os seguintes filtros:
    * **Escolha as Ações**: Selecione uma ou mais ações no menu suspenso para exibir seus gráficos de preços.
    * **Selecione o Período**: Use o controle deslizante para escolher o intervalo de datas desejado para os dados das ações.

2.  **Gráfico de Preços de Ações**: A área principal do aplicativo exibe um gráfico de linha mostrando os preços de fechamento das ações selecionadas ao longo do período escolhido.

3.  **Desempenho dos Ativos**: Abaixo do gráfico, você verá o desempenho de cada ativo selecionado, indicado por porcentagens verdes (positivas) ou vermelhas (negativas).

4.  **Desempenho da Carteira**: Na parte inferior, será exibido o desempenho geral da sua carteira selecionada. A carteira assume um investimento inicial de 1000 unidades em cada ação selecionada.

## Contêiner de Desenvolvimento (Opcional)

Este projeto inclui uma configuração `.devcontainer`, que permite executar o aplicativo em um ambiente de desenvolvimento consistente usando Visual Studio Code Dev Containers ou GitHub Codespaces.

Se você estiver usando o VS Code, você pode:
1. Instalar a extensão "Dev Containers".
2. Abrir o projeto no VS Code.
3. Quando solicitado, "Reabrir no Contêiner".

O arquivo `devcontainer.json` configura o ambiente para:
* Usar uma imagem Python 3.11.
* Instalar os pacotes necessários (`streamlit`, `pandas`, `yfinance`).
* Executar automaticamente o aplicativo Streamlit na porta 8501 quando o contêiner for anexado.
