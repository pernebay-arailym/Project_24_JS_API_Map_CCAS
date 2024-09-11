import pandas as pd

# Load the Excel file
excel_file = 'Maps_CCAS.xlsx'  # Replace this with your actual file path
  # Replace this with your actual sheet name if necessary

# Read the Excel sheet
df = pd.read_excel(excel_file)


# Iterate over the rows and convert them to the desired format
locations = []

for _, row in df.iterrows():
    location = {
        'lat': row['latitude'],
        'lng': row['longitude'],
        'bailleur': row['Bailleur social'],
        'nom': row['Nom de l\'immeuble'],
        'adresse': row['Address'],
        'logements': row['Numero de logements']
    }
    locations.append(location)

# Print the locations as JavaScript code
print(f"const locations = {locations};")
