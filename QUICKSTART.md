# Quick Start Guide

## For Testing Your Google Form with Dummy Data

### Option 1: Generate Test Data Only (Recommended First Step)

This creates JSON and CSV files with 20 student profiles that you can review:

```bash
# No installation needed for this option
python3 generate_test_data.py
```

Output files:
- `test_students.json` - JSON format with all student data
- `test_students.csv` - CSV format (opens in Excel/Sheets)

### Option 2: Full Browser Automation

This automatically fills and submits your form 20 times:

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Edit form_automation_test.py
#    - Inspect your form to get field selectors
#    - Update the fill_form() function with your selectors

# 3. Run the script
python3 form_automation_test.py
```

## What You Get

Each generated student profile includes:
- ✅ Full name (Pakistani names)
- ✅ University (10 major Pakistani universities)
- ✅ City (10 Pakistani cities)
- ✅ Major/Field of study
- ✅ Year level (1st to Final year)
- ✅ Age (18-25)
- ✅ Personality type (10 different types)
- ✅ Interests
- ✅ Career goals
- ✅ Feedback text

## Need Help?

See `FORM_TEST_README.md` for detailed instructions and troubleshooting.

## Important Notes

⚠️ **Before Running Automation:**
1. This script is for testing YOUR OWN forms only
2. You must customize field selectors in the script
3. Test with 1-2 submissions first
4. Respect rate limits (delays are built-in)

## Example Generated Profile

```
Name:          Fatima Khan
Email:         test1@example.com
University:    LUMS
City:          Islamabad
Major:         Computer Science
Year:          3rd Year
Age:           21
Personality:   analytical and detail-oriented
Interests:     Programming, Research
Career Goal:   Software Engineer at a tech company
```
