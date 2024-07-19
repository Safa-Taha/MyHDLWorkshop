module tb_Mux_Three_One;

wire [7:0] z;
reg [7:0] a;
reg [7:0] b;
reg [7:0] c;
reg [2:0] sel;

initial begin
    $from_myhdl(
        a,
        b,
        c,
        sel
    );
    $to_myhdl(
        z
    );
end

Mux_Three_One dut(
    z,
    a,
    b,
    c,
    sel
);

endmodule
