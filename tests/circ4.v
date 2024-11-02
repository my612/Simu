`timescale 1ns/100ps
module circ4(in1, in2, in3, o0, o1);

    input in1;
    input in2;
    input in3;
    
    output o0;
    output o1;

    or #(9) g1 (o0,in3,in1);
    or #(9) g1 (o1,in2,in3);

endmodule
