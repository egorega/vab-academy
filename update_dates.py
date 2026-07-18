import os

dates = {
    "1": "18 Июля",
    "2": "19 Июля",
    "3": "20 Июля",
    "4": "21 Июля",
    "5": "22 Июля",
    "6": "23 Июля",
    "7": "24 Июля",
}

base_dir = r"C:\Users\jejeb\.gemini\antigravity\scratch\vab-academy\Curriculum"

for root, _, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".md"):
            filepath = os.path.join(root, file)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            
            lines = content.split('\n')
            if lines and lines[0].startswith("# День "):
                header = lines[0]
                try:
                    day_part = header.split("День ")[1]
                    day_num_str = day_part.split(":")[0].strip()
                    
                    if day_num_str in dates:
                        date_str = dates[day_num_str]
                        # Check if the date is already in the header
                        if date_str not in header:
                            new_header = header.replace(f"День {day_num_str}:", f"День {day_num_str} ({date_str}):")
                            lines[0] = new_header
                            
                            with open(filepath, "w", encoding="utf-8") as f:
                                f.write('\n'.join(lines))
                            print(f"Updated {file}")
                except Exception as e:
                    print(f"Error on {file}: {e}")
