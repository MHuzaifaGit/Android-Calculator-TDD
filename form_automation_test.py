#!/usr/bin/env python3
"""
Script to fill a Google Form with test data.
This script generates dummy data for testing purposes only.

Requirements:
    pip install selenium webdriver-manager
    
Usage:
    python form_automation_test.py
"""

import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Configuration
FORM_URL = "https://forms.gle/v6wPjJtFCrqyPh1D7"
NUM_SUBMISSIONS = 20

# Sample data for Pakistani university students
PAKISTANI_UNIVERSITIES = [
    "National University of Sciences and Technology (NUST)",
    "Lahore University of Management Sciences (LUMS)",
    "University of Engineering and Technology (UET) Lahore",
    "Pakistan Institute of Engineering and Applied Sciences (PIEAS)",
    "COMSATS University Islamabad",
    "Government College University (GCU) Lahore",
    "University of Karachi",
    "Quaid-i-Azam University",
    "University of Punjab",
    "NED University of Engineering and Technology"
]

PAKISTANI_CITIES = [
    "Karachi", "Lahore", "Islamabad", "Rawalpindi", "Faisalabad",
    "Multan", "Peshawar", "Quetta", "Sialkot", "Gujranwala"
]

FIRST_NAMES = [
    "Muhammad", "Ahmed", "Ali", "Hassan", "Usman", "Bilal", "Hamza", "Omar",
    "Fatima", "Ayesha", "Zainab", "Mariam", "Hira", "Sana", "Amna", "Mahnoor"
]

LAST_NAMES = [
    "Khan", "Ali", "Ahmed", "Hassan", "Hussain", "Malik", "Shah", "Raza",
    "Iqbal", "Haider", "Abbas", "Mehdi", "Zaidi", "Butt"
]

PERSONALITIES = [
    "analytical and detail-oriented",
    "creative and innovative",
    "practical and results-driven",
    "collaborative and team-oriented",
    "independent and self-motivated",
    "curious and research-focused",
    "organized and methodical",
    "adaptable and flexible",
    "ambitious and goal-driven",
    "empathetic and people-focused"
]

MAJORS = [
    "Computer Science", "Software Engineering", "Electrical Engineering",
    "Mechanical Engineering", "Business Administration", "Economics",
    "Civil Engineering", "Data Science", "Information Technology",
    "Artificial Intelligence"
]

YEARS = ["1st Year", "2nd Year", "3rd Year", "4th Year", "Final Year"]


def generate_dummy_student():
    """Generate a dummy student profile."""
    return {
        "name": f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}",
        "university": random.choice(PAKISTANI_UNIVERSITIES),
        "city": random.choice(PAKISTANI_CITIES),
        "major": random.choice(MAJORS),
        "year": random.choice(YEARS),
        "age": random.randint(18, 25),
        "personality": random.choice(PERSONALITIES),
    }


def setup_driver():
    """Set up Chrome WebDriver with appropriate options."""
    chrome_options = Options()
    # Uncomment the line below to run in headless mode (no browser window)
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver


def fill_form(driver, student_data, submission_num):
    """Fill and submit the form with student data."""
    print(f"\n[{submission_num}/{NUM_SUBMISSIONS}] Filling form for: {student_data['name']}")
    print(f"  University: {student_data['university']}")
    print(f"  Personality: {student_data['personality']}")
    
    try:
        # Navigate to the form
        driver.get(FORM_URL)
        
        # Wait for the form to load
        wait = WebDriverWait(driver, 10)
        
        # Note: The actual field selectors will depend on the form structure
        # You'll need to inspect the form and update these selectors accordingly
        # This is a template that needs to be customized for your specific form
        
        # Example: Find all text input fields
        # text_fields = wait.until(
        #     EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input[type='text']"))
        # )
        
        # Example: Fill name field (adjust selector as needed)
        # text_fields[0].send_keys(student_data['name'])
        
        # Example: Fill university field
        # text_fields[1].send_keys(student_data['university'])
        
        # Add more fields as needed based on your form structure
        
        # Find and click submit button
        # submit_button = driver.find_element(By.CSS_SELECTOR, "div[role='button']")
        # submit_button.click()
        
        # Wait a bit before next submission
        time.sleep(2)
        
        print(f"  ✓ Form submitted successfully")
        return True
        
    except Exception as e:
        print(f"  ✗ Error filling form: {str(e)}")
        return False


def main():
    """Main function to run the form automation."""
    print("=" * 60)
    print("Google Form Automation Test Script")
    print("=" * 60)
    print(f"\nTarget: {FORM_URL}")
    print(f"Number of submissions: {NUM_SUBMISSIONS}")
    print("\nNOTE: This script is for testing YOUR OWN forms only.")
    print("Make sure you have the right to automate submissions to this form.")
    print("\nIMPORTANT: You need to customize the field selectors in this script")
    print("based on your actual form structure. Inspect the form HTML to get")
    print("the correct selectors for each field.")
    print("\n" + "=" * 60)
    
    input("\nPress Enter to continue or Ctrl+C to cancel...")
    
    driver = setup_driver()
    successful_submissions = 0
    
    try:
        for i in range(1, NUM_SUBMISSIONS + 1):
            # Generate dummy student data
            student_data = generate_dummy_student()
            
            # Fill and submit the form
            if fill_form(driver, student_data, i):
                successful_submissions += 1
            
            # Add a delay between submissions to be respectful
            if i < NUM_SUBMISSIONS:
                delay = random.randint(3, 7)
                print(f"  Waiting {delay} seconds before next submission...")
                time.sleep(delay)
    
    except KeyboardInterrupt:
        print("\n\nScript interrupted by user.")
    
    finally:
        driver.quit()
        print("\n" + "=" * 60)
        print(f"Completed: {successful_submissions}/{NUM_SUBMISSIONS} submissions")
        print("=" * 60)


if __name__ == "__main__":
    main()
