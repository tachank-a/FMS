def init_state(fn):
    def wrapper(*args, **kwargs):
        v = fn(*args, **kwargs)
        v.send(None)
        return v

    return wrapper


class FSM:
    _modifiers = {"int", "char", "double"}
    _buffer = ""
    _modifier_buffer = ""
    _alphabet1 = {'i', 'n', 't', 'a', 'b'}
    _alphabet2 = {' ', '\n', '\t', '\r'}

    def __init__(self):
        # Чек на ошибку
        self._stopped = False
        self._init = self._create_init()
        self._q0_state = self._create_q0_state()
     #   self._q1_state = self._create_q1_state()
      #  self._q2_state = self._create_q2_state()

        self._current_state = self._init

    def send_value(self, value):
        try:
            self._current_state.send(value)
        except StopIteration:
            self._stopped = True

    @init_state
    def _create_init(self):
        while True:
            value = yield
            if value in self._alphabet2:
                self.current_state = self._init
            elif value in self._alphabet1:
                self._modifier_buffer += value
                self.current_state = self._q0_state

    @init_state
    def _create_q0_state(self):
        while True:
            value = yield
            if value in self._alphabet1:
                self._modifier_buffer += value
                self._current_state = self._q0_state
            elif value in self._alphabet2:
                if self.valid_modifier():
                    print("Modifier Valid")
                    break
                else:
                    print("Modifier not Valid")
                    break



    # @init_state
    # def _create_q1_state(self):
    #     pass
    #
    # @init_state
    # def _create_q2_state(self):
    #     pass

    def valid_modifier(self):
        if self._modifier_buffer in self._modifiers:
            self._modifier_buffer = ""
            return True
        else:
            return False