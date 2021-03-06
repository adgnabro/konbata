"""
    Loader and Parser for the txt format.

    Version: 0.01-beta

"""

from konbata.Data.Data import DataNode, DataTree
from konbata.Formats.Format import Format


def txt_toTree(file, delimiter=None, options=None):
    """
    Function transforms a txt file into a DataTree.

    Parameters
    ----------
    file: file
        open input file in at least read mode
    delimiter: TODO
    options: list, optional

    Returns
    -------
    tree: DataTree
    """

    tree = DataTree(tree_type='txt')

    # TODO add more options
    # TODO add column or row storage

    col0 = DataNode('')

    for row in file.readlines():
        col0.add(DataNode(row))

    tree.root.add(col0)

    return tree


def txt_fromTree(tree, file, options=None):
    """
    Function transforms a DataTree into a csv file.

    Parameters
    ----------
    tree: DataTree
    file: file
        open output file in at least write mode
    options: list, optional
    """

    if not isinstance(tree, DataTree):
        raise TypeError('tree must be type of DataTree')

    output = tree.generate_string_representation()
    file.writelines(output)


txt_format = Format('txt', [';', ','], txt_toTree, txt_fromTree)
