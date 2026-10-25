import re

# User enters text containing email addresses
text = input("Enter text containing email addresses: ")

# Regex pattern for email matching
pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

# Find all email addresses
emails = re.findall(pattern, text)

# Display results
if emails:
    print("\nEmail addresses found:")
    for email in emails:
        print(email)
else:
    print("\nNo valid email addresses found.")