"""Load the Palmer Penguins data (penguins.csv) into NumPy arrays."""
import csv
import numpy as np


def load_penguins(path="penguins.csv"):
    """Return a dictionary with one NumPy array per column.

    Rows with a missing value ("NA") are skipped, leaving 333 penguins.
    Number columns become float arrays; text columns become string arrays.
    """
    columns = {}
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            if "NA" in row.values():
                continue
            for name, value in row.items():
                columns.setdefault(name, []).append(value)
    data = {}
    for name, values in columns.items():
        try:
            data[name] = np.array(values, dtype=float)
        except ValueError:
            data[name] = np.array(values)
    return data
