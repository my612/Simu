`timescale 1ns/1ps

module circ3(in0, in1, en, o0, o1, o2, o3);
  input in0;
  input in1;
  input en;

  output o0;
  output o1;
  output o2;
  output o3;
  
  wire w0;
  wire w1;

  not #(2) (w0, in0);
  not #(2) (w1, in1);

  and #(5) (o0, w1, w0, en);
  and #(5) (o1, w1, in0, en);
  and #(5) (o2, in1, w0, en);
  and #(5) (o3, in1, in0, en);
  
endmodule
