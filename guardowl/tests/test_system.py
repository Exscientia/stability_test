from guardowl.setup import create_system_from_mol, generate_molecule
from guardowl.testsystems import hipen_systems
from .conftest import generate_hipen_system


def test_generate_molecule() -> None:
    """Test if we can generate a molecule instance"""
    system, top, mol = generate_hipen_system()
    assert mol.n_conformers >= 1


def test_generate_system_top_instances() -> None:
    """Test if we can generate a system/topology instance"""
    system, topology, mol = generate_hipen_system()
    topology = topology.to_openmm()

    indices = [atom.index for atom in topology.atoms()]
    assert len(indices) > 0
