import os
import re

dir_path = r'd:\PSO2ENPatchCSV\Translated'
pattern = re.compile(r'【\s*(.+?)\s*】')
replacement = r'【 \1 】'

count = 0
files_updated = 0

for root, _, files in os.walk(dir_path):
    for f in files:
        if f.endswith('.csv'):
            path = os.path.join(root, f)
            try:
                with open(path, 'r', encoding='utf-8') as file:
                    content = file.read()
            except UnicodeDecodeError:
                # Fallback to shift-jis or just skip
                try:
                    with open(path, 'r', encoding='utf-8-sig') as file:
                        content = file.read()
                except UnicodeDecodeError:
                    continue
            
            new_content = pattern.sub(replacement, content)
            
            if new_content != content:
                # Determine original encoding to save it correctly? 
                # Assuming utf-8 for now since it's CSV translation, but let's just write as utf-8.
                with open(path, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                print(f"Updated {f}")
                files_updated += 1
                
                # To count replacements roughly
                count += 1

print(f"Total files updated: {files_updated}")
