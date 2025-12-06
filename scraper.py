import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time

def getDefinition(questionWord, optionsElements):
    #Fetches definition and synonyms from Free Dictionary API.
    wordClean = questionWord.split()[0].lower()
    optionTexts = [opt.text.lower() for opt in optionsElements]
    print(f"Looking up API for: '{wordClean}'")
    knowledgeText = ""

    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{wordClean}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            # The API returns a list of "meanings". We want to grab all 
            # definitions and synonyms into one big text blob to check against.
            
            searchContent = ""
            for entry in data:
                for meaning in entry.get('meanings', []):
                    # Add definitions
                    for definition in meaning.get('definitions', []):
                        searchContent += definition.get('definition', '') + " "
                    # Add synonyms
                    searchContent += " ".join(meaning.get('synonyms', [])) + " "
            
            knowledgeText = searchContent.lower()
    except Exception as e:
        print(f"(API Error: {e})")
    
    if knowledgeText:
        for i, optText in enumerate(optionTexts):
            # Check if the option word exists inside the definition/synonyms
            if optText in knowledgeText:
                print(f"Match found in dictionary: '{optText}'")
                return i 
    else:
        print("Word not found in API search.")
    
    print("Guessing first option.")
    return 0

if __name__ == '__main__':
    # Start browser 
    driver = uc.Chrome(version_main=142) 

    correctCount = 0
    incorrectCount = 0
    
    try:
        #Navigate to page and handle banner if present
        driver.get("https://play.freerice.com/categories/english-vocabulary")
       
        try:
            print("Checking for cookie banner...")
            cookieButton = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
            )
            cookieButton.click()
            print("Cookie banner closed.")
        except:
            print("No cookie banner found (or already closed).")
        

        while True:
            # Wait for the question text to appear
            questionElement = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.CLASS_NAME, "card-title"))
            )
            
            # Find the option buttons
            options = driver.find_elements(By.CLASS_NAME, "card-button")
            
            if len(options) > 0:

                questionText = questionElement.text
                print(f"Question found: {questionText}")

                #Calling API to get definition of word
                targetIndex = getDefinition(questionText, options)

                selectedOption = options[targetIndex]
                print(f"Clicking option: {selectedOption.text}")
            
                #Clicking option 1 for now always
                driver.execute_script("arguments[0].click();", selectedOption)

                #Update score
                time.sleep(1)

                resultClasses = selectedOption.get_attribute("class")
                if "wrong" in resultClasses:
                    incorrectCount += 1
                    print(f"Result: WRONG (Total Wrong: {incorrectCount})")
                elif "correct" in resultClasses:
                    correctCount += 1
                    print(f"Result: CORRECT (Total Correct: {correctCount})")

            else:
                print("No options found!")
            
            # Wait a bit before next question
            time.sleep(4) 

    except KeyboardInterrupt:
        print("\nStopping bot...")
        print(f"Final Score - Correct: {correctCount}, Incorrect: {incorrectCount}")
        driver.quit()
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        driver.quit()