from myhdl import block, intbv, \
    always_seq, always, delay, Signal, instance, ResetSignal, modbv
from random import randrange

@block
def counter(clk, rst, c_en, w_en, count, write_in):
    @always_seq(clk.posedge, reset=rst)
    def logic():
        if w_en:
            count.next = write_in
        elif c_en:
            count.next = count + 1
        else:
            count.next = count
    return logic

@block
def test_counter():
    c_en, clk, w_en = [Signal(bool(0)) for i in range(3)]
    rst = ResetSignal(bool(0), active=0, isasync=True)
    count = Signal(modbv(0)[12:])
    write_in = Signal(intbv(0)[12:])
    inst = counter(clk, rst, c_en, w_en, count, write_in)

    @always(delay(5))
    def clk_gen():
        clk.next = not clk

    @instance
    def res_gen():
        yield delay(5)
        rst.next = 1
        while True:
            yield delay(50)
            rst.next = 0
            yield delay(10)
            rst.next = 1

    @instance
    def stimulus():
        w_en.next = 1
        c_en.next = 1
        write_in.next = randrange(4094, 4096)
        while True:
            yield delay(10)
            w_en.next = 0
            c_en.next = 1
            yield delay(50)
            w_en.next = 1
            c_en.next = 0
            write_in.next = randrange(4096)

    return inst, res_gen, clk_gen, stimulus

def simulate(timesteps):
    tb = test_counter()
    tb.config_sim(trace=True)
    tb.run_sim(timesteps)

def convert_to_verilog():
    en, clk, we = [Signal(bool(0)) for i in range(3)]
    rst = ResetSignal(bool(0), active=0, isasync=True)

    count = Signal(intbv(0)[12:])
    w_in = Signal(intbv(0)[12:])
    counter_1 = counter(clk, rst, en, we, count, w_in)
    counter_1.convert(hdl='Verilog')


if __name__ == '__main__':
    simulate(500)
    convert_to_verilog()