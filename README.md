# Arabic Name Gender Classifier

A simple Python tool to classify Arabic names as male or female. This project can be used to analyze gender distribution in datasets containing Arabic names.

## Features

- Classify names as male or female based on reference lists
- Add new names to the reference lists
- Handle unknown names by logging them for future classification
- Analyze gender distribution in datasets

## Project Structure

```
names_to_gender/
├── gender.py              # Main classification script
├── handle_unknown_names/
│   └── male_or_female.py  # Interactive script to classify unknown names
└── names/
    ├── males_en.csv       # Database of male names
    ├── females_en.csv     # Database of female names
    └── unknown.csv        # Storage for unclassified names
```

## Installation

1. Clone this repository:
```
git clone https://github.com/your-username/names_to_gender.git
```

2. Install the required dependencies:
```
pip install -r requirements.txt
```

## Usage

### Basic Classification

```python
from names_to_gender.gender import classify_gender

# Initialize the classifier
classifier = classify_gender()

# Classify a single name
gender = classifier.classify_names("Ahmed")
print(f"Gender: {gender}")  # Output: Gender: male

# Analyze gender distribution in a dataset
classifier.count_gender("path/to/your/dataset.csv")
```

### Interactive Classification of Unknown Names

Run the following script to classify unknown names and update the reference lists:

```
python names_to_gender/handle_unknown_names/male_or_female.py
```

## Input Data Format

The input CSV file for gender analysis should have a column named `PRENOM` containing the first names to be classified.

## Contributing

Feel free to fork this repository and submit pull requests to improve the classifier or add new features!

Suggestions for improvements:
- Add more sophisticated name analysis (e.g., based on name endings)
- Implement machine learning techniques for name classification
- Add support for other languages and name formats
- Create a simple web interface
