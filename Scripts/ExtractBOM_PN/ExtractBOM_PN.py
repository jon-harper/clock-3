#Author: Jonathan Harper, 2022
#Description: Fusion 360 script. Extracts basic BOM data from active components containing "PN" in the part number field.
#Original Author: Autodesk Inc.

import adsk.core, adsk.fusion, traceback

from . import data_parser
from . import bom

source_path = 'C:/Users/jon/Documents/3D Print/Clockmaker/source.csv'
destination_path = 'C:/Users/jon/Documents/3D Print/Clockmaker/out.csv'

def get_occurences(design: adsk.fusion.Design) -> adsk.fusion.OccurrenceList:
    return design.rootComponent.allOccurrences

def run(context):
    app = None
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface

        design = adsk.fusion.Design.cast(app.activeProduct)
        if not design:
            ui.messageBox('No active design', 'Extract BOM')    
            return

        # Get all occurrences in the root component of the active design
        # occurences = get_occurences(design)
        occurences = get_occurences(design)

        # Gather information about each unique component
        model_parts = bom.generate_bom(occurences)
        
        (parts, problems) = bom.merge_source_data(model_parts, data_parser.import_source_data(source_path))
        # if len(problems) != 0:
        #     pass
        # msg = format_bom(parts)
        # ui.messageBox(msg, 'Bill of Materials')
        ui.messageBox(str(problems), 'Parts not found in source file')
        data_parser.export_data(destination_path, parts)

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()), 'Extract BOM')
