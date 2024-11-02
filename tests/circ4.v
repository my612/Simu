module circ4(in0, in1, in2, in3, o0, o1, en);

    input in0;
    input in1;
    input in2;
    input in3;
    
    output o0;
    output o1;

    or #(9) (o0,in3,in1);
    or #(9) (o1,in2,in3);
  
endmodule
