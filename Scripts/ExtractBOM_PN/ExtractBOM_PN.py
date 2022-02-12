#Author: Jonathan Harper, 2022
#Description: Fusion 360 script. Extracts basic BOM data from active components containing "PN" in the part number field. Returns the results tab delimited.
#Original Author: Autodesk Inc.

import adsk.core, adsk.fusion, traceback

part_number_prefix = 'PN'

def generate_bom(occurences):
    bom = []
    for occ in occurences:
        comp = occ.component
        if not comp.partNumber.startswith(part_number_prefix):
            continue
        jj = 0
        for bomI in bom:
            if bomI['component'] == comp:
                # Increment the instance count of the existing row.
                bomI['instances'] += 1
                break
            jj += 1

        if jj == len(bom):
            # Add this component to the BOM
            bom.append({
                'component': comp,
                'name': comp.description,
                'instances': 1,
                'part_num': comp.partNumber
            })
    return bom

def format_bom(bom):
    # Display the BOM
    ret = 'Part Number\tInstances\tName\n'
    raw = "{}\t{}\t{}\n"
    for item in bom:
        ret += raw.format(item['part_num'], str(item['instances']), item['name'])  
    return ret        

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface

        design = adsk.fusion.Design.cast(app.activeProduct)
        title = 'Extract BOM'
        if not design:
            ui.messageBox('No active design', title)
            return

        # Get all occurrences in the root component of the active design
        occurences = design.rootComponent.allOccurrences

        # Gather information about each unique component
        bom = generate_bom(occurences)
        msg = format_bom(bom)

        ui.messageBox(msg, 'Bill Of Materials')

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
