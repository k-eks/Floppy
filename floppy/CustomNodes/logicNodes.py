from floppy.node import Node, Input, Output, Tag, abstractNode
import operator

@abstractNode
class LogicNode(Node):
    Tag('LogicOperations')


# creating a look up table for the operators
LogicOperators = {
    "contains": operator.contains,
    "and": operator.and_,
    "or": operator.or_
}


class BoolInversion(LogicNode):
    """
    Negates a bool variable.
    :param nodeClass: subclass object of 'Node'.
    :return: newly created Node instance.
    """
    Input('BoolIn', bool)
    Output('BoolOut', bool)

    def run(self):
        super(BoolInversion, self).run()

        self._BoolOut(not self._BoolIn)


class LogicStatements(LogicNode):
    """
    Compares to objects by a user defined statement.
    :param nodeClass: subclass object of 'Node'.
    :return: newly created Node instance.
    """
    Input('Statement1', object)
    Input('Logic', str, select=list(LogicOperators.keys()), default=list(LogicOperators.keys())[0])
    Input('Statement2', object)
    Output('Result', bool)

    def run(self):
        super(LogicStatements, self).run()

        self._Result(LogicOperators[self._Logic](self._Statement1, self._Statement2))
