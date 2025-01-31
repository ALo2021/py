# Assuming the input dataset is 'dataset'
import pandas as pd

dataset = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35], 'Score': [85, 90, 95]}

# Convert all column names to lowercase
dataset.columns = [col.lower() for col in dataset.columns]

# Add a calculated column
dataset['score_category'] = dataset['score'].apply(lambda x: 'High' if x > 90 else 'Low')
