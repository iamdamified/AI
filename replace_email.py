# create program to find and replace all email address in a text using regex
import re
def replace_email_addresses(text, replacement="REDACTED"):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.sub(email_pattern, replacement, text)
input_text = "Please contact us at adekoyadamilareofficial@gmail.com for more information."
updated_text = replace_email_addresses(input_text)
print("Updated Text:", updated_text)
# Output: Updated Text: Please contact us at REDACTED for more information.
"""This module provides a function to find and replace all email addresses in a given text using regular expressions."""
