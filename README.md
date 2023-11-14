# Lexical-Analyzer

Language Specification: The self-designed language is called Cminus and it has the following features:
  • It is a case-sensitive language that uses ASCII characters.
  • It supports only two data types: basic type int and a standard data type float.
  • It supports arithmetic, logical, relational, and assignment operators.
  • It supports if-else, while, and compound statements for control flow.
  • It supports single-line and multi-line comments that start with /* and end with */.
  • It supports identifiers that start with a letter and can contain alphanumeric characters.
  • It supports literals that are enclosed in single quotes for strings, and supports only decimal notation for floating point numbers.
  • It supports keywords that are reserved for the language and cannot be used as identifiers. The keywords are: int, float, if, else, exit, while, read, write, and return.

Lexical Analyzer Specification: The lexical analyzer is a program that takes an input source code file written in Cminus and produces a list of tokens as output. A token is a pair of a token type and a token value. The token types are:
  • KEYWORD: A reserved word in the language.
  • IDENTIFIER: A user-defined name for a variable or a function.
  • CONSTANT: A constant value of a data type.
  • ARITH-OP: A symbol that performs an arithmetic operation on operands.
  • LOGIC-OP: A symbol that performs a logical operation on operands.
  • SEPARATOR: A symbol that separates tokens or groups them together.
  • COMMENT: A text that is ignored by the compiler and used for documentation purposes.

The lexical analyzer should follow these steps:
  • Read the input source code file line by line and store it in a buffer.
  • Scan the buffer from left to right and identify the tokens based on the language specification.
  • For each token, create a token object with the token type and the token value as attributes.
  • Append the token object to a list of tokens.
  • Repeat steps 2 to 4 until the end of the buffer is reached or an error is encountered.
  • Return the list of tokens as output or display an error message if an error is encountered.
