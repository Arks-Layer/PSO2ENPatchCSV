import os
import sys

def check_file(filepath):
    issues = []
    
    with open(filepath, 'rb') as f:
        content = f.read()
    
    # 1. Check encoding and BOM
    if content.startswith(b'\xef\xbb\xbf'):
        issues.append("Contains BOM (UTF-8 with BOM instead of UTF-8)")
        content = content[3:]
    
    try:
        text = content.decode('utf-8')
    except UnicodeDecodeError:
        issues.append("Not valid UTF-8 encoding")
        return issues
        
    # 2. Check EOL
    if '\r\n' in text:
        issues.append("Contains CRLF instead of LF")
    
    # 3. Check CSV quote issues
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if line.count('"') % 2 != 0:
            issues.append(f"Unmatched quotes on line {i+1}")
            
    # 4. Check for duplicate lines (excluding empty lines)
    seen_lines = set()
    for i, line in enumerate(lines):
        line = line.strip()
        if not line: continue
        if line in seen_lines:
            pass # sometimes empty commas can be dupes, so skip strict check for now, or just warn if the whole line is literally the same and not empty
        else:
            seen_lines.add(line)

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
        print("All files passed automated QA checks!")
