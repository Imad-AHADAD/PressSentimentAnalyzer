import re

def cleanText(text, num_page):
    # Split the text into lines
    lines = text.split('\n')
    
    # Define a regular expression pattern to match "Page xx" or "x"
    page_pattern = re.compile(r'^Page [0-9]{2}$|^[0-9]{2}$')
    
    # Create a list to store lines that should be kept
    cleaned_lines = []
    
    for line in lines:
        if not page_pattern.match(line):
            cleaned_lines.append(line.strip())
    
    # Join the cleaned lines back into text
    cleaned_text = "\n".join(cleaned_lines)
    
    # Remove line breaks after '.' or if the next word starts with lowercase
    cleaned_text = re.sub(r'\n(?=[.]|[a-z])', ' ', cleaned_text)
    
    return f"Page {num_page+1} : \n" + cleaned_text + '\n\n'




def contains_arabic_letter(word):
    arabic_letters = [
        "ا", "ب", "ت", "ث", "ج", "ح", "خ", "د", "ذ", "ر", "ز", "س",
        "ش", "ص", "ض", "ط", "ظ", "ع", "غ", "ف", "ق", "ك", "ل", "م",
        "ن", "ه", "و", "ي"
    ]

    for letter in arabic_letters:
        if letter in word:
            return True
        
    return False

