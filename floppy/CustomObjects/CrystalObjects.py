from decimal import *
import ntpath
from floppy.CustomObjects import toolbox


class StructureModel(object):
    """
    This class holds information about the crystal structure model and, if available, refinement indicators.
    """

    def __init__(self):
        """
        Constructor
        """
        super(StructureModel, self).__init__()
        self._name = None
        self._crystalSystem = None
        self._sgNumber = None
        self._sg = None
        self._cell = [Decimal(0)] * 6
        self._cellErrors = [Decimal(0)] * 6
        self._wavlength = Decimal(0)
        self._refinementIndicators = [Decimal(0)] * 3
        self._freeVariables = []


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    @property
    def crystalSystem(self):
        return self._crystalSystem

    @crystalSystem.setter
    def crystalSystem(self, value):
        self._crystalSystem = value


    @property
    def sgNumber(self):
        return self._sgNumber

    @sgNumber.setter
    def sgNumber(self, value):
        self._sgNumber = value


    @property
    def sg(self):
        return self._sg

    @sg.setter
    def sg(self, value):
        self._sg = value


    @property
    def cell(self):
        return self._cell

    @cell.setter
    def cell(self, value):
        self._cell = value


    @property
    def cellErrors(self):
        return self._cellErrors

    @cellErrors.setter
    def cellErrors(self, value):
        self._cellErrors = value


    @property
    def wavelength(self):
        return self._wavelength

    @wavelength.setter
    def wavelength(self, value):
        self._wavelength = value


    @property
    def refinementIndicators(self):
        return self._refinementIndicators

    @refinementIndicators.setter
    def refinementIndicators(self, value):
        self._refinementIndicators = value


    @property
    def freeVariables(self):
        return self._freeVariables

    @freeVariables.setter
    def freeVariables(self, value):
        self._freeVariables = value


    def parse_cif(self, pathToCif):
        """
        Reads in a cif file and extracts the information.
        :param pathToCif: string, file path to the cif
        """
        # IMPORTANT: read lines will be turned to lower case!
        self._name = ntpath.basename(pathToCif)

        with open(pathToCif) as cifFile:
            for line in cifFile:
                line = line.strip().lower()

                if line.startswith("_space_group_crystal_system"):
                    self._crystalSystem = line.split()[1]
                elif line.startswith("_space_group_it_number"):
                    self._sgNumber = int(line.split()[1])
                elif line.startswith("_space_group_name_h-m_alt"):
                    self._sg = " ".join(line.split()[1:])
                elif line.startswith("_cell_length_a"):
                    value, error = toolbox.error_string_to_float(line.split()[1])
                    self._cell[0] = value
                    self._cellErrors[0] = error
                elif line.startswith("_cell_length_b"):
                    value, error = toolbox.error_string_to_float(line.split()[1])
                    self._cell[1] = value
                    self._cellErrors[1] = error
                elif line.startswith("_cell_length_c"):
                    value, error = toolbox.error_string_to_float(line.split()[1])
                    self._cell[2] = value
                    self._cellErrors[2] = error
                elif line.startswith("_cell_angle_alpha"):
                    value, error = toolbox.error_string_to_float(line.split()[1])
                    self._cell[3] = value
                    self._cellErrors[3] = error
                elif line.startswith("_cell_angle_beta"):
                    value, error = toolbox.error_string_to_float(line.split()[1])
                    self._cell[4] = value
                    self._cellErrors[4] = error
                elif line.startswith("_cell_angle_gamma"):
                    value, error = toolbox.error_string_to_float(line.split()[1])
                    self._cell[5] = value
                    self._cellErrors[5] = error
                elif line.startswith("_diffrn_radiation_wavelength"):
                    self._wavelength = Decimal(line.split()[1])
                elif line.startswith("_refine_ls_r_factor_gt"):
                    self._refinementIndicators[0] = Decimal(line.split()[1])
                elif line.startswith("_refine_ls_wr_factor_ref"):
                    self._refinementIndicators[1] = Decimal(line.split()[1])
                elif line.startswith("_refine_ls_goodness_of_fit_ref"):
                    self._refinementIndicators[2] = Decimal(line.split()[1])
                elif line.startswith("fvar"):
                    fvars = line.split()[1:]
                    for value in fvars:
                        self._freeVariables.append(Decimal(value))