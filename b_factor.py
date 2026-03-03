from reader.file_reader import *
import numpy as np

model_pdb = read_pdb(structure_id)

if model_pdb:
    print(f'Successfully loaded model {model_pdb.id} for {structure_id}')

residue_b_factors = []

def b_calc(model_pdb):
    """Function to calculate b-factors values for each residue and print out as a list"""
    for chain in model_pdb:
        print(f'The calculation of b-factors for chain {chain.id}:')
        for residue in chain:
            b_factor = [atom.get_bfactor() for atom in residue]
            if b_factor:
                avg_bf = np.mean(b_factor)
                residue_b_factors.append([residue.get_resname(), residue.id[1], avg_bf])
    return residue_b_factors

bf_values = b_calc(model_pdb)

if bf_values:
    print(f'Successfully calculated b-factors for {structure_id}.pdb:'
          f' {bf_values}')

