# -*- coding: utf-8 -*-
"""
    HDL Tests
    ~~~~~~~~~

    :copyright: Copyright 2006-2019 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

import pytest

from pygments.lexers import SystemVerilogLexer
from pygments.token import (Comment, Keyword, Name, Number, Operator,
                            Punctuation, Text)


@pytest.fixture(scope='module')
def lexer():
    yield SystemVerilogLexer()


SYSTEMVERILOG_BASIC_TEXT = """\
// Adder flops the sum of its inputs
module Adder #(
    parameter int N = 42
) (
    output logic [N-1:0] y,
    output logic         co,

    input  logic [N-1:0] a,
    input  logic [N-1:0] b,
    input  logic         ci,

    input  logic clk
);
    always_ff @(posedge clk) begin
        {co, y} <= a + b + ci;
    end
endmodule : Adder
"""

SYSTEMVERILOG_BASIC_TOKENS = [
    (Comment.Single, '// Adder flops the sum of its inputs\n'),
    (Keyword, 'module'),
    (Text, ' '),
    (Name, 'Adder'),
    (Text, ' '),
    (Punctuation, '#'),
    (Punctuation, '('),
    (Text, '\n'),

    (Text, '    '),
    (Keyword, 'parameter'),
    (Text, ' '),
    (Keyword.Type, 'int'),
    (Text, ' '),
    (Name, 'N'),
    (Text, ' '),
    (Operator, '='),
    (Text, ' '),
    (Number.Integer, '42'),
    (Text, '\n'),

    (Punctuation, ')'),
    (Text, ' '),
    (Punctuation, '('),
    (Text, '\n'),

    (Text, '    '),
    (Keyword, 'output'),
    (Text, ' '),
    (Keyword.Type, 'logic'),
    (Text, ' '),
    (Punctuation, '['),
    (Name, 'N'),
    (Operator, '-'),
    (Number.Integer, '1'),
    (Operator, ':'),
    (Number.Integer, '0'),
    (Punctuation, ']'),
    (Text, ' '),
    (Name, 'y'),
    (Punctuation, ','),
    (Text, '\n'),

    (Text, '    '),
    (Keyword, 'output'),
    (Text, ' '),
    (Keyword.Type, 'logic'),
    (Text, '         '),
    (Name, 'co'),
    (Punctuation, ','),
    (Text, '\n'),
    (Text, '\n'),

    (Text, '    '),
    (Keyword, 'input'),
    (Text, '  '),
    (Keyword.Type, 'logic'),
    (Text, ' '),
    (Punctuation, '['),
    (Name, 'N'),
    (Operator, '-'),
    (Number.Integer, '1'),
    (Operator, ':'),
    (Number.Integer, '0'),
    (Punctuation, ']'),
    (Text, ' '),
    (Name, 'a'),
    (Punctuation, ','),
    (Text, '\n'),

    (Text, '    '),
    (Keyword, 'input'),
    (Text, '  '),
    (Keyword.Type, 'logic'),
    (Text, ' '),
    (Punctuation, '['),
    (Name, 'N'),
    (Operator, '-'),
    (Number.Integer, '1'),
    (Operator, ':'),
    (Number.Integer, '0'),
    (Punctuation, ']'),
    (Text, ' '),
    (Name, 'b'),
    (Punctuation, ','),
    (Text, '\n'),

    (Text, '    '),
    (Keyword, 'input'),
    (Text, '  '),
    (Keyword.Type, 'logic'),
    (Text, '         '),
    (Name, 'ci'),
    (Punctuation, ','),
    (Text, '\n'),
    (Text, '\n'),

    (Text, '    '),
    (Keyword, 'input'),
    (Text, '  '),
    (Keyword.Type, 'logic'),
    (Text, ' '),
    (Name, 'clk'),
    (Text, '\n'),

    (Punctuation, ')'),
    (Punctuation, ';'),
    (Text, '\n'),

    (Text, '    '),
    (Keyword, 'always_ff'),
    (Text, ' '),
    (Punctuation, '@'),
    (Punctuation, '('),
    (Keyword, 'posedge'),
    (Text, ' '),
    (Name, 'clk'),
    (Punctuation, ')'),
    (Text, ' '),
    (Keyword, 'begin'),
    (Text, '\n'),

    (Text, '        '),
    (Punctuation, '{'),
    (Name, 'co'),
    (Punctuation, ','),
    (Text, ' '),
    (Name, 'y'),
    (Punctuation, '}'),
    (Text, ' '),
    (Operator, '<'),
    (Operator, '='),
    (Text, ' '),
    (Name, 'a'),
    (Text, ' '),
    (Operator, '+'),
    (Text, ' '),
    (Name, 'b'),
    (Text, ' '),
    (Operator, '+'),
    (Text, ' '),
    (Name, 'ci'),
    (Punctuation, ';'),
    (Text, '\n'),

    (Text, '    '),
    (Keyword, 'end'),
    (Text, '\n'),

    (Keyword, 'endmodule'),
    (Text, ' '),
    (Operator, ':'),
    (Text, ' '),
    (Name, 'Adder'),
    (Text, '\n'),
]

def test_systemverilog_basic(lexer):
    """A basic SystemVerilog test.

    Examine tokens emitted by the SV lexer for a trivial module.
    Not intended to stress any particular corner of the language.
    """
    tokens = list(lexer.get_tokens(SYSTEMVERILOG_BASIC_TEXT))
    assert tokens == SYSTEMVERILOG_BASIC_TOKENS


# Believe it or not, SystemVerilog supports spaces before and after the base
# specifier (ie 'b, 'd, 'h). See IEEE 1800-2017 Section 5.7.1 for examples.
SYSTEMVERILOG_NUMBERS_TEXT = """
8'b10101010
8 'b10101010
8'b 10101010
8'sb10101010
8'Sb10101010
8'B10101010
8'b1010_1010
8'b10xXzZ?10

