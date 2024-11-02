module circ8 (o2, o3, o1, in1, in0, o0);
  input o2;
  input o3;
  input o1;
  input in1;
  input in0;

  output o0;

  wire g;
  wire o0;

  and g_0(g, o0, o1, o2, o3);
  and g_1(o0, in0, in1);
endmodule
