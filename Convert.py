from pathlib import Path
import os
import re
import pandas as pd

base_file_path = Path(r'C:\Users\g.drew\OneDrive - Medivant Health\Documents\Python_projects\source_files\outscraperMedSpa1.csv')
source_dir_path = Path(r'C:\Users\g.drew\Medivant Health\Medivant IT - Documents\Ketamine Customer List')
destination_path = Path(r'C:\Users\g.drew\OneDrive - Medivant Health\Documents\Python_projects\source_files\Finished_formatting')
read_file2 = pd.read_csv(base_file_path, encoding="ISO-8859-1", engine="python")

def DropCols(filepath):
    source_file_path = Path(filepath)
    file_path_split = re.split((r'[_]'), source_file_path.name)[1]
    print(file_path_split)
    file_path_split = file_path_split + '.xlsx'
    try: 
        pandas_file = pd.read_excel(source_file_path)
    except OSError as err:
        print('{}: is the error'.format(err))
    arr_to_drop = []

    for col in pandas_file.columns:
        if (col not in read_file2.columns):
            arr_to_drop.append(col)

    file_with_dropped = pandas_file.drop(arr_to_drop, axis=1)

    final_path = destination_path.joinpath(file_path_split)

    file_with_dropped.to_excel(final_path, index=False)

with os.scandir(source_dir_path) as ketfolder:
    for file in ketfolder:
        if file.is_file:
            DropCols(file.path)