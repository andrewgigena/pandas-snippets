import pandas as pd

# Loaded some addresses to test
df = pd.read_csv("01-normalize-column.csv")

# First, it converts into Unicode normal form for the column "addresses". 
# Then it encodes into ASCII, ignoring errors (non ASCII characters)
# Then it returns an standard python's UTF-8 string
df["addresses_norm"] = df['addresses'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode("utf-8")
