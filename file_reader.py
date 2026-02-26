from Bio.PDB.PDBParser import PDBParser

"""Getting the PDB structure"""
par = PDBParser(PERMISSIVE=1)
structure_id = '1KY9'
filename = structure_id + '.pdb'

structure = par.get_structure(structure_id, filename)



