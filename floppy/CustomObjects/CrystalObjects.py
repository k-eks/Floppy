from decimal import *
import ntpath
from floppy.CustomObjects import toolbox


class AtomData(object):
    """
    This class holds information about an atom.
    """

    def __init__(self):
        """
        Constructor
        """
        super(AtomData, self).__init__()

        self._name = None
        self._type = None
        self._sof = None
        self._part = None
        self._positionFract = [Decimal(0)] * 3
        self._positionFractError = [Decimal(0)] * 3
        self._usio = Decimal(0)
        self._usioError = Decimal(0)
        self._adp = None
        self._adpError = None


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    @property
    def sof(self):
        return self._sof

    @sof.setter
    def sof(self, value):
        self._sof = value


    @property
    def part(self):
        return self._part

    @part.setter
    def part(self, value):
        self._part = value


    @property
    def positionFract(self):
        return self._positionFract

    @positionFract.setter
    def positionFract(self, value):
        self._positionFract = value


    @property
    def positionFractError(self):
        return self._positionFractError

    @positionFractError.setter
    def positionFractError(self, value):
        self._positionFractError = value


    @property
    def uiso(self):
        return self._uiso

    @uiso.setter
    def uiso(self, value):
        self._uiso = value


    @property
    def uisoError(self):
        return self._uisoError

    @uisoError.setter
    def uisoError(self, value):
        self._uisoError = value


    @property
    def adp(self):
        return self._adp

    @adp.setter
    def adp(self, value):
        self._adp = value


    @property
    def adpError(self):
        return self._adpError

    @adpError.setter
    def adpError(self, value):
        self._adpError = value


    @property
    def isAnisotropic(self):
        if self._adp is None:
            return True
        else:
            return False


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
        self._atoms = []


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


    @property
    def atoms(self):
        return self._atoms

    @atoms.setter
    def atoms(self, value):
        self._atoms = value


    def parse_cif(self, pathToCif):
        """
        Reads in a cif file and extracts the information.
        :param pathToCif: string, file path to the cif
        """
        self._name = ntpath.basename(pathToCif)
        atomsStart = atomsEnd = adpStart = adpEnd = 0

        with open(pathToCif) as cifFile:
            lines = cifFile.read().splitlines()

        # IMPORTANT: read lines will be turned to lower case!
        for lineNumber, line in enumerate(lines, start=0):
            line = line.strip().lower()
            # this is a simple parser
            if line.startswith("_space_group_crystal_system"):
                self._crystalSystem = line.split()[1]
            elif line.startswith("_space_group_it_number"):
                self._sgNumber = int(line.split()[1])
            elif line.startswith("_space_group_name_h-m_alt"):
                self._sg = " ".join(line.split()[1:])
            elif line.startswith("_cell_length_a"):
                value, error = toolbox.error_string_to_decimal(line.split()[1])
                self._cell[0] = value
                self._cellErrors[0] = error
            elif line.startswith("_cell_length_b"):
                value, error = toolbox.error_string_to_decimal(line.split()[1])
                self._cell[1] = value
                self._cellErrors[1] = error
            elif line.startswith("_cell_length_c"):
                value, error = toolbox.error_string_to_decimal(line.split()[1])
                self._cell[2] = value
                self._cellErrors[2] = error
            elif line.startswith("_cell_angle_alpha"):
                value, error = toolbox.error_string_to_decimal(line.split()[1])
                self._cell[3] = value
                self._cellErrors[3] = error
            elif line.startswith("_cell_angle_beta"):
                value, error = toolbox.error_string_to_decimal(line.split()[1])
                self._cell[4] = value
                self._cellErrors[4] = error
            elif line.startswith("_cell_angle_gamma"):
                value, error = toolbox.error_string_to_decimal(line.split()[1])
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
            elif line.startswith("_atom_site_disorder_group"):
                atomsStart = lineNumber
            elif line.startswith("_atom_site_aniso_label"):
                atomsEnd = lineNumber
            elif line.startswith("_atom_site_aniso_u_12"):
                adpStart = lineNumber
            elif line.startswith("_geom_special_details"):
                adpEnd = lineNumber

        # reading out atoms, if possible
        if atomsStart != 0 and atomsEnd != 0:
            positionLines = lines[atomsStart+1:atomsEnd-1]
            adpData = lines[adpStart+1:adpEnd-1]
            self.parse_cif_atoms(positionLines, adpData)


    def parse_cif_atoms(self, positionLines, adpData):
        """
        Reads a line-by-line representation of the atoms location in a cif file.
        :param positionLines: list(string), raw lines from the position data of the cif file. Beaware of line breaks!
        :param adpData: list(string), line-wise data of the adps.
        :return: StructureModel and list(Atoms)
        """
        # cleaning up potential line breaks
        i = 0
        positionData = []
        while i  < (len(positionLines) - 1):
            line = positionLines[i]
            nextLine = positionLines[i+1]
            if len(nextLine) < 30:
                line = " ".join([line, nextLine])
                i += 1
            positionData.append(line)
            i += 1

        # transfering the position data into objects
        for line in positionData:
            parts = line.split()
            atom = AtomData()
            atom.name = parts[0]
            atom.type = parts[1]
            x, xError = toolbox.error_string_to_decimal(parts[2])
            y, yError = toolbox.error_string_to_decimal(parts[3])
            z, zError = toolbox.error_string_to_decimal(parts[4])
            atom.positionFract = [x, y, z]
            atom.positionFractError = [xError, yError, zError]
            atom.uiso, atom.usioError = toolbox.error_string_to_decimal(parts[5])
            atom.sof = parts[7]
            atom.part = parts[14]
            self._atoms.append(atom)

        # matching the adp data into the atoms
        for line in adpData:
            parts = line.split()
            uname = parts[0]
            u = []
            uError = []
            i = 1
            # puting the six adps and errors into lists
            while i < len(parts):
                value, error = toolbox.error_string_to_decimal(parts[i])
                u.append(value)
                uError.append(error)
                i += 1
            # matching atoms
            for atom in self._atoms:
                if atom.name == uname:
                    atom.adp = u
                    atom.adpError = uError

        for i in self._atoms:
            print(i.adpError)

