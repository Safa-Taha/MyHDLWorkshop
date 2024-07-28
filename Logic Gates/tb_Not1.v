module tb_Not1;

wire output;
reg input1;

initial begin
    $from_myhdl(
        input1
    );
    $to_myhdl(
        output
    );
end

Not1 dut(
    output,
    input1
);

endmodule
