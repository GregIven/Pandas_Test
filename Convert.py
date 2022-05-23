from pathlib import Path
import os
import pandas as pd

base_file_path = Path(r'C:\Users\g.drew\OneDrive - Medivant Health\Documents\Python_projects\source_files\outscraperMedSpa1.csv')
source_dir_path = Path(r'C:\Users\g.drew\Medivant Health\Medivant IT - Documents\Ketamine Customer List')
read_file2 = pd.read_csv(base_file_path, encoding="ISO-8859-1", engine="python")


def DropCols(filepath):
    source_file_path = Path(filepath)
    print(source_file_path)
    try: 
        pandas_file = pd.read_excel(source_file_path)
    except OSError as err:
        print('{}: is the error'.format(err))
    arr_to_drop = []

    for col in pandas_file.columns:
        if (col not in read_file2.columns):
            arr_to_drop.append(col)

    file_with_dropped = pandas_file.drop(arr_to_drop, axis=1)

    if (file_with_dropped.size > 0):
        print('dropped! {}'.format(file_with_dropped.head(1)))

with os.scandir(source_dir_path) as ketfolder:
    for file in ketfolder:
        item = next(ketfolder)
        DropCols(item.path)



# print(arr_to_drop)


# print(read_file.head())
# print(read_file.index)
# print(read_file.columns)    

# print(read_file2.columns)

# print(file_with_dropped.columns)
# file_with_dropped.to_csv(r'C:\Users\g.drew\OneDrive - Medivant Health\Documents\Python_projects\source_files\Finished_formatting\')
