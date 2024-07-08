# RG-scrapper

RG-scrapper is a Python-based web crawler designed to extract data from [ResearchGate.net](https://www.researchgate.net). It collects information about researchers, including their profiles, publications, and more. This tool leverages Selenium for web automation and scraping tasks.

## Features

- **Automated Data Extraction**: Collects researcher profiles and publication data.
- **Selenium-Based**: Utilizes Selenium for robust web scraping and automation.
- **Data Processing**: Scripts for processing and storing scraped data.

## Requirements

- Python 3.x
- Selenium
- WebDriver for your browser (e.g., ChromeDriver for Google Chrome)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mohamedfadlalla/RG-scrapper.git
   cd RG-scrapper
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Download the WebDriver for your browser and ensure it is in your system PATH.

## Usage

1. Update `config.py` with your desired settings, including your ResearchGate credentials and other parameters.
2. Run the scraper:
   ```bash
   python scraper.py
   ```

## Notes

- Ensure compliance with ResearchGate's terms of service when using this tool.
- Modify the scraping logic in `scraper.py` as needed to fit specific data requirements.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.

## Disclammer
ResearchGate.net porhibit automated access without prior express permission of researchgate in writing, 
it's under the User Obligatioin in Term of Use
