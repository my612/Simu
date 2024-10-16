from verilog_parser.parser import parse_verilog


ast = parse_verilog(open("./tests/circ1.v").read())
print(ast)