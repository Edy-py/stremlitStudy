This `README.md` file provides an overview of the Streamlit stock price application based on the provided code and files.

```markdown
# Streamlit Stock Price App

This is a Streamlit application that allows users to visualize historical stock prices from the IBOV (Ibovespa) index and track the performance of selected assets.

## Features

* **Interactive Stock Price Chart**: Displays a line chart of the closing prices for selected stocks.
* **Customizable Date Range**: Users can select a specific period to view stock data.
* **Individual and Portfolio Performance**: Shows the percentage performance of individual selected stocks and the overall portfolio performance within the chosen timeframe.
* **Theming**: Uses a dark theme for better readability.

## Files in this Repository

* `main.py`: The core Streamlit application script.
* `IBOV.csv`: A CSV file containing a list of Ibovespa tickers and their details.
* `.streamlit/config.toml`: Configuration file for Streamlit, setting the theme to dark.
* `.devcontainer/devcontainer.json`: Configuration for a development container, useful for consistent development environments.

## How to Run Locally

### Prerequisites

* Python 3.x
* pip (Python package installer)

### Setup

1.  **Clone the repository (or download the files):**

    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

2.  **Install the required Python packages:**

    The application uses `streamlit`, `pandas`, and `yfinance`.

    ```bash
    pip install streamlit pandas yfinance
    ```

### Running the Application

1.  **Navigate to the project directory** (where `main.py` is located) in your terminal.

2.  **Run the Streamlit application:**

    ```bash
    streamlit run main.py
    ```

    This will open the application in your web browser, usually at `http://localhost:8501`.

## Application Usage

1.  **Filters Sidebar**: On the left sidebar, you'll find the following filters:
    * **Choose Stocks**: Select one or more stocks from the dropdown to display their price charts.
    * **Select Period**: Use the slider to choose the desired date range for the stock data.

2.  **Stock Price Chart**: The main area of the application displays a line chart showing the closing prices of the selected stocks over the chosen period.

3.  **Asset Performance**: Below the chart, you will see the performance of each selected asset, indicated by green (positive) or red (negative) percentages.

4.  **Portfolio Performance**: At the bottom, the overall performance of your selected portfolio will be displayed. The portfolio assumes an initial investment of 1000 units in each selected stock.

## Development Container (Optional)

This project includes a `.devcontainer` setup, which allows you to run the application within a consistent development environment using Visual Studio Code Dev Containers or GitHub Codespaces.

If you are using VS Code, you can:
1. Install the "Dev Containers" extension.
2. Open the project in VS Code.
3. When prompted, "Reopen in Container".

The `devcontainer.json` file configures the environment to:
* Use a Python 3.11 image.
* Install necessary packages (`streamlit`, `pandas`, `yfinance`).
* Automatically run the Streamlit app on port 8501 when the container is attached.
```
