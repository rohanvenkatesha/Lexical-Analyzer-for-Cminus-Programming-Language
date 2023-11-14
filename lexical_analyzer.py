'''importing module for regular expression'''
import re

tokens = []
# regular expressions for token recognition
token_patterns = [
    ("KEYWORD", r'\b(int|main|float|if|else|exit|while|read|write|return)\b'),
    ("COMMENT", r'\/\*[\s\S]*?\*\/|\/\*[\s\S]*$'),
    ("IDENTIFIER", r'[a-zA-Z_]\w*'),
    ("CONSTANT", r'\d+(\.\d+)?'),
    ("ARITH_OP", r'[-+*/=]'),
    ("LOGIC_OP", r'==|!=|<=|>=|&&|\|\|'),
    ("SEPARATOR", r'[(),;{}[\]]')
]

def tokenize_source_code(file_name):
    ''' function to tokenize source code'''

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            source_code=[]
            lines = file.readlines()
            for line in lines:
                # Strip leading and trailing whitespace from the line and append it to the source_code list
                stripped_line = line.strip()
                source_code.append(stripped_line)
                # print (source_code)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return []

    # Combine lines into a single string
    source_text = ' '.join(source_code)
    # print(source_text)
    while source_text:
        match = None
        # pylint: disable=redefined-outer-name
        for token_type, pattern in token_patterns:
            regex = re.compile(pattern, re.DOTALL)
            # print(regex)
            match = regex.match(source_text)
            # print(match, token_type)
            if match:
                if token_type != "COMMENT":
                    token_value = match.group(0)
                else:
                    expression = source_text
                    if expression.startswith("/*"):
                        end_index = expression.find("*/")
                        if end_index != -1:
                            token_value = expression[:end_index + 2]
                        else:
                            print("Lexical error: Unclosed comment. ", expression)
                            return tokens

                tokens.append((token_type, token_value))
                source_text = source_text[len(token_value):]
                break
        if not match:
            # Handle unrecognized characters
            if source_text[0].isspace():
                source_text = source_text[1:]  # Skip whitespace
            else:
                print("Lexical error: Unable to tokenize:", source_text[0])
                source_text = source_text[1:]

    return tokens

tokens = tokenize_source_code("/workspaces/pa3-lexical-analysis-vrohan10/source_code.cminus")
templist = []
# Print the identified tokens
for token_type, token_value in tokens:
    if token_type == "COMMENT":
        templist.append((token_type, "...."))
    else:
        templist.append((token_type, token_value))

print(templist)
