import os
import codecs
import re
import sys

file_path = sys.argv[1] if len(sys.argv) > 1 else r'Quest/ui_quest_reb.csv'

def validate_csv(path):
    print(f"Validating {path}...")
    
    # 1. Check Encoding
    has_bom = False
    try:
        with open(path, 'rb') as f:
            raw = f.read(4)
        if raw.startswith(codecs.BOM_UTF8):
            has_bom = True
            print("  [WARN] File has UTF-8 BOM. (Game might require No BOM)")
        else:
            print("  [OK] File is UTF-8 (No BOM).")
            
    except Exception as e:
        print(f"  [Error] Could not read file info: {e}")
        return

    # 2. Check Content (Duplicates & Syntax)
    # We read with utf-8-sig to handle reading cleanly even if BOM exists
    try:
        with open(path, 'r', encoding='utf-8-sig') as f:
            content = f.read()
    except UnicodeDecodeError:
        print("  [Error] Unicode Decode Error! File might be CP949 or other.")
        return

    lines = content.splitlines()
    keys = {}
    duplicates = 0
    syntax_errors = 0
    
    for i, line in enumerate(lines):
        line_num = i + 1
        if not line.strip(): continue
        
        # Check basic csv structure: Key,"""Value"""
        # Regex for Key,"""..."""
        # Or simple split
        if ',"""' in line:
            parts = line.split(',"""', 1)
            key = parts[0]
            val = parts[1]
            
            # Check duplicate key
            if key in keys:
                print(f"  [WARN] Duplicate Key on line {line_num}: {key} (Previous at {keys[key]})")
                duplicates += 1
            else:
                keys[key] = line_num
                
            # Check value end
            if not val.strip().endswith('"""'):
                print(f"  [WARN] Syntax Error on line {line_num}: Does not end with \"\"\"")
                syntax_errors += 1
            else:
                inner = val.strip()[:-3] # remove trailing """
                # Check for unescaped quotes inside
                # We expect \" or \"" depending on standard.
                # If we see " not preceded by \
                # But wait, \\" is valid literal backslash quote?
                # Let's simple check: " preceded by not-\
                
                idx = 0
                while idx < len(inner):
                    if inner[idx] == '"':
                        # Valid patterns: \", or the second quote of \""
                        is_escaped = False
                        if idx > 0 and inner[idx-1] == '\\':
                            is_escaped = True
                        elif idx > 1 and inner[idx-2:idx] == '\\"':
                            is_escaped = True
                            
                        if not is_escaped:
                             print(f"  [WARN] Potential Unescaped Quote on line {line_num} at pos {idx}")
                             syntax_errors += 1
                    idx += 1
        else:
             # Maybe a comment or invalid line?
             # csv usually works line by line but description fields can have newlines?
             # If dictionary csv, it's strictly one line per entry usually.
             print(f"  [INFO] Line {line_num} does not match standard pattern: {line[:40]}...")

    print(f"Validation Complete.")
    print(f"  Duplicates: {duplicates}")
    print(f"  Syntax Issues: {syntax_errors}")

if __name__ == "__main__":
    if os.path.exists(file_path):
        validate_csv(file_path)
    else:
        print(f"File not found: {file_path}")
