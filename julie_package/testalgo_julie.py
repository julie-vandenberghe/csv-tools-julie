import pandas as pd

def display_csv(file_path: str, n=None) -> None:
    """
    Affiche le contenu d'un CSV dans le terminal.
    Si n est None, affiche tout, sinon les n premières lignes.
    """
    df = pd.read_csv(file_path, sep=';')
    df.columns = df.columns.str.strip()
    
    if n is None:
        print(df)
    else:
        print(df.head(n))

def filter_csv(input_file: str, output_file: str, column_name: str, value) -> None:
    """
    Filtre les lignes du CSV où la colonne `column_name` a la valeur `value`
    et écrit le résultat dans `output_file`.
    """
    df = pd.read_csv(input_file, sep=';') # Lecture du CSV
    filtered_df = df[df[column_name] == value] # Filtre sur la colonne qui a la valeur value
    filtered_df.to_csv(output_file, index=False, sep=';') # Écriture du CSV modifié

def drop_columns_csv(input_file: str, output_file: str, columns_to_drop: list) -> None:
    """
    Supprime les colonnes listées dans `columns_to_drop` du CSV `input_file`
    et écrit le résultat dans `output_file`.
    
    Parameters:
    - input_file : str : chemin du fichier CSV d'entrée
    - output_file : str : chemin du fichier CSV de sortie
    - columns_to_drop : list : liste des noms de colonnes à supprimer
    """
    
    df = pd.read_csv(input_file, sep=';') # Lecture du CSV
    df = df.drop(columns=columns_to_drop) # Suppression des colonnes
    df.to_csv(output_file, index=False, sep=';') # Écriture du CSV modifié
