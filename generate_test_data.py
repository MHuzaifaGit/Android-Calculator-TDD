#!/usr/bin/env python3
"""
Alternative approach: Manual form inspection and data generation.

This script helps you prepare test data that can be manually reviewed
before submission, or used with other automation tools.

Usage:
    python generate_test_data.py
"""

import json
import random
import csv


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

# Additional fields that might be in a form
INTERESTS = [
    "Programming", "Research", "Entrepreneurship", "Sports", "Music",
    "Reading", "Gaming", "Volunteering", "Photography", "Writing"
]

CAREER_GOALS = [
    "Software Engineer at a tech company",
    "Data Scientist",
    "Research Scientist",
    "Entrepreneur / Startup Founder",
    "Product Manager",
    "University Professor",
    "Consultant",
    "Government Service",
    "NGO / Non-profit work",
    "Freelancer / Independent Professional"
]

FEEDBACK_TEMPLATES = [
    "This is a test response from {name}. As a {year} {major} student at {university}, I am {personality}.",
    "Test submission by {name}. Currently studying {major} at {university} in {city}. My personality type is {personality}.",
    "Sample data for testing: {name}, {university}, {major}, {personality}.",
    "Testing form with profile: {name} - {year} student focusing on {major} at {university}.",
]


def generate_dummy_student(index):
    """Generate a dummy student profile with more details."""
    name = f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}"
    university = random.choice(PAKISTANI_UNIVERSITIES)
    city = random.choice(PAKISTANI_CITIES)
    major = random.choice(MAJORS)
    year = random.choice(YEARS)
    personality = random.choice(PERSONALITIES)
    
    # Generate email (test email)
    email = f"test{index}@example.com"
    
    # Generate random interests (2-4 interests)
    num_interests = random.randint(2, 4)
    interests = random.sample(INTERESTS, num_interests)
    
    # Other fields
    career_goal = random.choice(CAREER_GOALS)
    age = random.randint(18, 25)
    
    # Generate a feedback text using templates
    feedback_template = random.choice(FEEDBACK_TEMPLATES)
    feedback = feedback_template.format(
        name=name,
        year=year,
        major=major,
        university=university,
        city=city,
        personality=personality
    )
    
    return {
        "id": index,
        "name": name,
        "email": email,
        "university": university,
        "city": city,
        "major": major,
        "year": year,
        "age": age,
        "personality": personality,
        "interests": ", ".join(interests),
        "career_goal": career_goal,
        "feedback": feedback,
    }


def save_as_json(students, filename="test_students.json"):
    """Save student data as JSON."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(students, f, indent=2, ensure_ascii=False)
    print(f"✓ Saved {len(students)} student profiles to {filename}")


def save_as_csv(students, filename="test_students.csv"):
    """Save student data as CSV."""
    if not students:
        return
    
    fieldnames = students[0].keys()
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)
    print(f"✓ Saved {len(students)} student profiles to {filename}")


def print_student_summary(student):
    """Print a formatted summary of a student profile."""
    print(f"\n{'='*60}")
    print(f"Student #{student['id']}")
    print(f"{'='*60}")
    print(f"Name:          {student['name']}")
    print(f"Email:         {student['email']}")
    print(f"University:    {student['university']}")
    print(f"City:          {student['city']}")
    print(f"Major:         {student['major']}")
    print(f"Year:          {student['year']}")
    print(f"Age:           {student['age']}")
    print(f"Personality:   {student['personality']}")
    print(f"Interests:     {student['interests']}")
    print(f"Career Goal:   {student['career_goal']}")
    print(f"Feedback:      {student['feedback']}")


def main():
    """Generate test data for form submissions."""
    print("=" * 70)
    print("Google Form Test Data Generator")
    print("=" * 70)
    print("\nThis script generates dummy data for testing your Google Form.")
    print("The data represents Pakistani university students with different")
    print("personalities and backgrounds.\n")
    
    num_students = 20
    print(f"Generating {num_students} student profiles...\n")
    
    students = []
    for i in range(1, num_students + 1):
        student = generate_dummy_student(i)
        students.append(student)
        
        # Print first 3 examples
        if i <= 3:
            print_student_summary(student)
    
    print(f"\n{'='*70}")
    print(f"Generated {len(students)} total profiles")
    print(f"{'='*70}\n")
    
    # Save to files
    save_as_json(students)
    save_as_csv(students)
    
    print("\n" + "="*70)
    print("Files created:")
    print("  - test_students.json (JSON format)")
    print("  - test_students.csv  (CSV format for Excel)")
    print("="*70)
    print("\nYou can now:")
    print("  1. Review the generated data")
    print("  2. Customize the data in the JSON/CSV files")
    print("  3. Use the data with the form_automation_test.py script")
    print("  4. Manually copy data from CSV to test your form")
    print("="*70)


if __name__ == "__main__":
    main()
