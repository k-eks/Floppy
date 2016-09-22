from floppy.node import Node, Input, Output, Tag, abstractNode

@abstractNode
class StringNode(Node):
    Tag('StringOperations')

class StringAppend(StringNode):
    """
    Creates a new node which combines two strings. These can be seperated by a delimiter.
    :param nodeClass: subclass object of 'Node'.
    :return: newly created Node instance.
    """
    Input('First', str)
    Input('Second', str)
    Input('Delimiter', str, optional=True, default='')
    Output('Joined', str)

    def run(self):
        super(StringAppend, self).run()
        self._Joined(self._Delimiter.join([self._First, self._Second]))


class ListToString(StringNode):
    """
    Creates a new node which combines two strings. These can be seperated by a delimiter.
    :param nodeClass: subclass object of 'Node'.
    :return: newly created Node instance.
    """
    Input('List', object, list=True)
    Input('Delimiter', str, optional=True, default='')
    Output('Joined', str)

    def run(self):
        super(ListToString, self).run()
        string = []
        for element in self._List:
            string.append(str(element))
        self._Joined(self._Delimiter.join(string))