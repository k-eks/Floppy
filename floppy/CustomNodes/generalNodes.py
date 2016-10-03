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


class ToList(GeneralNode):
    """
    Turns the inputs into a list and type casts them.
    :param nodeClass: subclass object of 'Node'.
    :return: newly created Node instance.
    """
    Input("TypeCast", str, list=True)
    Input("Input1", object)
    Input("Input2", object)
    Input("Input3", object, optional=True)
    Input("Input4", object, optional=True)
    Input("Input5", object, optional=True)
    Input("Input6", object, optional=True)
    Input("Input7", object, optional=True)
    Input("Input8", object, optional=True)
    Input("Input9", object, optional=True)
    Output("NewList", object, list=True)

    def run(self):
        super(ToList, self).run()

        # Loop over inputs an put them into a new list
        newList = []
        print(self.getInputPin("Input1").info.value)
        for name in self.inputs:
            if "Input" in name: # this skips TypeCast and Trigger
                currentVar = self.getInputPin(name).info.value
                if currentVar != None:
                    if type(currentVar) == list:
                        newList.extend(currentVar)
                    else:
                        newList.append(currentVar)
        self._NewList(newList)
