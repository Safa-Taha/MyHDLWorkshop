from myhdl import block, always_comb

@block
def And2(output, input1, input2):
    """ 2-input AND gate
    output = input1 AND input2
    """
    @always_comb
    def comb():
        output.next = input1 and input2

    return comb

@block
def Or2(output, input1, input2):
    """ 2-input OR gate
    output = input1 OR input2
    """
    @always_comb
    def comb():
        output.next = input1 or input2

    return comb

@block
def Not1(output, input1):
    """ NOT gate
    output = NOT input1
    """
    @always_comb
    def comb():
        output.next = not input1

    return comb
