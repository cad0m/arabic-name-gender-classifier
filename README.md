# Arabic Names Gender Classifier

A simple Python tool to classify Arabic names as male or female, with CSV datasets included.

## Features

- Classify Arabic names by gender using reference CSV databases
- CSV files containing male and female Arabic names
- Add new Arabic names to the database through user input
- Analyze gender distribution in datasets with Arabic names

## Installation

```
git clone https://github.com/your-username/names_to_gender.git
pip install -r requirements.txt
```

## Usage

### Basic Classification

```python
from names_to_gender.gender import classify_gender

# Initialize the classifier
classifier = classify_gender()

# Classify a single Arabic name
gender = classifier.classify_names("Ahmed")
print(f"Gender: {gender}")  # Output: Gender: male

# Analyze gender distribution in a dataset with Arabic names
classifier.count_gender("path/to/your/dataset.csv")
```

### Classifying Unknown Arabic Names

```
python names_to_gender/handle_unknown_names/male_or_female.py
```

## Project Structure

```
names_to_gender/
├── gender.py                      # Main classification script
├── handle_unknown_names/
│   └── male_or_female.py          # Script to classify unknown names
└── names/
    ├── males_en.csv               # Database of male Arabic names
    ├── females_en.csv             # Database of female Arabic names
    └── unknown.csv                # Storage for unclassified names
```

## Contributing

Feel free to contribute by adding more Arabic names to the database or improving the classification algorithm.



## Keywords
arabic names, male arabic names, female arabic names, arabic names csv, gender classification, name gender, arabic names dataset
