`timescale 1ns/1ps

module circ3(input [1:0] in, output[3:0] out, input en);
  wire [1:0] w;

  not(w[0], in[0]);
  not(w[1], in[1]);

  and (out[0], w[1], w[0], en);
  and (out[1], w[1], in[0], en);
  and (out[2], in[1], w[0], en);
  and (out[3], in[1], in[0], en); 
  
endmodule
