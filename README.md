# countries_info :world_map:

# Web Scraping Project :spider:

This project is a web scraping tool built with Python. It extracts data from a particular website and save it ina a file for further analysis.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)

## Installation

1. Clone the repo
    ```sh
    git clone https://github.com/your_username/web-scraping-project.git
    ```
2. Change to the project directory
    ```sh
    cd web-scraping-project
    ```

3. Pull the missing dependencies
   
   ```sh
   pipreqs .
   ``` 

4. Install the required packages
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the scraper script
    ```sh
    python scraper.py
    ```
2. The script will output the scraped data to a file named `output.json` :page_with_curl:

## Dependencies

- Python 3 🐍
- Requests 
- BeautifulSoup4 

You can install the dependencies using the following command:
```sh
pip install -r requirements.txt
