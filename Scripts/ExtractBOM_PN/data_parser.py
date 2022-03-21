import csv

#IN (ID as dict key):
#Desc, Type, UOM, RefSupplier, RefUrl, RefMgr, RefMgrPart, Notes
#OUT:
#ID, Desc, Type, UOM, Count, RefSupplier, RefUrl, RefMfgr, RefMfgrPart, Notes

class ImportError(Exception):
    pass

class ExportError(Exception):
    pass

def import_source_data(filepath: str = None) -> dict:
    result = {}
    try:
        with open(filepath, 'r', newline='') as datafile:
            fieldnames=('ID', 'Type', 'Description', 'UOM', 'DefaultValue', 'RefSupplier', 'RefUrl', 'RefMfgr', 'RefMfgrPN', 'Notes')
            reader = csv.DictReader(datafile, fieldnames=fieldnames, dialect='excel')
            for row in reader:
                result[row['ID']] = {
                    'Type': row['Type'],
                    'Description': row['Description'],
                    'UOM': row['UOM'],
                    'Value': 0, #note that this is not not DefaultValue
                    'RefSupplier': row['RefSupplier'],
                    'RefUrl': row['RefUrl'],
                    'RefMfgr': row['RefMfgr'],
                    'RefMfgrPN': row['RefMfgrPN'],
                    'Notes': row['Notes']
                }
                if row['DefaultValue'] is not None and row['DefaultValue'].isnumeric():
                    result[row['ID']]['Value'] = int(row['DefaultValue'])
    except Exception as e:
        raise ImportError('Failed to process source file') from e
    return result

def export_data(filepath: str, data: dict) -> None:
    try:
        with open(filepath, 'w', newline='') as datafile:
            fieldnames=('ID', 'Type', 'Description', 'UOM', 'Value', 'RefSupplier', 'RefUrl', 'RefMfgr', 'RefMfgrPN', 'Notes')
            writer = csv.DictWriter(datafile, fieldnames, dialect=csv.excel)
            writer.writeheader()
            for part_num in data.keys():
                if (data[part_num]['Value'] == 0):
                    continue
                outdata = data[part_num]
                outdata['ID'] = part_num
                writer.writerow(outdata)
                
    except Exception as e:
        raise ExportError('Failed to export data') from e