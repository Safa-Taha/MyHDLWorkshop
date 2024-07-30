module tb_Barrel_Shifter;

reg [11:0] par_in;
wire [11:0] par_out;
reg [2:0] shift_amount;

initial begin
    $from_myhdl(
        par_in,
        shift_amount
    );
    $to_myhdl(
        par_out
    );
end

Barrel_Shifter dut(
    par_in,
    par_out,
    shift_amount
);

endmodule
