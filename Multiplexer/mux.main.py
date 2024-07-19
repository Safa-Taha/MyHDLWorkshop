from mux_design import mux_two_to_one, mux_three_to_one
import random
from myhdl import block, instance, Signal, intbv, delay
from mux_design import*

random.seed(5)
randrange=random.randrange


@block
def test21_mux():
    z,a,b,sel=[Signal(intbv(0)) for i in range(4)]


    mux21 =mux_two_to_one(z,a,b,sel)

    @instance
    def stimulus():
        print(" output      input(a)     input(b)   selector")
        for i in range(15):
            a.next=randrange(8)
            b.next=randrange(8)
            sel.next=randrange(2)
            
            #RANDOM INPUTS
            yield delay(1110)
            print("    %s          %s          %s          %s   " % (z, a, b, sel))
    return mux21, stimulus


@block
def test31_mux():
    z = Signal(intbv(0))
    a = Signal(intbv(0))
    b = Signal(intbv(0))
    c = Signal(intbv(0))
    sel = Signal(intbv(0))

    mux31 = mux_three_to_one(z, a, b, c, sel)
    @instance
    def stimulus():
        print("output input(a) input(b) input(c) selector")
        for i in range(15):
            a.next = randrange(5)
            b.next = randrange(5)
            c.next = randrange(5)
            sel.next = randrange(3)
            
            #RANDOM INPUTS
            yield delay(10)
            print("  %s         %s         %s       %s      %s" % (z, a, b, c, sel))

    return mux31, stimulus

tb=test21_mux()
tb.config_sim(trace=True)
tb.run_sim()
tb1 =test31_mux()
tb1.config_sim(trace=True)
tb1.run_sim()
convert_to_verilog()
