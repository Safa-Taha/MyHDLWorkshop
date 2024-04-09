module tb_Simple_Memory;

reg clk;
reg en;
reg [4:0] addr;
reg [7:0] din;
wire [7:0] dout;

initial begin
    $from_myhdl(
        clk,
        en,
        addr,
        din
    );
    $to_myhdl(
        dout
    );
end

Simple_Memory dut(
    clk,
    en,
    addr,
    din,
    dout
);

endmodule
