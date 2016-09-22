from floppy.node import Node, Input, Output, Tag, abstractNode
import os, ntpath

@abstractNode
class GeneralNode(Node):
    Tag('GeneralOperations')

class SelectItem(GeneralNode):
    """
    Creates a new node for list selection.
    :param nodeClass: subclass object of 'Node'.
    :return: newly created Node instance.
    """
    Input('List', object, list=True)
    Input('Index', int)
    Output('Item', object)

    def run(self):
        super(SelectItem, self).run()
        # checking against index out of range
        if int(self._Index) < len(self._List):
            self._Item(self._List[int(self._Index)])
        else:
            self._Item(0)