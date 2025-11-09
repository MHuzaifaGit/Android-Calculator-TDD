# Form Automation Test Script

## Overview
This script helps you test your own Google Form by automatically filling it with dummy data representing different Pakistani university student personalities.

## ⚠️ Important Notes
- **Use this script ONLY on your own forms**
- This is for testing purposes only
- Respect rate limits and don't overload the form
- Review Google Forms Terms of Service

## Prerequisites

### 1. Install Python 3.7 or higher
```bash
python3 --version
```

### 2. Install Required Dependencies
```bash
pip install selenium webdriver-manager
```

## Setup Instructions

### Step 1: Inspect Your Form
Before running the script, you need to customize it for your specific form structure:

1. Open your Google Form in a web browser
2. Right-click and select "Inspect" or press F12 to open Developer Tools
3. Navigate to the "Elements" or "Inspector" tab
4. Identify the HTML elements for each form field you want to fill

### Step 2: Update Field Selectors
Open `form_automation_test.py` and locate the `fill_form()` function. You'll see commented examples like:

```python
# Example: Find all text input fields
# text_fields = wait.until(
#     EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input[type='text']"))
# )
```

Update these selectors based on your form's HTML structure. Common selectors:

- Text inputs: `input[type='text']`
- Text areas: `textarea`
- Radio buttons: `input[type='radio']`
- Checkboxes: `input[type='checkbox']`
- Dropdowns: `select` or `div[role='listbox']`

### Step 3: Customize Student Data
Edit the data arrays in the script to match your testing needs:
- `PAKISTANI_UNIVERSITIES`: List of universities
- `PAKISTANI_CITIES`: List of cities
- `FIRST_NAMES`, `LAST_NAMES`: Names for student profiles
- `PERSONALITIES`: Different personality types
- `MAJORS`: Academic majors
- `YEARS`: Year levels

## Usage

### Run the Script
```bash
python3 form_automation_test.py
```

The script will:
1. Show configuration details
2. Ask for confirmation
3. Generate 20 unique student profiles
4. Fill and submit the form for each profile
5. Add random delays between submissions (3-7 seconds)
6. Display progress and results

### Run in Headless Mode
To run without opening a browser window, uncomment this line in the `setup_driver()` function:
```python
chrome_options.add_argument("--headless")
```

## Customization

### Change Number of Submissions
Edit the constant at the top of the script:
```python
NUM_SUBMISSIONS = 20  # Change to desired number
```

### Adjust Delays
Modify the delay between submissions in the `main()` function:
```python
delay = random.randint(3, 7)  # Adjust min and max seconds
```

## Example Student Profile
The script generates profiles like:
```
Name: Fatima Khan
University: National University of Sciences and Technology (NUST)
City: Islamabad
Major: Computer Science
Year: 3rd Year
Age: 21
Personality: analytical and detail-oriented
```

## Troubleshooting

### ChromeDriver Issues
If you encounter ChromeDriver issues:
```bash
# Update webdriver-manager
pip install --upgrade webdriver-manager

# Or manually download ChromeDriver matching your Chrome version
```

### Form Not Loading
- Check your internet connection
- Verify the form URL is correct
- Ensure the form is publicly accessible

### Fields Not Filling
- Inspect the form HTML to verify selectors
- Check for dynamic content loading (may need additional waits)
- Look for CAPTCHAs or other anti-automation measures

### Rate Limiting
If submissions are being rejected:
- Increase delays between submissions
- Reduce the number of submissions
- Check if Google Forms has flagged the activity

## Ethical Considerations

✅ **Appropriate Use:**
- Testing your own forms
- Generating test data for development
- Quality assurance of form functionality

❌ **Inappropriate Use:**
- Manipulating surveys or polls you don't own
- Spamming forms
- Bypassing form restrictions
- Creating fake responses for others' research

## Technical Details

### Dependencies
- **selenium**: Web browser automation
- **webdriver-manager**: Automatic ChromeDriver management

### Browsers Supported
- Google Chrome (default)
- Can be adapted for Firefox, Edge, etc.

## License
This script is provided as-is for testing purposes. Use responsibly and in accordance with all applicable terms of service.

## Support
If you encounter issues:
1. Check that all field selectors are correct
2. Verify dependencies are installed
3. Ensure Chrome browser is up to date
4. Review error messages for specific issues

## Next Steps
1. ✅ Install dependencies
2. ✅ Inspect your form structure
3. ✅ Customize field selectors
4. ✅ Update test data as needed
5. ✅ Run a test with 1-2 submissions first
6. ✅ Scale up to full test run
