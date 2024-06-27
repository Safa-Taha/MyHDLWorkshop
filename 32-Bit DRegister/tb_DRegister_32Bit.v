module tb_DRegister_32Bit;

reg clk;
reg rst;
reg load;
reg [31:0] par_in;
wire [31:0] par_out;

initial begin
    $from_myhdl(
        clk,
        rst,
        load,
        par_in
    );
    $to_myhdl(
        par_out
    );
end

DRegister_32Bit dut(
    clk,
    rst,
    load,
    par_in,
    par_out
);

endmodule
