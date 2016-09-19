from floppy.node import Node, Input, Output, Tag, abstractNode
import os

@abstractNode
class FileNode(Node):
    Tag('FileOperations')

class FileWriter(FileNode):
    """
    Creates a new node for file operations
    :param nodeClass: subclass object of 'Node'.
    :return: newly created Node instance.
    """
    Input('FileName', str)
    Input('Overwrite', bool, select=(True, False))
    Input('LineMode', bool, select=(True, False)) # if true, append a new line
    Input('Content', str)
    Output('Trigger', object)

    def run(self):
        super(FileWriter, self).run()

        # determine file writing conditions
        if(self._Overwrite):
            writeFlag = 'w'
        else:
            writeFlag = 'a'
        # write to file
        with open(self._FileName, writeFlag) as file:
            # some funny results are produced if the os.lineseep is added via += operator
            if(self._LineMode):
                file.write(self._Content + os.linesep)
            else:
                file.write(self._Content)