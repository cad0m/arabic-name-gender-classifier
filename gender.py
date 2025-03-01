import csv
import pandas as pd
import os

class classify_gender:
    def __init__(self):
        # Create the directory structure if it doesn't exist
        if not os.path.exists('names_to_gender/names'):
            os.makedirs('names_to_gender/names')
            
        self.males_names = []
        self.females_names = []
        
        # Check if files exist before opening
        males_path = 'names_to_gender/names/males_en.csv'
        females_path = 'names_to_gender/names/females_en.csv'
        
        if os.path.exists(males_path):
            try:
                with open(males_path, 'r') as file:
                    males_reader = file.readlines()
                    for line in males_reader:
                        self.males_names.append(line.split(',')[0].lower())
            except Exception as e:
                print(f"Error reading males file: {e}")
        else:
            # Create empty file if it doesn't exist
            with open(males_path, 'w') as file:
                pass
                
        if os.path.exists(females_path):
            try:
                with open(females_path, 'r') as file:
                    females_reader = file.readlines()
                    for line in females_reader:
                        self.females_names.append(line.split(',')[0].lower())
            except Exception as e:
                print(f"Error reading females file: {e}")
        else:
            # Create empty file if it doesn't exist
            with open(females_path, 'w') as file:
                pass
    
    def add_males_name(self,first_name):
        if first_name not in self.males_names:
            self.males_names.append(first_name.lower())
            # Update the CSV file with the new name
            try:
                with open('names_to_gender/names/males_en.csv', 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([first_name.lower(), "Male"])
            except Exception as e:
                print(f"Error adding male name: {e}")
        else:
            print(f"{first_name} already exists in the male list")
    
    def add_females_name(self,first_name):
        if first_name not in self.females_names:
            self.females_names.append(first_name.lower())
            # Update the CSV file with the new name
            try:
                with open('names_to_gender/names/females_en.csv', 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([first_name.lower(), "Female"])
            except Exception as e:
                print(f"Error adding female name: {e}")
        else:
            print(f"{first_name} already exists in the female list")
    
    def classify_names(self,first_name):
        if first_name.lower() in self.males_names:
            return 'male'
        elif first_name.lower() in self.females_names:
            return 'female'
        else:
            # Make sure the unknown.csv file exists
            unknown_path = "names_to_gender/names/unknown.csv"
            if not os.path.exists(os.path.dirname(unknown_path)):
                os.makedirs(os.path.dirname(unknown_path))
                
            try:
                with open(unknown_path, "a", newline='\n') as file:
                    writer = csv.writer(file)
                    writer.writerow([str(first_name).lower()])
            except Exception as e:
                print(f"Error writing to unknown.csv: {e}")
            return 'unknown'
    
    def count_gender(self, file_path='csv_merged_cleaned/Mip_S1.csv'):
        try:
            df = pd.read_csv(file_path, index_col=False)
            df['Gender'] = df['PRENOM'].apply(self.classify_names)
            gender_counts = df['Gender'].value_counts()
            
            print(f"Gender Distribution in {os.path.basename(file_path)}:")
            print(gender_counts)
            
        except Exception as e:
            print(f"An error occurred: {e}")