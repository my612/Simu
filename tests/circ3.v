`timescale 1ns/100ps
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
  wire w2;
  wire w3;
  wire w4;
  wire w5;
  
  not #(2) g1 (w0,in0);
  not #(2) g2 (w1,in1);
  and #(5) g3 (w2,w1,w0);
  and #(5) g4 (o0,w2,en);

  and #(5) g5 (w3,w1,in0);
  and #(5) g6 (o1,w3,en);
  
  
  and #(5) g7 (w4,in1,w0);
  and #(5) g8 (o2,w4,en);
  
  
  and #(5) g9 (w5,in1,in0);
  and #(5) g10 (o3,w5,en);
  
endmodule
