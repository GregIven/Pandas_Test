from pathlib import Path
import os
import pandas as pd

base_file_path = Path(r'C:\Users\g.drew\OneDrive - Medivant Health\Documents\Python_projects\source_files\outscraperMedSpa1.csv')
source_dir_path = Path(r'C:\Users\g.drew\Medivant Health\Medivant IT - Documents\Ketamine Customer List')

with os.scandir(source_dir_path) as ketfolder:
    for file in ketfolder:
        print(file.name)


read_file = pd.read_excel(r'C:\Users\g.drew\OneDrive - Medivant Health\Documents\Python_projects\source_files\ketamine_sources\ketamine-ar_FORMATTED.xlsx')
read_file2 = pd.read_csv(base_file_path, encoding="ISO-8859-1", engine="python")

arr_to_drop = []

for col in read_file.columns:
    if (col not in read_file2.columns):
        arr_to_drop.append(col)

# print(arr_to_drop)

file_with_dropped = read_file.drop(arr_to_drop, axis=1)

# print(read_file.head())
# print(read_file.index)
# print(read_file.columns)    

# print(read_file2.columns)

# print(file_with_dropped.columns)
# file_with_dropped.to_csv(r'C:\Users\g.drew\OneDrive - Medivant Health\Documents\Python_projects\source_files\Finished_formatting\')