24'o01234567
24 'o01234567
24'o 01234567
24'so01234567
24'So01234567
24'O01234567
24'o0123_4567
24'o01xXzZ?7

32'd27182818
32 'd27182818
32'd 27182818
32'sd27182818
32'Sd27182818
32'D27182818
32'd2718_2818
32'd27xXzZ?8

32'hdeadbeef
32 'hdeadbeef
32'h deadbeef
32'shdeadbeef
32'Shdeadbeef
32'Hdeadbeef
32'hdead_beef
32'hdexXzZ?f

'0 '1 'x 'X 'z 'Z

42 1234_5678
"""

SYSTEMVERILOG_NUMBERS_TOKENS = [
    (Number.Bin, "8'b10101010"),
    (Text, '\n'),
    (Number.Bin, "8 'b10101010"),
    (Text, '\n'),
    (Number.Bin, "8'b 10101010"),
    (Text, '\n'),
    (Number.Bin, "8'sb10101010"),
    (Text, '\n'),
    (Number.Bin, "8'Sb10101010"),
    (Text, '\n'),
    (Number.Bin, "8'B10101010"),
    (Text, '\n'),
    (Number.Bin, "8'b1010_1010"),
    (Text, '\n'),
    (Number.Bin, "8'b10xXzZ?10"),
    (Text, '\n'),
    (Text, '\n'),
    (Number.Oct, "24'o01234567"),
    (Text, '\n'),
    (Number.Oct, "24 'o01234567"),
    (Text, '\n'),
    (Number.Oct, "24'o 01234567"),
    (Text, '\n'),
    (Number.Oct, "24'so01234567"),
    (Text, '\n'),
    (Number.Oct, "24'So01234567"),
    (Text, '\n'),
    (Number.Oct, "24'O01234567"),
    (Text, '\n'),
    (Number.Oct, "24'o0123_4567"),
    (Text, '\n'),
    (Number.Oct, "24'o01xXzZ?7"),
    (Text, '\n'),
    (Text, '\n'),
    (Number.Integer, "32'd27182818"),
    (Text, '\n'),
    (Number.Integer, "32 'd27182818"),
    (Text, '\n'),
    (Number.Integer, "32'd 27182818"),
    (Text, '\n'),
    (Number.Integer, "32'sd27182818"),
    (Text, '\n'),
    (Number.Integer, "32'Sd27182818"),
    (Text, '\n'),
    (Number.Integer, "32'D27182818"),
    (Text, '\n'),
    (Number.Integer, "32'd2718_2818"),
    (Text, '\n'),
    (Number.Integer, "32'd27xXzZ?8"),
    (Text, '\n'),
    (Text, '\n'),
    (Number.Hex, "32'hdeadbeef"),
    (Text, '\n'),
    (Number.Hex, "32 'hdeadbeef"),
    (Text, '\n'),
    (Number.Hex, "32'h deadbeef"),
    (Text, '\n'),
    (Number.Hex, "32'shdeadbeef"),
    (Text, '\n'),
    (Number.Hex, "32'Shdeadbeef"),
    (Text, '\n'),
    (Number.Hex, "32'Hdeadbeef"),
    (Text, '\n'),
    (Number.Hex, "32'hdead_beef"),
    (Text, '\n'),
    (Number.Hex, "32'hdexXzZ?f"),
    (Text, '\n'),
    (Text, '\n'),
    (Number, "'0"),
    (Text, ' '),
    (Number, "'1"),
    (Text, ' '),
    (Number, "'x"),
    (Text, ' '),
    (Number, "'X"),
    (Text, ' '),
    (Number, "'z"),
    (Text, ' '),
    (Number, "'Z"),
    (Text, '\n'),
    (Text, '\n'),
    (Number.Integer, '42'),
    (Text, ' '),
    (Number.Integer, '1234_5678'),
    (Text, '\n'),
]

def test_systemverilog_numbers(lexer):
    """Test most types of numbers"""
    tokens = list(lexer.get_tokens(SYSTEMVERILOG_NUMBERS_TEXT))
    assert tokens == SYSTEMVERILOG_NUMBERS_TOKENS
