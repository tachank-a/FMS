from FiniteStateMachine import FSM
from FiniteStateMachineExceptions import *

input = open("input.txt")

input_as_list = list(input.read())

machine = FSM()

for value in input_as_list:
    #try-catch
        machine.send_value(value)


if not machine.semicolon_exist:
    raise InvalidExpressionException("Expected ';' at end of declaration")
