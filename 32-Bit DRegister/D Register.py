from myhdl import block, instance, always, always_seq, Signal, \
                  ResetSignal, intbv, delay
from random import randrange


# Start of Module
@block
def Register(clk, rst, load, par_in, par_out):
    """
    Simple 32-bit data register. It can load and reset.
    :param clk: Clock signal
    :param rst: Reset signal
    :param load: Load enable signal
    :param par_in: Parallel 32-bit input
    :param par_out: Parallel 32-bit output
    """

    @always_seq(clk.posedge, reset=rst)
    def logic():
        if load:
            par_out.next = par_in
    return logic

# End of The Module


# Start of Test Bench
@block
def test_reg32bit():
    clk, load = [Signal(bool(0)) for i in range(2)]
    rst = ResetSignal(bool(0), active=0, isasync=True)
    par_in = Signal(intbv(0)[32:])
    par_out = Signal(intbv(0)[32:])
    reg1 = Register(clk, rst, load, par_in, par_out)

    @always(delay(10))
    def clk_gen():
        clk.next = not clk

    @instance
    def res_gen():
        yield delay(5)
        rst.next = 1
        while True:
            yield delay(randrange(400, 800))
            rst.next = 0
            yield delay(randrange(100, 350))
            rst.next = 1

    @instance
    def load_gen():
        yield delay(5)
        load.next = 1
        while True:
            yield delay(randrange(30, 65))
            load.next = 0
            yield delay(randrange(20, 35))
            load.next = 1

    @always(clk.negedge)
    def stimulus():
        par_in.next = randrange(2**32)

    return reg1, clk_gen, res_gen, load_gen, stimulus

# End of Test Bench


def convert_to_verilog():
    clk, load = [Signal(bool(0)) for i in range(2)]
    rst = ResetSignal(bool(0), active=0, isasync=True)
    par_in = Signal(intbv(0)[32:])
    par_out = Signal(intbv(0)[32:])
    inst = Register(clk, rst, load, par_in, par_out)
    inst.convert(name="DRegister_32Bit", hdl='Verilog')


tb = test_reg32bit()
tb.config_sim(name='DRegister_32Bit',  trace=True)
tb.run_sim(2000)
convert_to_verilog()
