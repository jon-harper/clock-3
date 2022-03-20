#bom.py

import adsk.core, adsk.fusion

part_number_prefix = 'PN'

def generate_bom(occurences):
    bom = []
    for occ in occurences:
        comp = occ.component
        if not comp.partNumber.startswith(part_number_prefix):
            continue
        index = 0
        for item in bom:
            if item['component'] == comp:
                item['count'] += 1
                break
            index += 1

        if index == len(bom):
            bom.append({
                'component': comp,
                'name': comp.description,
                'count': 1,
                'ID': comp.partNumber
            })
    return bom

def format_bom(parts: dict):
     # Display the BOM
     ret = 'Part Number\tType\tCount\t\tUOMDescription\n'
     raw = "{}\t{}\t{}\t{}\n"
     for (id, item) in parts.items():
         if item['Value'] == 0:
             continue
         ret += raw.format(id, item['Type'], str(item['Value']), item['UOM'], item['Description'])
     return ret

def merge_source_data(bom: dict, parts : dict):
    problems = []
    for line in bom:
        if not line['ID'] in parts.keys():
            problems.append(line['ID'])
        elif line['count'] != 0:
            parts[line['ID']]['Value'] = line['count']
    return (parts, problems)