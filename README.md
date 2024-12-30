# Lexical Analyzer for Cminus Programming Language

This repository implements a **Lexical Analyzer** for the **Cminus** programming language. The lexical analyzer reads Cminus source code and outputs a sequence of **tokens**, each representing a fundamental element of the code. These tokens are then passed to the parser for further syntactic and semantic analysis.

This project uses **PLY (Python Lex-Yacc)**, a Python library, for lexical analysis. The lexical analyzer generates a list of tokens from the input source code file, making it easier for the parser to process the Cminus language's grammar.

---

## Features

The **Lexical Analyzer** supports the following functionality:

- **Tokenization**: Converts Cminus source code into a sequence of tokens.
- **Supported Token Types**:
  - **KEYWORD**: Reserved words in the language (e.g., `int`, `float`, `if`, `else`, `while`, etc.).
  - **IDENTIFIER**: User-defined names for variables or functions (e.g., `main`, `x`).
  - **CONSTANT**: Constant values, such as integers or floats.
  - **ARITH-OP**: Arithmetic operators (`+`, `-`, `*`, `/`, `%`).
  - **LOGIC-OP**: Logical operators (`&&`, `||`).
  - **SEPARATOR**: Symbols that separate tokens or group them together (e.g., parentheses, commas, semicolons).
  - **COMMENT**: Single-line and multi-line comments, ignored during parsing but useful for documentation.
- **Error Handling**: Prints error messages when an invalid token is encountered.

---

## Requirements

To run the lexical analyzer, you need the following:

- **Python 3.x** or higher
- **PLY Library**: A Python library for Lexical and Syntactic analysis.

You can install the required dependencies using the following command:

```bash
pip install ply
```

---

## Setup and Usage

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/rohanvenkatesha/Lexical-Analyzer-for-Cminus-Programming-Language
   cd Lexical-Analyzer-for-Cminus-Programming-Language
   ```

2. **Run the Lexical Analyzer**:

   The lexical analyzer is implemented in the `lexical_analyzer.py` script. To run the lexer on a Cminus source code file, use the following command:

   ```bash
   python lexical_analyzer.py source_code.cminus
   ```

   Replace `source_code.cminus` with the name of your input file. The lexer will output the recognized tokens along with their types.

3. **View the Tokenized Output**:

   The lexer will print the recognized tokens along with their types, for example:

   ```plaintext
   Token: int, Type: KEYWORD
   Token: main, Type: IDENTIFIER
   Token: (, Type: SEPARATOR
   Token: ), Type: SEPARATOR
   Token: {, Type: SEPARATOR
   Token: int, Type: KEYWORD
   Token: a, Type: IDENTIFIER
   Token: =, Type: ARITH-OP
   Token: 5, Type: CONSTANT
   Token: ;, Type: SEPARATOR
   ```

4. **Input Cminus Code**:

   You can use any Cminus source file for input, such as `source_code.cminus`. The lexer will read the code and output the sequence of tokens.

---

## File Structure

```plaintext
Lexical-Analyzer-for-Cminus-Programming-Language/
├── lexical_analyzer.py         # Main script for lexical analysis
├── Cminus_programming_language.pdf  # Language specification for Cminus
├── source_code.cminus          # Example Cminus source code file
├── Report.pdf                  # Report on the project
└── README.md                   # Documentation
```

---

## Example Cminus Code

Here is an example of Cminus code that can be tokenized by the lexical analyzer:

```c
int main() {
    int a = 5;
    float b = 3.14;
    
    if (a > b) {
        write("Greater\n");
    } else {
        write("Lesser\n");
    }
    
    return 0;
}
```

When processed by the lexical analyzer, it will produce tokens like:

```plaintext
Token: int, Type: KEYWORD
Token: main, Type: IDENTIFIER
Token: (, Type: SEPARATOR
Token: ), Type: SEPARATOR
Token: {, Type: SEPARATOR
Token: int, Type: KEYWORD
Token: a, Type: IDENTIFIER
Token: =, Type: ARITH-OP
Token: 5, Type: CONSTANT
Token: ;, Type: SEPARATOR
...
```

---

## Lexical Analyzer Specification

The **Lexical Analyzer** for Cminus is designed to recognize and classify the following types of tokens:

- **KEYWORD**: Reserved words in the language (e.g., `int`, `float`, `if`, `else`, `while`, `read`, `write`, `return`).
- **IDENTIFIER**: Alphanumeric strings that start with a letter and can contain digits (e.g., `main`, `x`).
- **CONSTANT**: Integer literals or floating-point literals (e.g., `5`, `3.14`).
- **ARITH-OP**: Operators that perform arithmetic operations (e.g., `+`, `-`, `*`, `/`, `%`).
- **LOGIC-OP**: Logical operators (e.g., `&&`, `||`).
- **SEPARATOR**: Symbols that separate tokens or group them together (e.g., `(`, `)`, `{`, `}`, `;`, `,`).
- **COMMENT**: Single-line comments (`// comment`) and multi-line comments (`/* comment */`).

---

## Error Handling

If the lexical analyzer encounters an invalid token or an unrecognized symbol, it will output an error message, for example:

```plaintext
Error: Invalid character '@' at line 4
```

The lexer will stop processing further once an error is encountered.

---

## Grammar Specifications

For the complete **grammar rules** of the Cminus language, refer to the **[Cminus_programming_language.pdf](Cminus_programming_language.pdf)** file in this repository. It defines the syntax and constructs supported by the language, including:

- **Data Types**: `int`, `float`
- **Control Flow**: `if`, `else`, `while`, `exit`, `return`
- **Operators**: Arithmetic, relational, logical, and assignment operators
- **Comments**: Single-line (`//`) and multi-line (`/* */`) comments
- **Keywords**: `int`, `float`, `if`, `else`, `exit`, `while`, `read`, `write`, `return`

---

## Future Improvements

- **Extended Tokenization**: Add support for string interpolation, arrays, or other advanced features.
- **Optimized Error Handling**: Improve error messages to provide more information about the source of errors.
- **Integration with Parser**: Integrate the lexical analyzer with the parser to create a complete compiler pipeline for Cminus.

---
