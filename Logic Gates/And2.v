// File: And2.v
// Generated by MyHDL 0.11.45
// Date: Sun Jul 28 10:22:31 2024


`timescale 1ns/10ps

module And2 (
    output,
    input1,
    input2
);
// 2-input AND gate
// output = input1 AND input2

output output;
wire output;
input input1;
input input2;





assign output = (input1 && input2);

endmodule