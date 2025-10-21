import os
from julie_package.testalgo_julie import display_csv, filter_csv, drop_columns_csv
import pandas as pd

# Fichier fourni
input_file = "./cardata.csv"
print("===== ORIGINAL CSV =====")
display_csv(input_file, n=None)
display_csv(input_file, n=5) # affiche les 5 premières lignes

# Exemple de filtrage sur une colonne existante, ici Fuel_Type = 'Diesel'
output_file = "filtered_cardata.csv"
column_name = "Fuel_Type"
value = "Diesel"
filter_csv(input_file, output_file, column_name, value)
print("\n===== FILTERED CSV (Fuel_Type = Diesel) =====")
display_csv("filtered_cardata.csv")

# Exemple de suppression de colonnes existantes, ici 'Car_Name' et 'Engine'
output_file = "cleaned_cardata.csv"
columns_to_drop = ["Car_Name", "Kms_Driven"]
drop_columns_csv(input_file, output_file, columns_to_drop)

print("\n===== CSV APRÈS SUPPRESSION DE COLONNES =====")
display_csv(output_file)