from Resources import *
from FiniteStateMachineExceptions import *

def init_state(fn):
    def wrapper(*args, **kwargs):
        v = fn(*args, **kwargs)
        v.send(None)
        return v

    return wrapper


class FSM:

    _buffer = ""
    _modifier_buffer = ""
    _value_buffer = ""
    _value_buffer_list = []

    def __init__(self):
        # Чек на ошибку
        self.semicolon_exist = False

        self._init = self._create_init_state()

        self._q0_state = self._create_q0_state()
        #self._q1_state = self._create_q1_state()
        self._q2_state = self._create_q2_state()
        self._q3_state = self._create_q3_state()
        # self._q4_state = self._create_q4_state()
        # self._q5_state = self._create_q5_state()
        # self._q6_state = self._create_q6_state()
        # self._q7_state = self._create_q7_state()
        # self._q8_state = self._create_q8_state()
        # self._q9_state = self._create_q9_state()
        # self._q10_state = self._create_q10_state()
        # self._q11_state = self._create_q11_state()
        # self._q12_state = self._create_q12_state()

        self._current_state = self._init

    def send_value(self, value):
        try:
            self._current_state.send(value)
        except StopIteration:
            print("\nAnalysis completed")

    @init_state
    def _create_init_state(self):
        while True:
            value = yield
            print("\nFSM in start state")

            if value in special_characters:
                self._current_state = self._init

            elif value in alphabet:
                self._modifier_buffer += value
                self._current_state = self._q0_state

    @init_state
    def _create_q0_state(self):
        while True:
            value = yield
            print("\nFSM in q0 state")

            if value in alphabet:
                self._modifier_buffer += value
                self._current_state = self._q0_state

            elif value in special_characters:
                if self._modifier_buffer in modifiers:
                    self._modifier_buffer = ""
                    self._current_state = self._q2_state

                elif self._modifier_buffer is long:
                    self._modifier_buffer = ""
                    #to long
                    break

                elif self._modifier_buffer is short:
                    #to short
                    break

                else:
                    raise WrongModifierException("Expression contains invalid modifier")



    # @init_state
    # def _create_q1_state(self):
    #     while True:
    #         value = yield
    #         print("\nFSM in q1 state")


    @init_state
    def _create_q2_state(self):
        while True:
            value = yield
            print("\nFSM in q2 state")

            if value in special_characters:
                self._current_state = self._q2_state

            elif value in alphabet:
                self._value_buffer += value
                self._current_state = self._q3_state
            elif value in numbers:
                raise FirstDigitInTheNameException("The expression contains the first digit in the variable name")






    @init_state
    def _create_q3_state(self):
        while True:
            value = yield
            print("\nFSM in q3 state")

            if value in alphabet:
                self._value_buffer += value
                self._current_state = self._q3_state

            elif value in numbers:
                self._value_buffer += value
                self._current_state = self._q3_state

            elif value in special_characters:
                # self._current_state = self._q4_state
                break

            elif value is opening_bracket:
                # self._current_state = self._q5_state
                break
            elif value is comma:
                if self._value_buffer in self._value_buffer_list:
                    raise DuplicateVariableNamesException("Expression has duplicate variable names")

                else:
                    self._value_buffer_list.append(self._value_buffer)
                    self._value_buffer = ""
                    self._current_state = self._q2_state

            elif value is semicolon:
                if self._value_buffer in self._value_buffer_list:
                    raise DuplicateVariableNamesException("Expression has duplicate variable names")
                else:
                    self.semicolon_exist = True
                    print("\nThe expression is semantically correct")
                    break




    #
    # @init_state
    # def _create_q2_state(self):
    #     pass
    #
    # @init_state
    # def _create_q2_state(self):
    #     pass
    #
    # @init_state
    # def _create_q2_state(self):
    #     pass
    #
    # @init_state
    # def _create_q2_state(self):
    #     pass
    #
    # @init_state
    # def _create_q2_state(self):
    #     pass
    #
    # @init_state
    # def _create_q2_state(self):
    #     pass
    #
    # @init_state
    # def _create_q2_state(self):
    #     pass
    #
    # @init_state
    # def _create_q2_state(self):
    #     pass
    #
    # @init_state
    # def _create_q2_state(self):
    #     pass

    def valid_modifier(self):
        if self._modifier_buffer in modifiers:
            self._modifier_buffer = ""
            return True
        else:
            return False
