from myhdl import block, always_comb, Signal, intbv, instance, delay
from random import randrange


@block
def Barrel_Shifter(par_in, par_out, shift_amount):
    """
    A barrel shifter with 3-bits shift amount for 12-bits register.
    :param par_in: Parallel input (12-bits).
    :param par_out: Parallel output (12-bits).
    :param shift_amount: Amount of shift to be executed (3-bits maximum).
    """

    @always_comb
    def logic():
        par_out.next = par_in >> shift_amount
    return logic


@block
def tb_barrel_shifter():
    shift_amount = Signal(intbv(0)[3:])
    par_in = Signal(intbv(0)[12:])
    par_out = Signal(intbv(0)[12:])
    bs = Barrel_Shifter(par_in, par_out, shift_amount)

    @instance
    def stimulus():
        for i in range(20):
            par_in.next = randrange(4096)  # random 12-bit number
            shift_amount.next = randrange(8)
            yield delay(10)
    return bs, stimulus




# Convert to Verilog
def convert_to_verilog():
    shift_amount = Signal(intbv(0)[3:])
    par_in = Signal(intbv(0)[12:])
    par_out = Signal(intbv(0)[12:])
    bs = Barrel_Shifter(par_in, par_out, shift_amount)
    bs.convert(name='Barrel_Shifter', hdl='Verilog')


tb = tb_barrel_shifter()
tb.config_sim(name='Barrel_Shifter', trace=True)
tb.run_sim(3000)
convert_to_verilog()

