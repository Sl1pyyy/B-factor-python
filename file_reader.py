from Bio.PDB.PDBParser import PDBParser

try:
    structure_id = input('Print the PDB structure code: ')
    if structure_id != structure_id.upper():
        raise ValueError('PDB structure code must be uppercase')
    if structure_id.isdigit():
        raise ValueError('PDB structure code is only digits')
    if len(structure_id) != 4:
        raise ValueError('PDB structure code must be 4 digits')
finally:
    pass

def read_pdb(structure_id):
    """Getting the PDB structure"""
    par = PDBParser(PERMISSIVE=1, QUIET=True)
    filename = f'{structure_id}.pdb'
    structure = par.get_structure(structure_id, filename)
    return structure[0]


model = read_pdb(structure_id)

if model:
    print(f'Successfully loaded Model {model.id} for {structure_id}')
