import os
import re

work_dir = r'c:\Users\focus\Documents\GitHub\PSO2ENPatchCSV\work'

def analyze_commas(directory):
    total_lines = 0
    total_commas = 0
    comma_lines = 0
    
    print(f"Analyzing {directory}...")
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.csv'):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                except:
                    with open(filepath, 'r', encoding='cp949') as f:
                        lines = f.readlines()
                
                for line in lines:
                    # Ignore internal CSV format commas (separator) if possible, but these files are usually quoted strings.
                    # We usually look for commas inside the message body.
                    # Pattern: "message" or """message"""
                    # Simplified: just count commas in the whole line for relative comparison, 
                    # OR try to extract the text part.
                    
                    # Extract text content inside quotes if possible
                    matches = re.findall(r'"""(.*?)"""', line, re.DOTALL)
                    if not matches:
                        matches = re.findall(r'"(.*?)"', line)
                    
                    content = " ".join(matches) if matches else line
                    
                    cnt = content.count(',')
                    if cnt > 0:
                        total_commas += cnt
                        comma_lines += 1
                        # Print sample if high density
                        if cnt > 2 and total_lines < 1000: # Sampling
                             pass
                             # print(f"Sample ({cnt}): {content.strip()[:50]}...")
                    
                    total_lines += 1

    print(f"Total Lines: {total_lines}")
    print(f"Lines with Commas: {comma_lines} ({comma_lines/total_lines*100:.1f}%)")
    print(f"Total Commas: {total_commas}")
    print(f"Avg Commas per Line: {total_commas/total_lines:.2f}")

analyze_commas(work_dir)
analyze_commas(r'c:\Users\focus\Documents\GitHub\PSO2ENPatchCSV\UI')
analyze_commas(r'c:\Users\focus\Documents\GitHub\PSO2ENPatchCSV\Linestrike')
