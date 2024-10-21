module circ4(in0, in1, in2, in3, o0, o1, en);

    input in0;
    input in1;
    input in2;
    input in3;
    
    output o0;
    output o1;

    or(o1, in3, in2);
    or(o0, in3, in1);
  
endmodule
