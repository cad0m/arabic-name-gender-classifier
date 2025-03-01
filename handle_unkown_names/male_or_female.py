import csv
import os

def preprocess_unknown(file_path):
    """Remove duplicates and sort names in unknown.csv."""
    # Check if file exists, create if it doesn't
    if not os.path.exists(file_path):
        # Create directories if they don't exist
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as file:
            pass
        return
    
    try:
        with open(file_path, 'r') as file:
            names = sorted(set(name.strip() for name in file if name.strip()))
        with open(file_path, 'w') as file:
            file.write("\n".join(names))
    except Exception as e:
        print(f"Error preprocessing unknown names: {e}")

def classify_and_update(unknown_file, females_file, males_file):
    """Classify names as male or female and update respective files."""
    # Make sure all files exist
    for file_path in [unknown_file, females_file, males_file]:
        dir_path = os.path.dirname(file_path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path, exist_ok=True)
        if not os.path.exists(file_path):
            with open(file_path, 'w') as file:
                pass
    
    try:
        with open(unknown_file, 'r') as file:
            unknown_names = [line.strip() for line in file if line.strip()]
    except Exception as e:
        print(f"Error reading unknown file: {e}")
        return
    
    for name in unknown_names:
        while True:
            gender = input(f"Classify name '{name}' (m/f): ").strip().lower()
            if gender in ['m', 'f']:
                break
            print("Invalid input. Please enter 'm' or 'f'.")
        
        try:
            with open(females_file if gender == 'f' else males_file, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([name, "Female" if gender == 'f' else "Male"])
        except Exception as e:
            print(f"Error updating gender file: {e}")
    
    if input("Finished classifying all names? (yes/no): ").strip().lower() == 'yes':
        try:
            open(unknown_file, 'w').close()
        except Exception as e:
            print(f"Error clearing unknown file: {e}")

if __name__ == "__main__":
    unknown_path = "names_to_gender/names/unknown.csv"
    females_path = "names_to_gender/names/females_en.csv"
    males_path = "names_to_gender/names/males_en.csv"
    
    preprocess_unknown(unknown_path)
    classify_and_update(unknown_path, females_path, males_path)