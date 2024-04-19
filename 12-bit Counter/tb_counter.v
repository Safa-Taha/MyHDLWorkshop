module tb_counter;

reg clk;
reg rst;
reg c_en;
reg w_en;
wire [11:0] count;
reg [11:0] write_in;

initial begin
    $from_myhdl(
        clk,
        rst,
        c_en,
        w_en,
        write_in
    );
    $to_myhdl(
        count
    );
end

counter dut(
    clk,
    rst,
    c_en,
    w_en,
    count,
    write_in
);

endmodule
