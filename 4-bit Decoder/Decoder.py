from myhdl import always, block, instance, \
    always_comb, Signal, intbv, delay


# Start of Module
@block
def decoder_4bit(inpu, out, enable):
    @always_comb
    def logic():
        if enable:
            out.next = 2 ** inpu
        else:
            out.next = 0

    return logic
# End of The Module


# Test Bench
@block
def test_decoder():
    inp = Signal(intbv(0)[4:])
    en = Signal(bool(1))
    out = Signal(intbv(0)[16:])
    dec = decoder_4bit(inp, out, en)

    @always(delay(10))
    def stim():
        if inp < 15:
            inp.next = inp + 1
        else:
            inp.next = 0

    @always(delay(5))
    def enable_toggle():
        en.next = not en

    return stim, dec, enable_toggle


def simulate():
    tb = test_decoder()
    tb.config_sim(trace=True)
    tb.run_sim(1500)


def convertToVer():
    en = Signal(bool(0))
    inpu = Signal(intbv(0)[4:])
    output = Signal((intbv(0)[16:]))
    decoder = decoder_4bit(inpu, output, en)
    decoder.convert(hdl='Verilog')


if __name__ == '__main__':
    simulate()
    convertToVer()
    pass
