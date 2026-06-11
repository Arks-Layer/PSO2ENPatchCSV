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
        
        parts = line.split(',', 1)
        if len(parts) > 1:
            value = parts[1]
            
            # Count open and close tags for <c>
            open_c = len(re.findall(r'<c.*?>', value))
            close_c = len(re.findall(r'</c>', value))
            if open_c != close_c:
                issues.append(f"Line {i+1} has mismatched <c> tags: {open_c} open, {close_c} close")
                
            # Count open and close tags for <yellow> or similar if any, but usually it's just <c=something>
            # Check if there are malformed tags like < br> or < /c>
            if re.search(r'<\s+br>', value) or re.search(r'<\s+/c>', value):
                issues.append(f"Line {i+1} has malformed tags (contains spaces inside brackets)")
                
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
        print("All tags matched perfectly!")

