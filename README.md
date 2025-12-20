# FreeRice Vocabulary Bot

This project provides a Python script to automate playing the English vocabulary game on FreeRice.com. It leverages web scraping and a dictionary API to intelligently select answers, aiming to correctly guess the meaning of words.

## Description

The `scraper.py` script opens a Chrome browser instance, navigates to the FreeRice English Vocabulary game, and then continuously attempts to answer questions. For each question, it extracts the target word and the provided multiple-choice options. It then queries the Free Dictionary API for the definition and synonyms of the target word. By comparing the API's response with the available options, the bot tries to identify the correct answer. The script tracks the number of correct and incorrect answers during its operation.

## Features

*   **Automated Game Play**: Navigates to FreeRice.com and handles game progression automatically.
*   **Cookie Banner Handling**: Automatically dismisses the cookie consent banner if present.
*   **Question and Option Extraction**: Identifies the vocabulary word and its potential definitions from the webpage.
*   **Dictionary API Integration**: Utilizes the Free Dictionary API (dictionaryapi.dev) to fetch definitions and synonyms for the question word.
*   **Intelligent Answering**: Attempts to find an answer option that matches the definitions or synonyms retrieved from the API.
*   **Score Tracking**: Keeps a running count of correct and incorrect answers.
*   **Undetected ChromeDriver**: Uses `undetected_chromedriver` to minimize detection as a bot.
*   **Graceful Termination**: Allows for stopping the bot cleanly with a KeyboardInterrupt (Ctrl+C), displaying the final score.

## Installation

To set up and run this project, follow these steps:

1.  **Python**: Ensure you have Python 3.x installed on your system.
2.  **Browser**: Make sure you have Google Chrome installed, as `undetected_chromedriver` relies on it.
3.  **Dependencies**: Install the required Python libraries using pip:
    ```bash
    pip install selenium requests undetected-chromedriver
    ```

    *   `selenium`: For web browser automation.
    *   `requests`: For making HTTP requests to the dictionary API.
    *   `undetected-chromedriver`: A selenium wrapper designed to avoid browser detection.

## Usage

1.  **Run the script**:
    Navigate to the project directory in your terminal and execute the script:
    ```bash
    python scraper.py
    ```

2.  **Observation**:
    A Chrome browser window will open, navigate to FreeRice.com, and begin playing the English vocabulary game automatically. The terminal will display messages indicating the questions, API lookups, selected answers, and the current score.

3.  **Stopping the bot**:
    To stop the bot at any time, press `Ctrl+C` in your terminal. The script will print the final correct and incorrect answer counts before exiting.