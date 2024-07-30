module tb_ALU;

wire [7:0] z;
reg [7:0] a;
reg [7:0] b;
reg [3:0] sel;

initial begin
    $from_myhdl(
        a,
        b,
        sel
    );
    $to_myhdl(
        z
    );
end

ALU dut(
    z,
    a,
    b,
    sel
);

endmodule
