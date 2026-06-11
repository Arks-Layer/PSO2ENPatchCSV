import os
import sys
import re

def check_file(filepath):
    issues = []
    
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line: continue
        
        # Check for English characters (ignoring common tag words and IDs)
        # We split by comma to get the value part
        parts = line.split(',', 1)
        if len(parts) > 1:
            value = parts[1]
            
            # Remove tags like <br>, <c>...</c>
            text_without_tags = re.sub(r'<[^>]+>', '', value)
            
            # Search for English letters in the remaining text
            # We allow 'NPC' or specific English names if needed, but for now just list any matches
            english_chars = re.findall(r'[a-zA-Z]+', text_without_tags)
            if english_chars:
                issues.append(f"Line {i+1} might have untranslated text: {english_chars}")
                
            # Check for <br> command
            if '<br>' in value or '<br/>' in value or '<br />' in value:
                pass # valid, but check if there are odd spaces?
                
            # Check ODD strings in NPC names (e.g., name010#0)
            if parts[0].startswith('name'):
                if re.search(r'[^ก-๙a-zA-Z0-9\s"\'.,!-]', text_without_tags):
                    issues.append(f"Line {i+1} has odd characters in NPC name: {text_without_tags}")
                    
    return issues

if __name__ == "__main__":
    folder = sys.argv[1]
    all_clean = True
    for root, dirs, files in os.walk(folder):
        for f in files:
            if not f.endswith('.csv'): continue
            path = os.path.join(root, f)
            issues = check_file(path)
            if issues:
                all_clean = False
                print(f"File: {f}")
                for issue in issues:
                    print(f"  - {issue}")
    if all_clean:
        print("No English text or odd characters found!")

