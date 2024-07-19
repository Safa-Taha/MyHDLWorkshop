from myhdl import *

# Two-to-one
@block

def mux_two_to_one(z,a,b,sel):
    @always_comb
    def combLogic():
        if sel == 1:
            z.next = a
        else :
            z.next=b
    return combLogic


# Three-to-one
@block

def mux_three_to_one(z,a,b,c,sel):
    @always_comb
    def comblogic():
        if sel ==1:
            z.next = a
        elif sel ==2:
            z.next = b
        elif sel ==3:
            z.next =c
        else:
            z.next=0
    return comblogic



# Convert to Verilog
def convert_to_verilog():
    z = Signal(intbv(0)[8:])
    a = Signal(intbv(0)[8:])
    b = Signal(intbv(0)[8:])
    c = Signal(intbv(0)[8:])
    sel1 = Signal(intbv(0)[2:])
    m21 =mux_two_to_one(z,a,b,sel1)
    m21.convert(name='MUX_Two_One',hdl='Verilog')

    sel2 = Signal(intbv(0)[3:])
    m31 =mux_three_to_one(z,a,b,c,sel2)
    m31.convert(name='Mux_Three_One',hdl='Verilog')


convert_to_verilog()
