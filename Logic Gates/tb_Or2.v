module tb_Or2;

wire output;
reg input1;
reg input2;

initial begin
    $from_myhdl(
        input1,
        input2
    );
    $to_myhdl(
        output
    );
end

Or2 dut(
    output,
    input1,
    input2
);

endmodule
